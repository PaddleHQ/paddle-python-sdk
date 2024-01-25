[![Build Status](https://img.shields.io/github/actions/workflow/status/Invincibear/paddle-billing-python-sdk/publish_to_pypi.yml)](https://github.com/Invincibear/paddle-billing-python-sdk/actions/?query=branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/paddle-billing-python-sdk.svg)](https://pypi.python.org/pypi/paddle-billing-python-sdk)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/paddle-billing-python-sdk.svg)](https://pypi.python.org/pypi/paddle-billing-python-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



# paddle-billing-python-sdk
A *limited* Python wrapper for the new Paddle Billing SDK

This project only contains the Paddle Billing components needed to satisfy another project of mine. Please feel free to contribute missing components. I may or may not add additional components myself over time, no promises. I am always open to PRs for bug fixes or new features.


### Core developers
- [Invincibear](https://github.com/Invincibear)



## Table of contents
- [Requirements](#Requirements)
- [Install](#Install)
- [Usage](#Usage)
- [Examples](#Examples)

## Requirements
Python 3.11 and later.

**Project dependencies** (automatically installed by pip):
- requests>=2.31
- urllib3>=2.1.0


## Install
Because `paddle-billing-python-sdk` is [available on PyPi](https://pypi.org/project/paddle-billing-python-sdk/), installation is as simple as running the following `pip` command: 

`pip install paddle-billing-python-sdk`



## Usage
To authenticate, you'll need an API key. You can create and manage API keys in **Paddle > Developer tools > Authentication**.

Pass your API key while initializing a new Paddle client:
``` python
from paddle-billing-python-sdk.Client import Client

paddle = Client('PADDLE_API_SECRET_KEY')
```

You can pass your Paddle API secret key into the SDK from an environment variable:
``` python
from os import environ
from paddle-billing-python-sdk.Client import Client

paddle = Client(environ.get('PADDLE_API_SECRET_KEY'))
```

You can also pass an environment to work with Paddle's sandbox:
``` python
from paddle-billing-python-sdk.Client      import Client
from paddle-billing-python-sdk.Options     import Options
from paddle-billing-python-sdk.Environment import Environment

paddle = Client(
    api_key = 'PADDLE_API_SECRET_KEY',
    options = Options(Environment.SANDBOX),
)
```

Keep in mind that API keys are separate for your sandbox and live accounts, so you'll need to generate keys for each environment.



## Examples
There are examples included in the [examples folder]()

### List entities
You can list supported entities with the `list` function in the resource. It returns an iterator to help when working with multiple pages.
``` python
from paddle-billing-python-sdk.Client import Client

paddle = Client('PADDLE_API_SECRET_KEY')

products = paddle.products.list()

# List returns an iterable, so pagination is handled automatically.
for product in products:
    print(f"Product's id: {product.id}")
```

### Get an entity
You can get an entity with the `get` function in the resource. It accepts the `id` of the entity to get. The entity is returned.
``` python
from paddle-billing-python-sdk.Client import Client

paddle = Client('PADDLE_API_SECRET_KEY')

product = paddle.products.get('PRODUCT_ID')
```

### Create an entity
You can create a supported entity with the `create` function in the resource. It accepts the resource's corresponding `CreateOperation`. The created entity is returned.

``` python
from paddle-billing-python-sdk.Client                                      import Client
from paddle-billing-python-sdk.Entities.Shared.TaxCategory                 import TaxCategory
from paddle-billing-python-sdk.Resources.Products.Operations.CreateProduct import CreateProduct

paddle = Client('PADDLE_API_SECRET_KEY')

product = paddle.products.create(
    CreateProduct(
        name         = 'My Product,
        tax_category = TaxCategory.Standard,
    )
)
```

### Update an entity
You can update a supported entity with the `update` function in the resource. It accepts the `id` of the entity to update and the corresponding `UpdateOperation`. The updated entity is returned.
``` python
from paddle-billing-python-sdk.Client                                      import Client
from paddle-billing-python-sdk.Resources.Products.Operations.UpdateProduct import UpdateProduct

paddle = Client('PADDLE_API_SECRET_KEY')

# Update the name of the product
product = paddle.products.update('PRODUCT_ID', UpdateProduct(
    name = 'My Improved Product'
))
```

Where operations require more than one `id`, the `update` function accepts multiple arguments. For example, to update an address for a customer, pass the `customerId` and the `addressId`:
# TODO
# TODO
# TODO
``` python
address = paddle.products.update(
    'CUSTOMER_ID',
    'ADDRESS_ID',
    $update_operation,
)
```

# TODO
# TODO
# TODO
### Delete an entity
You can delete an entity with the `delete` function in the resource. It accepts the `id` of the entity to delete. ??? is returned.
``` python
from paddle-billing-python-sdk.Client import Client

paddle = Client('PADDLE_API_SECRET_KEY')

product = paddle.products.delete('PRODUCT_ID')
```
