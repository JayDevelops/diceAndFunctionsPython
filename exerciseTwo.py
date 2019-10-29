import random

def dice1():
    # From 1 - 6
    number = random.randrange(1, 7)
    print(number, "\n")

# Calls the function
print("This is a random dice roll, below ")
dice1()

def dice2(until):
    # Prints out a random number from 1 until the including variable, hence +1
    randomNum = random.randrange(1, until + 1)
    print(randomNum)

dice2UserInput = int(input("Please input a number to roll a dice until this number: "))
dice2(dice2UserInput)

def dice3(newUntil):
    #  Prints out the user range when they do have a valid input
    while newUntil != "":
        # Prints out a random number from 1 until the including variable, hence +1
        randomNum = random.randrange(1, newUntil + 1)
        print(randomNum)
        break
    else:
        # Prints out 6 sides when there's no default values
        fixedNum = random.randrange(1, 7)

dice3UserInput = int(input("Please input a number to roll a dice until this number: "))
dice3(dice3UserInput)
