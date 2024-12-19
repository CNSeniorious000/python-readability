from js import eval as js_eval  # type: ignore
from pyodide.ffi import JsProxy, to_js

from .common import parse_getter

js_parse = js_eval(parse_getter())


def parse(html: str, options: dict):
    result: JsProxy = js_parse(html, to_js(options)) if options else js_parse(html)
    return result.to_py()
