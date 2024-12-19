from sys import platform

if platform == "emscripten":
    from .pyodide import parse
else:
    from .pythonmonkey import parse

__all__ = ["parse"]
