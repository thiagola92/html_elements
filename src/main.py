import requests
from json import dumps
from pathlib import Path

from extractor import extract_sections, extract_details, extract_globals

OUTPUT = "output/output.json"
URL_ELEMENTS = "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements"
URL_GLOBALS = (
    "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes"
)

response = requests.get(URL_ELEMENTS)
webpage = response.content
sections = extract_sections(webpage)

Path(OUTPUT).write_text(dumps(sections, indent=2))

response = requests.get(URL_GLOBALS)
webpage = response.content
global_attributes = extract_globals(webpage)

for s in sections.values():
    for i in s.values():
        if url := i.get("url"):
            print(url)

            response = requests.get(url)

            if response.ok:
                webpage = response.content
                details = extract_details(webpage)
                details.update(global_attributes)

                i.update(details)

Path(OUTPUT).write_text(dumps(sections, indent=2))
