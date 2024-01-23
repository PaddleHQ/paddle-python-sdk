from __version__    import __version__
from setuptools     import setup, find_packages


setup(
    name='paddle-billing-python-sdk',
    version=__version__,
    author='Corey Regan',
    author_email='regan.corey@gmail.com',
    description='A Python wrapper for the Paddle Billing API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/invincibear/paddle-billing-python-sdk',
    packages=find_packages(),
    install_requires=[
        'requests>=2.31',
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
            'pytest>=7.0.0',
            'setuptools>=69.0.3',
        ],
    },
)
