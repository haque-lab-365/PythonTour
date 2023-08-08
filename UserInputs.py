import random



while True:
    
    print("Please enter/guess a three digits number")
    guess = input('> ')
    
    if(len(guess) < 0 or not guess.isdecimal()):
        print("Please enter a valid decimal number.")
        #break
    
    if len(guess) != 3:
        print("You entered {} Please enter a 3 digits decimal number, example: {}".format(234))
        #break

    #print("The guessed number is {}".format(guess))
    print("Do you want to quit?")

    if input('> ').lower().startswith("y"):
        print("Waiting to see you soon!!!")
        break
