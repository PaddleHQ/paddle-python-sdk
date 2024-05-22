[![Build Status](https://img.shields.io/github/actions/workflow/status/PaddleHQ/paddle-python-sdk/publish_to_pypi.yml)](https://github.com/PaddleHQ/paddle-python-sdk/actions/?query=branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/paddle-python-sdk.svg)](https://pypi.python.org/pypi/paddle-python-sdk)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/paddle-python-sdk.svg)](https://pypi.python.org/pypi/paddle-python-sdk/)
[![License: Apache 2.0](https://img.shields.io/github/license/PaddleHQ/paddle-python-sdk)](http://www.apache.org/licenses/LICENSE-2.0)


# paddle-python-sdk
[Paddle Billing](https://www.paddle.com/billing?utm_source=dx&utm_medium=paddle-python-sdk) is a complete digital product sales and subscription management platform, designed for modern software businesses. It helps you increase your revenue, retain customers, and scale your operations.

This is a [Python](https://www.python.org/) SDK that you can use to integrate Paddle Billing with applications written in Python.

For working with Paddle in your frontend, use [Paddle.js](https://developer.paddle.com/paddlejs/overview?utm_source=dx&utm_medium=paddle-python-sdk). You can open checkouts, securely collect payment information, build pricing pages, and integrate with Paddle Retain.

> **Important:** This package works with Paddle Billing. It does not support Paddle Classic. To work with Paddle Classic, see: [Paddle Classic API reference](https://developer.paddle.com/classic/api-reference/1384a288aca7a-api-reference?utm_source=dx&utm_medium=paddle-python-sdk)


## Table of contents
- [Requirements](#Requirements)
- [Install](#Install)
- [Usage](#Usage)
- [Examples](#Examples)
- [Resources](#Resources)

## Requirements
Python>=3.11 (for native type hinting, StrEnum, trailing commas, f-strings)

**Project dependencies** (automatically installed by pip):
- requests>=2.31
- urllib3>=2.1.0


## Install
Because `paddle-python-sdk` is [available on PyPi](https://pypi.org/project/paddle-python-sdk/), installation is as simple as running the following `pip` command: 

`pip install paddle-python-sdk`



## Usage
To authenticate, you'll need an API key. You can create and manage API keys in **Paddle > Developer tools > Authentication**.

Pass your API key while initializing a new Paddle client:
``` python
from paddle_billing import Client

paddle = Client('PADDLE_API_SECRET_KEY')
```

You can pass your Paddle API secret key into the SDK from an environment variable:
``` python
from os             import getenv
from paddle_billing import Client

paddle = Client(getenv('PADDLE_API_SECRET_KEY'))
```

You can also pass an environment to work with Paddle's sandbox:
``` python
from paddle_billing import Client, Environment, Options

paddle = Client('PADDLE_API_SECRET_KEY', options=Options(Environment.SANDBOX))
```

Keep in mind that API keys are separate for your sandbox and live accounts, so you'll need to generate keys for each environment.



## Examples
There are examples included in the [examples folder](https://github.com/PaddleHQ/paddle-python-sdk/tree/main/examples). To prevent leaking errors we recommend encapsulating Paddle operations inside Try/Except blocks. For brevity, most of the examples below do not do this.

### List entities
You can list supported entities with the `list()` method in the resource. It returns an iterator to help when working with multiple pages.
``` python
from paddle_billing import Client

paddle = Client('PADDLE_API_SECRET_KEY')

products = paddle.products.list()

# list() returns an iterable, so pagination is automatically handled
for product in products:
    print(f"Product's id: {product.id}")
```

### Get an entity
You can get an entity with the `get()` method in the resource. It accepts the `id` of the entity to get. The entity is returned.
``` python
from paddle_billing import Client

paddle = Client('PADDLE_API_SECRET_KEY')

product = paddle.products.get('PRODUCT_ID')
```

### Create an entity
You can create a supported entity with the `create()` method in the resource. It accepts the resource's corresponding `CreateOperation` e.g. `CreateProduct`. The created entity is returned.

``` python
from paddle_billing                               import Client
from paddle_billing.Entities.Shared.TaxCategory   import TaxCategory
from paddle_billing.Resources.Products.Operations import CreateProduct

paddle = Client('PADDLE_API_SECRET_KEY')

created_product = paddle.products.create(CreateProduct(
    name         = 'My Product',
    tax_category = TaxCategory.Standard,
))
```

### Update an entity
You can update a supported entity with the `update()` method in the resource. It accepts the `id` of the entity to update and the corresponding `UpdateOperation` e.g. `UpdateProduct`. The updated entity is returned.
``` python
from paddle_billing                        import Client
from paddle_billing.Resources.Products.Operations import UpdateProduct

paddle = Client('PADDLE_API_SECRET_KEY')

# Update the name of the product
updated_product = paddle.products.update('PRODUCT_ID', UpdateProduct(
    name = 'My Improved Product'
))
```

Where operations require more than one `id`, the `update()` method accepts multiple arguments. For example, to update an address for a customer, pass the `customerId` and the `addressId`:
``` python
updated_address = paddle.addresses.update(
    'CUSTOMER_ID',
    'ADDRESS_ID',
    operation_goes_here,
)
```

### Delete an entity
You can delete an entity with the `delete()` method in the resource. It accepts the `id` of the entity to delete. The deleted entity is returned.
``` python
from paddle_billing import Client

paddle = Client('PADDLE_API_SECRET_KEY')

deleted_product = paddle.products.delete('PRODUCT_ID')
```


## Resources

### Webhook signature verification
The SDK includes a helper class to verify webhook signatures sent by Notifications from Paddle.

``` python
from paddle_billing.Notifications import Secret, Verifier

integrity_check = Verifier().verify(request, Secret('WEBHOOK_SECRET_KEY'))
```

## Learn more
- [Paddle API reference](https://developer.paddle.com/api-reference/overview?utm_source=dx&utm_medium=paddle-python-sdk)
- [Sign up for Paddle Billing](https://login.paddle.com/signup?utm_source=dx&utm_medium=paddle-python-sdk)
