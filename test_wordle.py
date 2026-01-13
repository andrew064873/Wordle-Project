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
    
def test_correct_word():
    assert wordle("SOURCE") == "GGGGGG"
    
def test_multiple_correct_letters():
    assert wordle("SSSSSS") == "GYYYYY"
    
def test_multiple_guesses():
    assert wordle(["PLANTY", "XXOXXX", "SXXXXX", "SSSSSS", "SAUCES"]) == ["------", "--Y---", "G-----", "GYYYYY", "G-GYYY"]
    
def test_exceed_max_guesses_incorrect():
    assert wordle(["PLANTY", "XXOXXX", "SXXXXX", "SSSSSS", "SAUCES", "PASTAS", "EXCEED"]) == ["------", "--Y---", "G-----", "GYYYYY", "G-GYYY", "--Y--Y", "Number of guesses exceeded, you did not guess the word."]
    
def test_word_guessed():
    assert wordle(["PLANTY", "XXOXXX", "SXXXXX", "SOURCE"]) == ["------", "--Y---", "G-----", "GGGGGG", "The word was SOURCE, you guessed it in 4 guesses."]
    
def test_terminate_game_after_word_guessed():
    assert wordle(["PLANTY", "XXOXXX", "SXXXXX", "SSSSSS", "SOURCE", "PASTAS", "EXCEED"]) == ["------", "--Y---", "G-----", "GYYYYY", "GGGGGG", "The word was SOURCE, you guessed it in 5 guesses."]