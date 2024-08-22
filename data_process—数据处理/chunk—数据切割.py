from typing import Any


def chunk_data(chunk_size: int) -> list[list[Any]]:
    data: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] * 7700
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    return chunks


if __name__ == "__main__":
    result = chunk_data(501)
    print(len(result))
    print(f"the last chunk size:{len(result[-1])}")
