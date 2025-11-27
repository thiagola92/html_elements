from json import dumps
from pathlib import Path

from extractor import extract_details, extract_sections

CACHE_ELEMENTS = "src/cache/elements.html"
CACHE_TAGS = "src/cache/tags"

webpage = Path(CACHE_ELEMENTS).read_text()
sections = extract_sections(webpage)

Path("test0.json").write_text(dumps(sections, indent=2))

details = {}

for f in Path(CACHE_TAGS).iterdir():
    print(f.stem)
    details[f.stem] = extract_details(f.read_text())

Path("test1.json").write_text(dumps(details, indent=2))
