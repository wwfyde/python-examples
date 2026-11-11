def inc(i: int) -> int:
    return i + 1


def test_inc():
    assert inc(3) == 4
    assert inc(5) == 6
    assert inc(6) == 7
    assert inc(0) == 1
