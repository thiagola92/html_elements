from json import dumps
from pathlib import Path

from extractor import extract_details, extract_sections

CACHE_ELEMENTS = "src/cache/elements.html"
CACHE_TAGS = "src/cache/tags"
OUTPUT_00 = "output/test_output_00.json"
OUTPUT_01 = "output/test_output_01.json"

webpage = Path(CACHE_ELEMENTS).read_text()
sections = extract_sections(webpage)

Path(OUTPUT_00).write_text(dumps(sections, indent=2))

details = {}

for f in Path(CACHE_TAGS).iterdir():
    print(f.stem)

    details[f.stem] = extract_details(f.read_text())

Path(OUTPUT_01).write_text(dumps(details, indent=2))
