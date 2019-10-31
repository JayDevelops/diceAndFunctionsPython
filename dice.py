import random

def dice4(sides, rolls):
    index = 1
    if rolls != 0:
        print("The numbers below are going to be generated with this amount of rolls you entered: ", rolls, "\n")
        while rolls >= index:
            specificRanNum = random.randrange(1, sides + 1)
            index += 1
            print(specificRanNum, end=" ")
    else:
        specificRanNum = random.randrange(1, sides + 1)
        print("You rolled only once, at: ", specificRanNum, end=" ")


while True:
    dice4SidesInput = int(input("Please input a number to roll a dice until this number: "))
    dice4RollsInput = int(input("Please input a number to rolls this amount of times: "))
    if dice4SidesInput != 0 and dice4RollsInput != 0:
        dice4(dice4SidesInput, dice4RollsInput)
        break
    else:
        print("Please input a real number which is bigget than 0.\n")
        print("I will keep asking you and you cannot exit until you input a real number which is bigget than 0!!!😏\n")
