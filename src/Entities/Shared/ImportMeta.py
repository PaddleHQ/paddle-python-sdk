from __future__  import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class ImportMeta:
    externalId:   str | None
    importedFrom: str


    @classmethod
    def from_dict(cls, data: dict) -> ImportMeta:
        return ImportMeta(
            externalId   = data.get('external_id'),
            importedFrom = data['imported_from']
        )
