import random

# Play a simple guessing game with the user


# Generate a random password number from 1 to 10 inclusive.
def random_password():
    password = random.randrange(1, 11)
    return password

# Ask the user to input a guess until then enter a value from 1 to 10.
def get_guess():
    guess = 0
    while guess < 1 or guess > 10:
        guess = int(input("Guess the password, from 1 to 10: "))
    return guess
    
# Give a message based on how many attempts it took
def print_summary(tries):
    print("It took you", number_of_tries, "guesses!")
    if tries == 1:
        print("Nice! You cheated, didn't you?")
    elif 2 <= tries <= 4:
        print("Hey, that's better than average!")
    elif tries == 5:
        print("That's the average number of guesses!")
    elif tries <= 9:
        print("You're a little unlucky.")
    elif tries == 10:
        print("You're REALLY unlucky.")
    else:
        print("You may need to rethink your guessing strategy...")




# The "main" application
def main():
    password = random_password()
    number_of_tries = 1
    guess = get_guess()
    while guess != password:
        number_of_tries += 1
        guess = get_guess()

    print_summary(number_of_tries)


# Defining functions does not execute them!!! We must call the main ourselves.
# This is technically the first line to be executed.
main()


# This file shows many reasons for using functions:
# 1. Improve readability by using names to represent blocks of code.
# 2. Reduce repetition.
# 3. Parameterize behavior.
# 4. Isolate concerns.


