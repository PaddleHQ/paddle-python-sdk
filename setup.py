from setuptools import setup, find_packages


setup(
    version         = '0.1.3',

    author          = 'Paddle and contributors',
    author_email    = 'team-dx@paddle.com',
    description     = "Paddle's Python SDK for Paddle Billing",
    keywords        = ['paddle', 'sdk', 'python'],
    license         = 'Apache-2.0',
    name            = 'paddle-python-sdk',
    packages        = find_packages(),
    python_requires = '>=3.11',
    url             = 'https://developer.paddle.com/api-reference/overview',

    long_description              = open('README.md').read(),
    long_description_content_type = 'text/markdown',

    classifiers = [
        # Full list: https://pypi.org/classifiers/
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    extras_require = {
        'dev': [
            'pytest>=7.4.4,<8.1.0',
            'pytest-cov~=4.1.0',
            'requests-mock~=1.11.0',
            'setuptools>=69.0.3',
        ],
    },
    install_requires = [
        'requests>=2.31',
        'urllib3>=1.26.18',
    ],
)
