## Contributing

If you've spotted a problem with this package or have a new feature request please [open an issue](https://github.com/Invincibear/paddle-billing-python-sdk/issues) or a [submit a PR](https://github.com/Invincibear/paddle-billing-python-sdk/pulls).


## Set up dev environment
``` bash
git clone https://github.com/invincibear/paddle-billing-python-sdk && \
cd paddle-billing-python-sdk && \
pip install .[dev]
```


## Run tests
Python `pytest` tests can be run either by changing into the `paddle-billing-python-sdk`, activating the `venv`, and running `pytest`, or by running `pytest` directly
``` bash
cd paddle-billing-python-sdk && .venv/bin/pytest
```
``` bash
cd paddle-billing-python-sdk && \
source .venv/bin/activate && \
pytest
```

You can run specific tests by passing a parameter to `pytest`. For example, you can run all tests within a directory:
``` bash
pytest tests/Unit
```
Or you can run an individual test within a file:
``` bash
pytest tests/Unit/Notification/test_Verifier.py::TestVerifier::test_validate_paddle_signature_header_integrity
```

#### Use the command `deactivate` to exit the `venv`.
