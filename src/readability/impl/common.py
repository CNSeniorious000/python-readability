from pathlib import Path

cjs_file = Path(__file__, "../parse.cjs").resolve()


def parse_getter():
    return f"( ()=>{{ const module = {{}}; {cjs_file.read_text('utf-8')}; return module.exports.parse }})()"
