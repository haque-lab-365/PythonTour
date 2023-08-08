# https://inventwithpython.com/bigbookpython/
# https://inventwithpython.com/bigbookpython/project1.html

import random

NUM_DIGITS = 3 # (!) Try setting this to 1 or 10.
MAX_GUESS = 10 # (!) Try setting this to 1 or 10.


def main():
    
    print(''' Bagels -  a deductive logic game By Shahidul Haque - shahidul27@yahoo.com 
          I am thinking of a {} digits number with no repeated digits.
          Try to guess what it is. Here are some clues:
          When I say  ---- That means
          
          
          PICO :  One digit is correct but in the wrong position
          FERMI : One digit is correct and in the right position
          Bagels: No digit is correct
    
          For example -  if the secret number was 248 and your guess was 843, the clues would be Fermi, Pico '''.format(NUM_DIGITS))
    
    while True:
        secretNumber = getSecretNumber()
        print("I have thought up a number")
        print("You have guesses {} to get to ge it".format(MAX_GUESS))

        numGuesses = 1
        while numGuesses < MAX_GUESS:
            guess = ''
            
            #-Keep looping until they enter a valid guess (at least 3 digits):
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess a valid 3 digits #{}: '.format(numGuesses))
                guess = input('> ')
            
            clues = getClause(guess, secretNumber)
            print(clues)
            numGuesses += 1

            if guess == secretNumber:
                break  # They're correct, so break out of this loop.
            if numGuesses == MAX_GUESS:
               print("You ran out of guesses!")
               print("The answer was {} ".format(secretNumber))
        
        if not input('> ').lower().startswith("y"):
            break
    
    print("Thanks for playing...")

    #getSecretNumber()
    #print(f'The secret number is {getSecretNumber()}')    

def getSecretNumber():

    """ Returns a string made up of NUM_DIGITS with unique random digits """
    numbers  = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers)       # Shuffle them into random orders.
    print(numbers)
    #Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    
    return secretNum

def getClause(guess, secretNum):
   
   """ Returns a string with Pico, Fermin and Bagels clues for a guess and secret number pair """
   if guess == secretNum:
       return "You got it"
   
   clues = []

   for i in range(len(secretNum)):
       if(guess[i] == secretNum[i]):
        # A correct digit is in the correct place.
        clues.append("Fermi")
       
       elif guess[i] in secretNum:
        # A correct digit is in the incorrect place.
        clues.append("Pico")
   if len(clues) == 0:
      return "Bagels" # There are no correct digits at all!!!
   else:
      clues.sort() # Sort the clues in the alphabetical order so their original order doesn't give information away.
      return ' '.join(clues) # Make a single string from the list of string clause.


# Start the engine
if __name__ == '__main__':
    main()