#!/usr/bin/env python

from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="fino",
    version="0.7.0",
    description="Output the Finnish word for a given integer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hugovk/fino",
    author="hugovk",
    keywords=["Finnish", "suomi", "numbers", "integers"],
    py_modules=("fino",),
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 6 - Mature",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Natural Language :: Finnish",
        "Topic :: Artistic Software",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)

# End of file
