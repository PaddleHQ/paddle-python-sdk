from setuptools  import setup, find_packages


setup(
    version          = '0.0.1a102',

    author           = 'Corey Regan',
    author_email     = 'regan.corey@gmail.com',
    description      = 'A Python wrapper for the Paddle Billing API',
    name             = 'paddle-billing-python-sdk',
    packages         = find_packages(),
    python_requires  = '>=3.11',
    url              = 'https://github.com/invincibear/paddle-billing-python-sdk',

    long_description              = open('README.md').read(),
    long_description_content_type = 'text/markdown',

    classifiers = [
        # Full list: https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    extras_require = {
        'dev': [
            'pytest~=7.4.4',
            'pytest-cov~=4.1.0',
            'requests-mock~=1.11.0',
            'setuptools>=69.0.3',
        ],
    },
    install_requires = [
        'requests>=2.31',
        'urllib3>=2.1.0',
    ],
)
