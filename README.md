# HTML Elements

> [!WARNING]
> Deprecated
> 
> Use the following repository: https://github.com/mdn/browser-compat-data  
> There a section that tells you that you can download the [complete JSON](https://github.com/mdn/browser-compat-data?tab=readme-ov-file#other-languages)  

Scraped from
[MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#interactive_elements).

- [JSON](output/output.json)

Elements are splitted in sections. For example `<html>` can be found in the
"Main root" section:

```jsonc
{
  "sections": {
    "Main root": {
      "html": {
        "url": "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html",
        "short_desc": "Represents the root (top-level element) of an HTML document, so it is also referred to as the root element. All other elements must be descendants of this element.",
        "attributes": {
          "version": {
            "description": "Specifies the version of the HTML Document Type Definition that governs the current document. This attribute is not needed, because it is redundant with the version information in the document type declaration.",
            "deprecated": true,
            "nonstandard": false,
            "experimental": false,
            "boolean": false
          },
          "xmlns": {
            "description": "Specifies the XML Namespace of the document. Default value is \"http://www.w3.org/1999/xhtml\". This is required in documents parsed with XML parsers, and optional in text/html documents.",
            "deprecated": false,
            "nonstandard": false,
            "experimental": false,
            "boolean": false
          }
        },
        "long_desc": "The <html> HTML element represents the root (top-level element) of an HTML document, so it is also referred to as the root element. All other elements must be descendants of this element. There can be only one <html> element in a document."
      }
    }
    // Other sections...
  },
  "global_attributes": {
    // All global attributes...
  }
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
