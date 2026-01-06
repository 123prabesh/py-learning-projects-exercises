import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)

guesses = 0

is_runnong = True

print("Python Number Guessing Game")

print(f"Select a number betwwen {lowest_num} and {highest_num}")

while is_runnong:
    
    guess = input("Ebter you guess:")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1


        if guess < lowest_num or guess > highest_num:
            print("Guess is out of range.")
            print(f"Please select a number betwwen {lowest_num} and {highest_num}")

        elif guess < answer:
            print("Two low!! try again!!")
        elif guess > answer:
            print("Two high!! Try again !!")
        else:
            print(f"CORRECT! The answer was {answer}.\n Number of guesses was {guesses}")
    else:
        print("Invalid  guess.")
        print(f"Please select a number betwwen {lowest_num} and {highest_num}")
    