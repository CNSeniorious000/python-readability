# Readability.py

This is a Python wrapper for [@mozilla/readability](https://github.com/mozilla/readability), a standalone version of the readability library used for [Firefox Reader View](https://support.mozilla.org/kb/firefox-reader-view-clutter-free-web-pages).

## Installation

```sh
pip install python-readability
```

## Usage

```py
from readability import parse

parse(html_string, **options)
```

See the original documentation and the type hints for details.

## Requirements

Since this package is a wrapper for the original JavaScript library, it use a JavaScript engine to run the code.

For now, if you are running this package in a regular CPython environment, it will use [pythonmonkey](https://github.com/Distributive-Network/PythonMonkey) to interpret JavaScript, which requires Python 3.8+.

This package is also available inside [pyodide](https://github.com/pyodide/pyodide) because it can use the native JavaScript engine that `pyodide` runs on.
