from main import *
import pytest

def test_sample():
    assert generate_word() == "SOURCE"
    
def test_no_match():
    assert wordle("PLANTY") == "------"