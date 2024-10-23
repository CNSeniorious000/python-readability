from pathlib import Path

from js import eval as js_eval  # type: ignore
from pyodide.ffi import JsProxy, to_js

cjs = Path(__file__).parent / "parse.cjs"

script = f"( ()=>{{ const module = {{}}; {cjs.read_text()}; return module.exports.parse }})()"

js_parse = js_eval(script)


def parse(html: str, options: dict):
    result: JsProxy = js_parse(html, to_js(options)) if options else js_parse(html)
    return result.to_py()
