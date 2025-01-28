def json_exclude(properties: list[str]):
    def wrapper(cls):
        cls.json_exclude_properties = properties
        return cls

    return wrapper
