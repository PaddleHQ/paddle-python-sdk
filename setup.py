from setuptools  import setup, find_packages

from paddle_billing_python_sdk.__VERSION__ import __VERSION__


setup(
    name='paddle-billing-python-sdk',
    version=__VERSION__,
    author='Corey Regan',
    author_email='regan.corey@gmail.com',
    description='A Python wrapper for the Paddle Billing API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/invincibear/paddle-billing-python-sdk',
    packages=find_packages(),
    install_requires=[
        'requests>=2.31',
        'urllib3>=2.1.0',
    ],
    classifiers=[
        # Full list: https://pypi.org/classifiers/
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.11',
    extras_require={
        'dev': [
            'pytest~=7.4.4',
            'pytest-cov~=4.1.0'
            'pylint>=3.0.3',
            'setuptools>=69.0.3',
        ],
    },
)
