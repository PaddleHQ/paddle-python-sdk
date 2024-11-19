from json import JSONEncoder
from dataclasses import fields, is_dataclass
from datetime import datetime
import re

from paddle_billing.Entities.DateTime import DateTime
from paddle_billing.FiltersUndefined import FiltersUndefined
from paddle_billing.Undefined import Undefined


class PayloadEncoder(JSONEncoder):
    def default(self, z):
        if isinstance(z, Undefined):
            return None

        if isinstance(z, datetime):
            return DateTime.from_datetime(z)

        if hasattr(z, "to_json") and callable(z.to_json):
            return z.to_json()

        if is_dataclass(z):
            exclude_properties = getattr(z.__class__, "json_exclude_properties", [])
            format_properties = getattr(z.__class__, "json_format_properties", None)

            data = {}
            for field in fields(z):
                key = (
                    self._camel_to_snake(field.name)
                    if format_properties and field.name in format_properties
                    else field.name
                )

                if field.name not in exclude_properties:
                    data[key] = getattr(z, field.name)

            return FiltersUndefined.filter_undefined_values(data)

        return super().default(z)

    def _camel_to_snake(self, name: str) -> str:
        return re.sub(r"(?<!^)(?=[A-Z])", "_", name).lower()
