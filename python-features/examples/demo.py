from pathlib import Path
import sys


def total_line_count(paths):
    line_count = 0
    for path in paths:
        try:
            line_count += len(Path(path).read_text().splitlines())
        except Exception as e:
            breakpoint()
    return line_count


if __name__ == '__main__':
    total_line_count(paths='.')
