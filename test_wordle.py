from main import *
import pytest

def test_sample():
    assert generate_word() == "SOURCE"
    
def test_no_match():
    assert wordle("PLANTY") == "------"
    
def test_match_no_correct_placement():
    assert wordle("XXOXXX") == "--Y---"
    
def test_match_one_correct_placement():
    assert wordle("SXXXXX") == "G-----"
    
def test_correct_guess():
    assert wordle("SOURCE") == "GGGGGG"
    
def test_multiple_correct_letters():
    assert wordle("SSSSSS") == "GYYYYY"