import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__title__ = "flask-boilerplate"
__description__ = "Boilerplate for Flask API"
__url__ = "https://github.com/openboilerplates/flask-boilerplate"
__version__ = "1.0.3"
__author__ = "Fakabbir Amin"
__author_email__ = "fakabbir@gmail.com"
__license__ = "MIT License"

setuptools.setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    url=__url__,
    packages=setuptools.find_packages(),
    classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
    ],
    python_requires='>=3.6',
)
