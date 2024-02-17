from enum import EnumMeta, StrEnum

from paddle_billing.Undefined import Undefined


# Copied from enum.py because IDE complains when calling protected class super()._is_dunder
def _is_dunder(name):
    """
    Returns True if a __dunder__ name, False otherwise.
    """
    return (
            len(name) > 4 and
            name[:2] == name[-2:] == '__' and
            name[2] != '_' and
            name[-3] != '_'
    )



class PaddleStrEnumMeta(EnumMeta):
    """
    Returns Undefined() by default when a property doesn't exist
    This provides some flexibility for the SDK to handle Paddle adding new properties to their APIspec
    """

    def __getattr__(cls, name):
        if _is_dunder(name):
            raise AttributeError(name)

        try:
            return super().__getattr__(name)
        except AttributeError:
            return Undefined()



class PaddleStrEnum(StrEnum, metaclass=PaddleStrEnumMeta):
    """
    Subclass of StrEnum but uses PaddleStrEnumMeta metaclass to set Undefined() value to undefined enum keys
    """

    @classmethod
    def is_known(cls) -> bool:
        """Not yet implemented"""
