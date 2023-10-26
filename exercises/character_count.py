from typing import Dict


def character_count(s: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for item in s:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    return counts