from sys import platform

if platform == "emscripten":
    from .pyodide import parse
else:
    from .non_pyodide import parse

__all__ = ["parse"]
