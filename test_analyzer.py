import pytest 
from analyzer import count_chars, count_words

def test_count_chars():
    assert count_chars("hi") == 2
    assert count_chars("world") == 5
    assert count_chars("fantastic") == 9
    assert count_chars("") == 0
        
def test_count_words():
    assert count_words("hello world") == 2
    assert count_words("this is a test") == 4
    assert count_words("Is this really working for real?") == 6
    assert count_words("") == 0