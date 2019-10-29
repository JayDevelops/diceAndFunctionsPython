# Name function here
def name():
    hello = "hello from my function"
    print(hello)

# Call = Execute the code
name()


# Multiply the number
def mult(num):
    sum = num * 7
    print(sum)

# Input variable for the user
userInput = int(input("Input a number here: "))

# Call the function with the userInput
mult(userInput)


def userStringFunc():
    userString = input("Input a cool word: ")
    newString = "No, you're " + userString
    print(newString)

# Call the function here
userStringFunc()
