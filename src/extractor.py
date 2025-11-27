import html5lib

URL_PREFIX = "https://developer.mozilla.org"
SECTIONS = ".//div[@class='reference-layout__body']/section[@class='content-section']"
HEADER = ".//h2/a"


def extract_sections(webpage: str) -> dict[str, dict[str, dict]]:
    ROWS = ".//tbody/tr"
    ELEMENT_INFO = ".//td"
    TAG = ".//code"
    LINK = ".//a"

    # https://github.com/html5lib/html5lib-python/issues/489
    document = html5lib.parse(webpage, namespaceHTMLElements=False)
    sections = {}

    for section in document.findall(SECTIONS):
        header = section.find(HEADER)

        if header is None:
            continue

        header = "".join(header.itertext())
        header = clean_text(header)

        if header == "See also":
            continue

        sections[header] = {}

        for row in section.findall(ROWS):
            infos = row.findall(ELEMENT_INFO)

            if len(infos) != 2:
                continue

            tag = infos[0].find(TAG)
            tag = tag.text.removeprefix("<").removesuffix(">")
            url = infos[0].find(LINK)
            short_desc = "".join(infos[1].itertext())
            short_desc = short_desc.strip()

            if url is not None:
                url = URL_PREFIX + url.get("href")

            sections[header][tag] = {
                "url": url,
                "short_desc": short_desc,
            }

            if url is None:
                continue

    return sections


def extract_details(webpage: str) -> dict:
    DESCRIPTION = (
        ".//div[@class='reference-layout__header']//section[@class='content-section']"
    )

    LIST = ".//dl"
    ATTRIBUTE = ".//a/code"
    DEPRECATED = ".//abbr[@class='icon icon-deprecated']"

    # https://github.com/html5lib/html5lib-python/issues/489
    document = html5lib.parse(webpage, namespaceHTMLElements=False)
    details = {
        "attributes": {},
        "long_desc": "",
    }

    description = document.find(DESCRIPTION)

    if description is not None:
        description = "".join(description.itertext())
        details["long_desc"] = clean_text(description)

    for section in document.findall(SECTIONS):
        header = section.find(HEADER)

        if header is None:
            continue

        header = "".join(header.itertext())
        header = clean_text(header)

        if header != "Attributes":
            continue

        attributes = {}
        attribute = None
        deprecated = False

        for element in section.find(LIST) or []:
            if element.tag == "dt":
                # Extract.
                attribute = element.find(ATTRIBUTE)
                attribute = "".join(attribute.itertext())
                deprecated = element.find(DEPRECATED) is not None

                # Set.
                attributes[attribute] = {
                    "description": "",
                    "deprecated": deprecated,
                    "boolean": False,
                }
            elif attribute and element.tag == "dd":
                # Extract.
                description = "".join(element.itertext())
                description = clean_text(description)
                boolean = "A Boolean attribute" in description

                # Set.
                attributes[attribute]["description"] = description
                attributes[attribute]["boolean"] = boolean

                # Reset.
                attribute = None
                deprecated = False
            else:
                # Reset.
                attribute = None
                deprecated = False

        details["attributes"] = attributes

    return details


def clean_text(text: str) -> str:
    text = text.replace("\n", "").strip()

    while text.find("  ") != -1:
        text = text.replace("  ", " ")

    return text
