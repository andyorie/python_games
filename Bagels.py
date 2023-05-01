''' Bagels, by Al Sweigart (al&inventwithpython.com)
A deductive logic game where you must guess a number based on clues.
 '''

import random

NUM_DIGITS = 3 
MAX_GUESSES = 10


def main():
    print('''Bagels, by Al Sweigart (al&inventwithpython.com). 
       A deductive logic game where you must guess a number based on clues. 
       I am thinking of a {} - digit number with no repeating digits.
       Try to guess what it is. Here are some clues:
    When I say:    That means:
    Pico           One digit is correct but in the wrong position.
    Fermi          One digit is correct and in the right position.
    Bagels         No digit is correct.
       
    For example, if the secret number was 248 and your guess was 843, the clues would be Fermi Pico.
       '''.format(NUM_DIGITS))
 
 
    while True: # Main loop
        # This stores the secret number the player needs to guess.
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        # Randomly select a string to give to the player if they win
        winner_list = ["Great job!", "Winner!", "Superb!", "You won!", "Nice!"]
        winner_prompt = random.choice(winner_list)

        numGuesses = 1 # set a variable to count the number of guesses made by the player
        while numGuesses <= MAX_GUESSES:
            guess = "" # empty string to save the player guess
            
            # Keep looping until a valid guess.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")

            if guess == secretNum:
                print(winner_prompt)
                break # The player guessed correct so break out of this loop
              
            clues = getClues(guess, secretNum) # give a list of clues based on the player response
            print(clues)
            numGuesses += 1 # increases the count for the number of guesses made by the player

            if numGuesses > MAX_GUESSES:
                print("Nice try but you ran out of guesses")
                print("The answer was {}.".format(secretNum))
                break


        # Ask player if they want to play again.
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith('y'):
            break
    print("Thanks for playing!")


def getSecretNum():
    ''' Returns a string made up of NUM_DIGITS unique random digits.'''
    numbers = list('0123456789') # creates a list of digits 0 to 9.
    random.shuffle(numbers) # shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number: 
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    '''Returns a string with the Pico, Fermi, Bagels clues for a guess \
    and secret number pair.'''
    if guess != secretNum:
        clues = [ ]

        for i in range(len(guess)): # this loop adds strings to the clues list.
            if guess[i] == secretNum[i]:
                # A correct digit is in the correct place.
                clues.append('Fermi')
            elif guess[i] in secretNum:
                # A correct digit is in the incorrect place.
                clues.append('Pico')

        if len(clues) == 0:
            return 'Bagel' # There are no correct digits at all
        else:
            '''Sort the clues in alphabetical order so their original order does not give away information'''
            clues.sort()
            # Make a single string from the list of string clues.
            return ' '.join(clues)
    

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()







