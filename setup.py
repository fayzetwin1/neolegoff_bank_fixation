from io import open
from setuptools import setup, find_packages 


def read(filename):
    with open(filename, encoding="utf-8") as file:
        return file.read()


def requirements():
    with open("requirements.txt", "r") as req:
        return [r for r in req.read().split("\n") if r]


setup(
    name="neolegoff_bank_fixation",
    version="0.1.0-fork", 
    
    packages=find_packages(),
    
    url="https://github.com/WhiteApfel/neolegoff_bank",
    license="Mozilla Public License 2.0",
    author="WhiteApfel, fayzetwin",
    author_email="white@pfel.ru",
    description="Simple Tinkoff Bank API client",
    install_requires=requirements(),
    project_urls={
        "Source code": "https://github.com/WhiteApfel/neolegoff_bank",
        "Write me": "https://t.me/whiteapfel",
    },
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    keywords="tinkoff api bank",
)
