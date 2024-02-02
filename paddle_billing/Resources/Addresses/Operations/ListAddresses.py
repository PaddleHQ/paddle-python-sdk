from paddle_billing.EnumStringify import enum_stringify
from paddle_billing.HasParameters import HasParameters

from paddle_billing.Entities.Shared import Status

from paddle_billing.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing.Resources.Shared.Operations import Pager


class ListAddresses(HasParameters):
    def __init__(
            self,
            pager:    Pager        | None = None,
            ids:      list[str]    | None = None,
            statuses: list[Status] | None = None,
            search:   str          | None = None,
    ):
        self.pager    = pager
        self.search   = search
        self.ids      = ids      if ids      is not None else []
        self.statuses = statuses if statuses is not None else []

        # Validation
        if any(not isinstance(aid, str) for aid in self.ids):
            raise InvalidArgumentException('ids', 'string')
        if any(not isinstance(status, Status) for status in self.statuses):
            raise InvalidArgumentException('statuses', Status.__name__)


    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters['id'] = ','.join(self.ids)
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.search:
            parameters['search'] = self.search

        return parameters
