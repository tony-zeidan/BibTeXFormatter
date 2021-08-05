import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="bibtexformatter",
    version="1.0.0",
    description="A simple Python script/package for the formatting of bibtex files.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="Tony Abou Zeidan",
    author_email="tony.azp25@gmail.com",
    license="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9.4"
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'formatter = bibtexformatter.formatter'
        ]
    },
    install_requires=["bibtexparser"]
)
