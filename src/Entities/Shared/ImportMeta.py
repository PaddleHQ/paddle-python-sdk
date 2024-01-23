from __future__  import annotations
from dataclasses import dataclass
from typing      import Optional


@dataclass(frozen=True)
class ImportMeta:
    externalId:   Optional[str]
    importedFrom: str


    @classmethod
    def from_dict(cls, data: dict) -> ImportMeta:
        return ImportMeta(
            externalId   = data.get('external_id'),
            importedFrom = data['imported_from']
        )
