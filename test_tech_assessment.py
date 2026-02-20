import pytest
from tech_assessnent import palindrome_check, list_palindrome, word_information


def test_palindrome_false():
    assert (palindrome_check("hello") is False)


def test_palindrome_true():
    assert (palindrome_check("racecar") is True)


def test_palindrome_case():
    assert (palindrome_check("RaCecAr") is True)


def test_palindrome_characters():
    assert (palindrome_check("!RaCe$cAr") is True)


def test_palindrome_not_characters():
    assert (palindrome_check("Hell$o") is False)


def test_palindrome_space_characters():
    assert (palindrome_check("racec ar") is False)


def test_palindrome_list():
    assert (list_palindrome(["racecar", "hello", "kayak"]) == [
            "racecar", "kayak"])


def test_palindrome_list_empty():
    assert (list_palindrome(["hello", "there", "world"]) == [])


def test_word_not_valid():
    with pytest.raises:
        word_information("asdkljhaskd")
