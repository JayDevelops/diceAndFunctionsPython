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
    print(randomNum, "\n")

dice2UserInput = int(input("Please input a number to roll a dice until this number: "))
dice2(dice2UserInput)

def dice3(newUntil):
    #  Prints out the user range when they do have a valid input
    while newUntil != 0:
        # Prints out a random number from 1 until the including variable, hence +1
        randomNum = random.randrange(1, newUntil + 1)
        print(randomNum, "\n")
        break
    else:
        # Prints out 6 sides when there's no default values
        fixedNum = random.randrange(1, 7)

dice3UserInput = int(input("Please input a number to roll a dice until this number: "))
dice3(dice3UserInput)

def dice4(specificUntil):
    while specificUntil != 0:
        if specificUntil == 4 or specificUntil == 6 or specificUntil == 8:
            specificRanNum = random.randrange(1, specificUntil + 1)
            print(specificRanNum, end=" ")
        elif specificUntil == 10 or specificUntil == 12 or specificUntil == 20:
            specificRanNum = random.randrange(1, specificUntil + 1)
            print(specificRanNum, end=" ")
        else:
            print("Please input a number which is either 4, 6, 8, 10, 12, 20", "\n")
        break
    else:
        print("Please input a value which is either 4, 6, 8, 10, 12, 20", "\n")

dice4UserInput = int(input("Please input a number to roll a dice until this number: "))
dice4(dice4UserInput)


def dice5(sides, rolls):
    index = 1
    if rolls != 0:
        while rolls >= index:
            dice4(sides)
            index += 1
    else:
        dice4(sides)

dice5SidesInput = int(input("\nPlease input a number to roll a dice until this number: "))
dice5RollsInput = int(input("Please input a number to rolls this amount of times: "))

dice5(dice5SidesInput, dice5RollsInput)

# Only prints out heads or tail
def dice6(sides, rolls):
    # Starting at 0, the index
    index = 0

    # Default the sides to 2 now
    sides = 2
    if rolls != 0:
        while rolls >= index:
            # From 1 - 2
            number = random.randrange(1, 3)
            if number == 1:
                print("You landed on heads")
            else:
                print("You landed on tails")
            index += 1
    else:
        number = random.randrange(1, 3)
        if number == 1:
            print("You landed on heads")
        else:
            print("You landed on tails")

dice6SidesInput = int(input("\n\nPlease input a number to roll a this specific number: "))
dice6RollsInput = int(input("\nPlease input a number to roll a this one until this number: "))
dice6(dice6SidesInput, dice6RollsInput)


# Only returns the string, doesn't print it out
def dice7(arg):
    # Starting at 0, the index
    index = 0

    # Default the sides to 2 now
    sides = 2
    if rolls != 0:
        while rolls >= index:
            # From 1 - 2
            number = random.randrange(1, 3)
            if number == 1:
                return "You landed on heads"
            else:
                return "You landed on tails"
            index += 1
    else:
        number = random.randrange(1, 3)
        if number == 1:
            return "You landed on heads"
        else:
            return "You landed on tails"

dice7idesInput = int(input("\n\nPlease input a number to roll a this specific number: "))
dice7RollsInput = int(input("\nPlease input a number to roll a this one until this number: "))
dice6(dice7SidesInput, dice7RollsInput)
