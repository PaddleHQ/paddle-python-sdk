from datetime           import datetime
from src.Entities       import Events
from src.Entities.Event import EventTypeName



class TransactionCreated(Events):
    def __init__(self, event_id: str, event_type: EventTypeName, occurred_at: datetime, data: TransactionWithIncludes):
        super().__init__(event_id, event_type, occurred_at, data)
