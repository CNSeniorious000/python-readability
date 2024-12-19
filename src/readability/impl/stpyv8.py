from STPyV8 import JSContext

from .common import parse_getter

ctx = JSContext()
ctx.__enter__()

js_parse = ctx.eval(parse_getter())


def parse(html: str, options: dict):
    result = js_parse(html, options) if options else js_parse(html)
    return {**result}
