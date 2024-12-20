from __future__ import annotations

from json import dumps
from typing import TYPE_CHECKING

from py_mini_racer import MiniRacer

from .common import parse_getter

if TYPE_CHECKING:
    from py_mini_racer import JSFunction
    from py_mini_racer._objects import JSMappedObject


ctx = MiniRacer()
ctx.__enter__()

js_parse: JSFunction = ctx.eval(parse_getter())  # type: ignore


def parse(html: str, options: dict):
    result: JSMappedObject = js_parse(html, ctx.eval(f"({dumps(options)})")) if options else js_parse(html)  # type: ignore
    return {**result}
