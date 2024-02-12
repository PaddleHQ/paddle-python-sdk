[![Build Status](https://img.shields.io/github/actions/workflow/status/Invincibear/paddle-billing-python-sdk/publish_to_pypi.yml)](https://github.com/Invincibear/paddle-billing-python-sdk/actions/?query=branch%3Amain)
[![PyPI](https://img.shields.io/pypi/v/paddle-billing-python-sdk.svg)](https://pypi.python.org/pypi/paddle-billing-python-sdk)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/paddle-billing-python-sdk.svg)](https://pypi.python.org/pypi/paddle-billing-python-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



# paddle-billing-python-sdk
A Python wrapper for the new Paddle Billing SDK, based on Paddle's official [paddle-php-sdk](https://github.com/PaddleHQ/paddle-php-sdk/)


### Core developers
- [Invincibear](https://github.com/Invincibear)



## Table of contents
- [Requirements](#Requirements)
- [Install](#Install)
- [Usage](#Usage)
- [Examples](#Examples)

## Requirements
Python>=3.11 (for native type hinting, StrEnum, trailing commas, f-strings)

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
from paddle_billing.Client import Client

paddle = Client('PADDLE_API_SECRET_KEY')
```

You can pass your Paddle API secret key into the SDK from an environment variable:
``` python
from os                    import environ
from paddle_billing.Client import Client

paddle = Client(environ.get('PADDLE_API_SECRET_KEY'))
```

You can also pass an environment to work with Paddle's sandbox:
``` python
from paddle_billing.Client      import Client
from paddle_billing.Options     import Options
from paddle_billing.Environment import Environment

paddle = Client('PADDLE_API_SECRET_KEY', options=Options(Environment.SANDBOX))
```

Keep in mind that API keys are separate for your sandbox and live accounts, so you'll need to generate keys for each environment.



## Examples
There are examples included in the [examples folder](https://github.com/Invincibear/paddle-billing-python-sdk/tree/main/examples). To prevent leaking errors to your clients we recommend encapsulating Paddle operations inside Try/Except blocks. For brevity, the below examples do not do this.

### List entities
You can list supported entities with the `list()` method in the resource. It returns an iterator to help when working with multiple pages.
``` python
from paddle_billing.Client import Client

paddle = Client('PADDLE_API_SECRET_KEY')

products = paddle.products.list()

# List() returns an iterable, so pagination is automatically handled
for product in products:
    print(f"Product's id: {product.id}")
```

And a more production-friendly version of the same code, although you'd want to use your own logger instead of `print()`. Note the encapsulation of Paddle queries inside `try`/`except` blocks.
``` python
from logging               import getLogger
from paddle_billing.Client import Client
from sys                   import exit  # You should use classes/functions that return instead of exit

log    = getLogger('my_app')
paddle = Client('PADDLE_API_SECRET_KEY', options=Options(Environment.SANDBOX), logger=log)

products = None
try:
    products = paddle.products.list()
except (ApiError, MalformedResponse) as error:
    log.error(error)
    # Your additional logic that can handle Paddle's hints about what went wrong
except Exception as error:
    log.error(f"We received an unknown error listing products: {error}")

if not products:
    print("There was a problem trying to list products")
    exit(1)

if not len(products):
    log.warn("There are no products to list, try creating one using the example below")
    print("There are no products to list")
    exit

for product in products:
    print(f"Product's id: {product.id}")
    # Your additional logic for using each product
```

### Get an entity
You can get an entity with the `get()` method in the resource. It accepts the `id` of the entity to get. The entity is returned.
``` python
from paddle_billing.Client import Client

paddle = Client('PADDLE_API_SECRET_KEY')

product = paddle.products.get('PRODUCT_ID')
```

### Create an entity
You can create a supported entity with the `create()` method in the resource. It accepts the resource's corresponding `CreateOperation` e.g. `CreateProduct`. The created entity is returned.

``` python
from paddle_billing.Client                        import Client
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
from paddle_billing.Client                        import Client
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
from paddle_billing.Client import Client

paddle = Client('PADDLE_API_SECRET_KEY')

deleted_product = paddle.products.delete('PRODUCT_ID')
```


## Resources

### Webhook signature verification
The SDK includes a helper class to verify webhook signatures sent by Notifications from Paddle.

``` python
from paddle_billing.Notifications import Secret, Verifier

integrity_check = Verifier().verify(request, Secret('WEBHOOK_SECRET_KEY')
```

## Learn more
- [Paddle API reference](https://developer.paddle.com/api-reference/overview?utm_source=dx&utm_medium=paddle-billing-python-sdk)
- [Sign up for Paddle Billing](https://login.paddle.com/signup?utm_source=dx&utm_medium=paddle-billing-python-sdk)
