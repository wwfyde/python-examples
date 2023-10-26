"""
convert .md file to a json

# TODO markdown parse
"""
from typing import Dict

from pydantic import FilePath


def read_file(f: FilePath, mode: str = 'r') -> Dict[str, str]:
    terms = dict()
    with open(f, mode) as f:

        lines = f.readlines()
        line: str

        for line in lines:
            print(line)
            if line.strip().startswith("# "):

                terms[line.strip()[2:]] = ''

            elif line.strip().startswith("## "):
                terms[line.strip()[3:]] = ''

    return terms


if __name__ == '__main__':
    print(read_file('计算机专业术语对照.md'))



