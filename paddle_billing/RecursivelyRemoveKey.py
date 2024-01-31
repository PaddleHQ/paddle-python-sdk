def recursively_remove_key(data: list | dict | None, key_to_remove: str):
    """Remove key recursively from a dict or list"""

    if data is None:
        return

    if isinstance(data, dict):
        if key_to_remove in data:
            del data[key_to_remove]
        for value in data.values():
            recursively_remove_key(value, key_to_remove)
    elif isinstance(data, list):
        for item in data:
            recursively_remove_key(item, key_to_remove)
