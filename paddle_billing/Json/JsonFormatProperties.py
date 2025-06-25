def json_format_properties(properties: list[str]):
    def wrapper(cls):
        cls.json_format_properties = properties
        return cls

    return wrapper
