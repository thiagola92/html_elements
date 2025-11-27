import requests
from json import dumps
from pathlib import Path

from extractor import extract_sections, extract_details

URL = "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements"
OUTPUT = "output/output.json"

response = requests.get(URL)
webpage = response.content
sections = extract_sections(webpage)

Path(OUTPUT).write_text(dumps(sections, indent=2))

for s in sections.values():
    for i in s.values():
        if url := i.get("url"):
            print(url)

            response = requests.get(url)

            if response.ok:
                webpage = response.content
                details = extract_details(webpage)

                i.update(details)

Path(OUTPUT).write_text(dumps(sections, indent=2))
