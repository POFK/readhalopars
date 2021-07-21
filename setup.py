import os
import sys

from setuptools import setup, find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")

setup(
    name="rhp",
    version="0.1",
    author="Tianxiang Mao",
    author_email="mtianxiang@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    packages=find_packages(),
    include_dirs=["./rhp"],
    cffi_modules=["./rhp/rhp_extension_build.py:ffibuilder"],
)
