from exercises.character_count import character_count


def test_character_count():
    assert character_count('') == {}
    assert character_count('abc') == {"a": 1, "b": 1, "c": 1}
    assert character_count('abbcccc') == {"a": 1, "b": 2, "c": 4}
    assert character_count('abbccccd') == {'d': 1, "a": 1, "b": 2, "c": 4}
