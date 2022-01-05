<h1 align="center"> HTMLHexViewer </h1>

<p align="center">
<a href="https://pypi.org/project/HTMLHexViewer/"><img alt="PyPI" src="https://img.shields.io/pypi/v/htmlhexviewer"/></a>
<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"/>
<img alt="GitHub" src="https://img.shields.io/github/license/Vepnar/HTMLHexViewer"/>
</p>

> Hexdump but easier to read.

HTMLHexViewer is exactly what its name suggests, A HTML Hex Viewer inspired by the CLI tool [hexdump](https://en.wikipedia.org/wiki/Hex_dump). While still retaining almost all core functionalities of hex dump. HTMLHexViewer makes it possible to create stand-alone reports of the binary you're investigating.

## Installation

HTMLHexViewer can be installed using [pip](https://pypi.org/project/pip/). with the simple command `pip install htmlhexviewer`. If you prefer a more cutting edge version you could also install it with the following command: `pip install git+git://github.com/Vepnar/HtmlHexViewer.git`

## Usage

To convert an entire file into an HTML report execute.

```htmlhexviewer {target_binary}```

You could also run *HTMLHexViewer* as a package if the previous command didn't work.

```python -m htmlhexviewer {target_binary}```

It's recommended to set a max length of processed byte sequence with the parameter `-r [bytes to process]` and the offset with `-O [offset]`. The browser can't efficiently render many thousands of elements.

```htmlhexviewer -r 1000 -O 0 /usr/bin/bash```

The peformance drop on even small applications is significant. Thus these flags are a must.

## Example of usage & screenshots
[Image](images/one.png)
[YouTube Video](https://youtu.be/wlghJ6R6D_g)

## Credits
- [Black](https://github.com/psf/black). This markdown page has been inspired by them.
- Hexdump. This application is a remake of hexdump but more visual.
