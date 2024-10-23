from pathlib import Path

from pythonmonkey import JSObjectProxy, null
from pythonmonkey.require import require

js_parse = require(str(Path(__file__, "../parse.cjs").resolve()))["parse"]


def parse(html: str, options: dict):
    result: JSObjectProxy = js_parse(html, options) if options else js_parse(html)
    return {k: v if v is not null else None for k, v in result.items()}
