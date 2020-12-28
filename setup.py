from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="benerator_cumberpy",
    version="0.2.3",
    description="A Ben Cumberbatch-like name generator",
    long_description=long_description,
    url="https://github.com/fdmarcin/benerator-cumberpy",
    download_url="https://github.com/fdmarcin/benerator-cumberpy/archive/0.2.3.tar.gz",
    author="Marcin Sędłak-Jakubowski",
    author_email="fdmarcin@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="benedict cumberbatch word generator",
    py_modules=["benerator_cumberpy"],
    entry_points={
        "console_scripts": [
            "hello-ben = benerator_cumberpy:hello",
            "benerate = benerator_cumberpy:benerate_name",
        ]
    },
    include_package_data=True,
    packages=find_packages("src"),  # include all packages under src
    package_dir={"": "src"},
    package_data={"": ["data/*.txt"],},
)
