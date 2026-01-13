import random

def generateWord():
    return "SOURCE"

def getWord():
    with open('6-letter Words.txt') as word_dictionary:
        word_list = word_dictionary.read().upper().split(", ")
        
    return word_list[random.randint(0, len(word_list) - 1)]

def playWordle():
        
    word_to_guess = getWord()
    guess_results_output = []
    guesses = []
    
    print("A word has been chosen. Begin your guesses for the 6-letter word.")
    
    while True:
        if len(guess_results_output) > 5:
            print(f"Number of guesses exceeded, you did not guess the word, {word_to_guess}.")
            break
        
        print(f"Guess {len(guesses) + 1}")
        guesses.append(input().upper())
        
        guess_results_output.append(singleWordleGuess(word_to_guess, guesses[-1]))
        
        print(guess_results_output[-1])
        
        if guess_results_output[-1] == "GGGGGG":
            print(f"The word was {word_to_guess}, you guessed it in {len(guess_results_output)} guess" + ("es." if len(guess_results_output) > 1 else "."))
            break
        
def singleWordleGuess(word_to_guess, guessed_word):
    guess_result = ""
            
    for index, letter in enumerate(guessed_word):
            if (index, letter) in enumerate(word_to_guess):
                guess_result += 'G'
            elif letter in word_to_guess:
                guess_result += 'Y'
            else:
                guess_result += '-'
                    
    return guess_result

def wordle(guesses):
    
    word_to_guess = generateWord()
    
    if type(guesses) == str:
        return singleWordleGuess(word_to_guess, guesses)
    
    guess_results_output = []
    
    for position, guessed_word in enumerate(guesses):
    
        guess_result = ""

        if position > 5:
            guess_results_output.append("Number of guesses exceeded, you did not guess the word.")
            break
        
        for index, letter in enumerate(guessed_word):
                if (index, letter) in enumerate(word_to_guess):
                    guess_result += 'G'
                elif letter in word_to_guess:
                    guess_result += 'Y'
                else:
                    guess_result += '-'
                    
        guess_results_output.append(guess_result)
        
        if guess_results_output[-1] == "GGGGGG":
            guess_results_output.append(f"The word was SOURCE, you guessed it in {len(guess_results_output)} guesses.")
            break

    return guess_results_output

if __name__ == "__main__":
    playWordle()
