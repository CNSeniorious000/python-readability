def to_camel_case(snake: str):
    components = snake.replace("json_ld", "JSONLD").replace("base_uri", "baseURI").split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def to_camel_cases(snakes: dict):
    return {to_camel_case(k): v for k, v in snakes.items()}


def to_snake_case(camel: str):
    return "".join(["_" + c.lower() if c.isupper() else c for c in camel])


def to_snake_cases(camels: dict):
    return {to_snake_case(k): v for k, v in camels.items()}
