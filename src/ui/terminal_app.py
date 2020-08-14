from src.model.randomness import random_dice

# Introduces application
print("Welcome to diceroller, quit anytime but typing 'quit'\n")
choice = ""

# While loop for user input, breaks on 'quit'
while not choice == "quit":
    print("Please type one of the following: ")
    print("D6")
    print("D8")
    print("D20")
    choice = input()

    if choice == "D6":
        print(random_dice(6))
    elif choice == "D8":
        print(random_dice(8))
    elif choice == "D20":
        print(random_dice(20))
    else:
        print("Incorrect input")
