import random

def generate_word():
    return "SOURCE"

def getWord():
    with open('6-letter Words.txt') as wordDictionary:
        wordList = wordDictionary.read().upper().split(", ")
        
    return wordList[random.randint(0, len(wordList) - 1)]

def play_wordle():
    
    gameOn = True
    
    wordToGuess = getWord()
    guessResultsOutput = []
    guesses = []
    
    print(f"A word has been chosen. Begin your guesses for the 6-letter word. {wordToGuess}")
    
    while gameOn:
        if len(guessResultsOutput) > 5:
            print(f"Number of guesses exceeded, you did not guess the word, {wordToGuess}.")
            break
        
        print(f"Guess {len(guesses) + 1}")
        guesses.append(input().upper())
        
        guessResultsOutput.append(single_wordle_guess(wordToGuess, guesses[-1]))
        
        print(guessResultsOutput[-1])
        
        if guessResultsOutput[-1] == "GGGGGG":
            print(f"The word was {wordToGuess}, you guessed it in {len(guessResultsOutput)} guess" + ("es." if len(guessResultsOutput) > 1 else "."))
            break
        
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

if __name__ == "__main__":
    play_wordle()
