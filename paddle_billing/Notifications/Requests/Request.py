from typing import Optional, Protocol

from paddle_billing.Notifications.Requests.Headers import Headers


class Request(Protocol):
    body: Optional[bytes]
    content: Optional[bytes]
    data: Optional[bytes]
    headers: Headers
