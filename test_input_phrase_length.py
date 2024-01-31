import pytest

def test_input_phrase_length():
    phrase = input("Set a phrase: ")
    assert len(phrase) < 15, "The phrase should be less than 15 characters"


