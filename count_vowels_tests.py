import pytest
from main import count_vowels

@pytest.mark.parametrize("test_input, expected", [
    ("aeiou", 5),  # Только гласные
    ("bcdfg", 0),  # Нет гласных
    ("Hello World", 3),  # Смешанный регистр
    ("PyThOn", 2),  # Разный регистр букв
    ("", 0),  # Пустая строка
    ("AEIOUaeiouyY", 12),  # Все гласные в разном регистре
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected
