#!/usr/bin/env python

__version__ =  "0.1.0"
__author__ = "Arjan de Haan"

import argparse

from pathlib import Path

from typing import Iterator, List, Tuple
from jinja2 import Environment, FileSystemLoader


class ByteData:
    def __init__(self, value: int, index: int):
        self.value = value
        self.index = index

    def is_char(self) -> bool:
        return 31 < self.value < 128

    def index_hex(self) -> str:
        return padded_hex(self.index, 8)

    def chr(self) -> str:
        return chr(self.value)

    def hex(self) -> str:
        return padded_hex(self.value, 2)


def byte_reader(path: str) -> Iterator[str]:
    with open(path, "rb") as reader:
        b = reader.read(1)
        while b:
            yield b
            b = reader.read(1)


def padded_hex(x: int, length: int) -> str:
    return "{0:0{1}x}".format(x, length).upper()


def to_hex(x: int) -> str:
    return "{0:0x}".format(x).upper()


def read_all(path: str) -> str:
    with open(path, "r") as reader:
        return reader.read()


def read_binary(path: str, offset=0, length=0) -> List[ByteData]:
    read_bytes = []
    for index, read_byte in enumerate(byte_reader(path)):
        if offset > index:
            continue
        elif length > 0 and index - offset > length:
            break

        read_int = int.from_bytes(read_byte, byteorder="big")
        read_bytes.append(ByteData(read_int, index))
    return read_bytes


def render_template(
    env: Environment,
    byte_list: List[ByteData],
    title: str = "",
    style: str = "",
    script: str = "",
) -> str:
    address_count = len(byte_list) // 16 + 1
    template = env.get_template("base.html")

    configuration = {
        "address_count": address_count,
        "byte_list": byte_list,
        "title": title,
        "style": style,
        "script": script,
    }

    return template.render(**configuration)


def parse_args() -> Tuple:
    parser = argparse.ArgumentParser(description="Visual hexdumper")
    parser.add_argument(
        "-O", "--offset", type=int, help="Offset in bytes from the top", default=0
    )
    parser.add_argument(
        "-r", "--read", type=int, help="Amount of bytes to read", default=0
    )
    parser.add_argument(
        "-o", "--output", type=Path, default="./report.html"
    )
    parser.add_argument("source_file", type=Path)
    return parser.parse_args()


def main():
    current_location = Path(__file__).parent
    script_path = Path(current_location, "templates/script.js").absolute()
    style_path = Path(current_location, "templates/style.css").absolute()
    template_path = Path(current_location, "templates").absolute()

    env = Environment(loader=FileSystemLoader(template_path))
    env.globals.update(padded_hex=padded_hex)

    args = parse_args()
    source_path = args.source_file

    # Load external script & styling.
    script = f"<script>{read_all(script_path)}</script>"
    style = f"<style>{read_all(style_path)}</style>"

    print('Reading binary...')
    read_bytes = read_binary(source_path, offset=args.offset, length=args.read)
    print('Rendering template...')
    output = render_template(
        env, read_bytes, title=source_path, style=style, script=script
    )
    print(f'Writing to {args.output}...')
    with open(args.output, "w") as writer:
        writer.write(output)

    print('Done.')


if __name__ == "__main__":
    main()
