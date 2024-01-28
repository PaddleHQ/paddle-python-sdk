class FakeResponse:
    """This is the easiest way to simulate a Requests response object"""

    def __init__(self, headers = None, content = ''):
        self.headers = headers if headers is not None else {}
        self.content = content.encode() if isinstance(content, str) else content
