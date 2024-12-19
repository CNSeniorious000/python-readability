from json import dumps

from py_mini_racer import MiniRacer

from .common import parse_getter

ctx = MiniRacer()
ctx.__enter__()

js_parse = ctx.eval(parse_getter())


def parse(html: str, options: dict):
    result = js_parse(html, ctx.eval(f"({dumps(options)})")) if options else js_parse(html)
    return {**result}
