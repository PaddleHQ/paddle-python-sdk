from abc import ABC, abstractmethod


class HasParameters(ABC):
    @abstractmethod
    def get_parameters(self) -> dict:
        """
        Implementations of this method should return a dictionary of parameters
        suitable to be used in API calls, e.g., {'foo': 'bar'} which would result in foo=bar in an API call.
        """
        pass
