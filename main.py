
def generate_word():
    return "SOURCE"

def wordle(guessedWord):
    wordToGuess = generate_word()
    
    guessResult = ""
    
    for index, letter in enumerate(guessedWord):
            if (index, letter) in enumerate(wordToGuess):
                guessResult += "G"
            elif letter in wordToGuess:
                guessResult += "Y"
            else:
                guessResult += "-"

    return guessResult
        
print(wordle("PLANT"))