from setuptools import setup, find_packages

setup(
    name='paddle-billing-python-sdk',
    version='0.0.1',  # Update this for new versions
    author='Corey Regan',
    author_email='regan.corey@gmail.com',
    description='A Python wrapper for the Paddle Billing API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # If your README is in markdown
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
    python_requires='>=3.11',  # Minimum version requirement of the package
    extras_require={
        'dev': [
            'click>=8.0.0',
            'pytest>=7.0.0',
            'requests>=2.31',
            'setuptools>=69.0.3',
            'twine>=4.0.2',
            'wheel>=0.42.0',
        ],
    },
)
