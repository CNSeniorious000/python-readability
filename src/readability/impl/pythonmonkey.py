from pythonmonkey import JSObjectProxy, null
from pythonmonkey.require import require

from .common import cjs_file

js_parse = require(str(cjs_file))["parse"]


def parse(html: str, options: dict):
    result: JSObjectProxy = js_parse(html, options) if options else js_parse(html)
    return {k: v if v is not null else None for k, v in result.items()}
