#!/usr/bin/env python

from pathlib import Path
from typing import List
from setuptools import setup, find_packages

CURRENT_DIR = Path(__file__).parent


def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()


def get_long_description() -> str:
    return (CURRENT_DIR / "README.md").read_text(encoding="utf8")


setup(
    name="HTMLHexViewer",
    version="0.1.2",
    description="Create simple hexdumps from any file",
    long_description_content_type='text/markdown',
    long_description=get_long_description(),
    author="Arjan de Haan",
    author_email="agdehaan@gmail.com",
    url="https://github.com/Vepnar/HTMLHexViewer",
    license="GPL-3",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.6.2",
    install_requires=get_requirements(),
    entry_points={
        "console_scripts": [
            "htmlhexviewer=htmlhexviewer:main",
        ]
    },
    package_data={'htmlhexviewer': ['templates/*']},
)
