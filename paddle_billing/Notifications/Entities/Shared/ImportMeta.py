from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class ImportMeta:
    external_id: str | None
    imported_from: str

    @staticmethod
    def from_dict(data: dict) -> ImportMeta:
        return ImportMeta(
            external_id=data.get("external_id"),
            imported_from=data["imported_from"],
        )
