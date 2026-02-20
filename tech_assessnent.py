import requests


def palindrome_check(string: str) -> bool:
    string = string.lower()
    punctuation = ["@", "!", "#", ";", ":", "!", "?", "$"]
    new_string = ""
    for letter in string:
        if letter not in punctuation:
            new_string += letter

    for i in range(len(new_string)//2):
        if new_string[i] != new_string[-i-1]:
            return False
    return True


def list_palindrome(palindromes: list[str]) -> list[str]:
    are_palindromes = []
    for word in palindromes:
        if palindrome_check(word):
            are_palindromes.append(word)
    return are_palindromes


def word_information(word: str) -> dict:
    pass
