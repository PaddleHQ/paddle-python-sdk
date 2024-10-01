def _is_dunder(name):
    """
    Returns True if a __dunder__ name, False otherwise.
    """
    return len(name) > 4 and name[:2] == name[-2:] == "__" and name[2] != "_" and name[-3] != "_"


class PaddleStrEnumMeta(type):
    def __new__(cls, name, bases, attrs):
        # Store the original attrs to ensure we have all the class attributes
        original_attrs = dict(attrs)

        # Create the new class with the original attributes
        new_class = super().__new__(cls, name, bases, attrs)

        # Create instances for all enum members
        for key, value in original_attrs.items():
            if _is_dunder(key) or not isinstance(value, str):
                continue
            # Set enum member as instance of the class
            setattr(new_class, key, new_class(value))

        return new_class

    def __getattr__(cls, name):
        if _is_dunder(name):
            raise AttributeError(name)

        return cls(str(name).lower())


class PaddleStrEnum:
    value = None
    name = None

    _members = None
    _iter_index = 0

    _unknown_name = "Undefined"

    def __init__(self, value) -> None:
        members = self.members()
        try:
            search = list(members.values()).index(value)
            self.value = value
            self.name = list(members.keys())[search]
        except ValueError:
            self.value = value
            self.name = self._unknown_name

    def __iter__(self) -> "PaddleStrEnum":
        self._iter_index = 0
        return self

    def __next__(self) -> tuple:
        members = self.members()

        if self._iter_index >= len(members):
            raise StopIteration

        const_name = list(members.keys())[self._iter_index]
        const_value = members[const_name]
        self._iter_index += 1

        return const_name, const_value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}.{self.name}: {self.value}>"

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.value == other

        if isinstance(other, PaddleStrEnum):
            return self.value == other.value and self.name == other.name

        return False

    @classmethod
    def members(cls) -> dict:
        if not cls._members:
            members = dict(filter(lambda item: not item[0].startswith("__"), cls.__dict__.items()))
            cls._members = dict(zip(members.keys(), members.values()))
        return cls._members

    def is_known(self):
        return not self.name == self._unknown_name

    def to_json(self):
        return str(self)
