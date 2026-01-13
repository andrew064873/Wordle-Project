import random

def generateWord():
    """
        Generate test word of "SOURCE" for initial assertion tests.
        
        Returns: 
            "SOURCE" (str): set value to be used for testing
    """
    return "SOURCE"

def getWord():
    """
        This function retreives list of 6-letter words from '6-letter Words.txt' document and
        returns one at random.

        Returns: 
            word_list[random.randint(0, len(word_list) - 1)] (str): pulled random value from word_dictionary
    """
    with open('6-letter Words.txt') as word_dictionary:
        word_list = word_dictionary.read().upper().split(", ")
    word_dictionary.close()
        
    return word_list[random.randint(0, len(word_list) - 1)]

def playWordle():
    """
        This function allows for the wordle game to be played through main file, using user input, 
        singleWordleGuess def, and printing to terminal.
    """
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
    """
        This function allows for the output of a single guess passed in with the word to be guessed and
        outputs the formatted string result from the guess.

        Args:
            guessed_word (str): the word entered to be compared to the word to be guessed
            word_to_guess (str): the word to be guessed
            
        Returns:
            guess_result (str): the formatted string result generated from the guess
    """
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
    """
        This function simulates the wordle game when passed in a list of guesses.

        Args:
            guesses (list[str]): list of str values to be compared
            guesses (str): passed in variable can be in the form of a str
            
        Returns:
            singleWordleGuess(word_to_guess, guesses) (str): str response of single word passed in
            guess_results_output (list[str]): list of str values of guesses when compared to word_to_guess
    """
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
