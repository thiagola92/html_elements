# HTML Elements

Scraped from
[MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#interactive_elements).

- [JSON](output/output.json)

Elements are splitted in sections. For example `<html>` can be found in the "Main root" section:

```jsonc
{
  "Main root": {
    "html": {
      "url": "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html",
      "short_desc": "Short description.",
      "attributes": {
        "version": {
          "description": "Attribute description.",
          "deprecated": true,
          "boolean": false
        },
        "xmlns": {
          "description": "Attribute description.",
          "deprecated": false,
          "boolean": false
        }
      },
      "long_desc": "Long description."
    }
  },
  // Other sections...
}
```

## Usage

Make sure to install uv: https://docs.astral.sh/uv/getting-started/installation/

Install dependencies:

```
uv sync
```

Execute scraper:

```
uv run src/main.py
```

## Questions

Why not from [WHATWG](https://html.spec.whatwg.org/#toc-semantics)?

> It is very annoying to scrape this website.

Why not use [webref](https://github.com/w3c/webref/tree/main)?

> No patience to learn about the repository and about Web IDL, just to use in
> this project.
