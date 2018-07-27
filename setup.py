#!/usr/bin/env python

from setuptools import setup

setup(
    name="fino",
    version="0.3.0",
    description="Output the Finnish word for a given integer.",
    url="https://github.com/hugovk/fino",
    author="hugovk",
    keywords=["Finnish", "suomi", "numbers", "integers"],
    py_modules=("fino",),
    zip_safe=False,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    classifiers=[
        "Development Status :: 6 - Mature",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
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
