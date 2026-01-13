
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
    
    guessResultsOutput = []
    
    for position, guessedWord in enumerate(guesses):
    
        guessResult = ""

        if position > 5:
            guessResultsOutput.append("Number of guesses exceeded, you did not guess the word.")
            break
        
        for index, letter in enumerate(guessedWord):
                if (index, letter) in enumerate(wordToGuess):
                    guessResult += 'G'
                elif letter in wordToGuess:
                    guessResult += 'Y'
                else:
                    guessResult += '-'
                    
        guessResultsOutput.append(guessResult)
        
        if guessResultsOutput[-1] == "GGGGGG":
            guessResultsOutput.append(f"The word was SOURCE, you guessed it in {len(guessResultsOutput)} guesses.")
            break

    return guessResultsOutput
        
print(wordle(["PLANTY", "XXOXXX", "SXXXXX", "SSSSSS", "SOURCE", "PASTAS", "EXCEED"]))