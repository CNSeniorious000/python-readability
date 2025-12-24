from json import dumps, loads
from pathlib import Path
from shutil import which
from subprocess import PIPE, Popen
from typing import Any, NotRequired, TypedDict, Union

from .common import parse_getter

node_bin = which("node") or which("deno") or which("bun")

assert node_bin is not None, "Node.js, Deno or Bun executable need to be installed to use the subprocess implementation"

process = Popen([node_bin, str(Path(__file__, "../stdio-worker.js").resolve())], stdout=PIPE, stdin=PIPE, text=True, encoding="utf-8")


class Ok(TypedDict):
    result: Any


class Error(TypedDict):
    name: str
    message: str
    stack: NotRequired[str]


class Err(TypedDict):
    error: Error


class JsEvaluationError(Exception):
    def __init__(self, error: Error):
        self.name = error["name"]
        self.message = error["message"]
        self.stack = error.get("stack")
        super().__init__(f"{self.name}: {self.message}\n{self.stack}" if self.stack else f"{self.name}: {self.message}")


def eval_js(code: str):
    print(dumps(code), file=process.stdin, flush=True)
    assert process.stdout is not None, process
    ret: Union[Ok, Err] = loads(process.stdout.readline())
    if error := ret.get("error"):
        raise JsEvaluationError(error)
    return ret.get("result")


eval_js(f"globalThis.parse = {parse_getter()}")


def parse(html: str, options: dict):
    return eval_js(f"parse({html!r}, {dumps(options)})")
