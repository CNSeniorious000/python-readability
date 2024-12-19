from sys import platform

if platform == "emscripten":
    from .pyodide import parse
else:
    try:
        from .stpyv8 import parse
    except ModuleNotFoundError:
        try:
            from .mini_racer import parse
        except ModuleNotFoundError:
            try:
                from .pythonmonkey import parse
            except ModuleNotFoundError:
                from .node_subprocess import parse


__all__ = ["parse"]
