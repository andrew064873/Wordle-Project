
def generate_word():
    return "SOURCE"

def single_wordle_guess(wordToGuess, guessedWord):
    guessResult = ""
            
    for index, letter in enumerate(guessedWord):
            if (index, letter) in enumerate(wordToGuess):
                guessResult += 'G'
            elif letter in wordToGuess:
                guessResult += 'Y'
            else:
                guessResult += '-'
                    
    return guessResult

def wordle(guesses):
    
    wordToGuess = generate_word()
    
    if type(guesses) == str:
        return single_wordle_guess(wordToGuess, guesses)
    
    guessResults = []
    
    for guessedWord in guesses:
    
        guessResult = ""
        
        for index, letter in enumerate(guessedWord):
                if (index, letter) in enumerate(wordToGuess):
                    guessResult += 'G'
                elif letter in wordToGuess:
                    guessResult += 'Y'
                else:
                    guessResult += '-'
                    
        guessResults.append(guessResult)

    return guessResults
        
print(wordle("PANTSY"))