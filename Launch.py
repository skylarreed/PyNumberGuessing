# This is a simple number guessing game written by me, Skylar.
import random
import os

TOTAL_GUESSES = 10
keep_playing = True
def guess_ez():
    return random.randint(1, 50)
def guess_hard():
    return random.randint(1, 100)

def clear_console():
    os.system('cls')

def easy_mode():
    guesses = TOTAL_GUESSES
    number = guess_ez()
    while guesses > 0:
        guess = int(input("What is your guess?: "))
        if guess == number:
            print(f"Dang, you have seemed to guess the number right. The number was {number}. You had {guesses} lives remaining!")
            return "win"
        elif guess > number:
            guesses -= 1
            print(f"Your guess of {guess} was higher than my number. You have lost a life. You now have {guesses} lives remaining.")
        elif guess < number:
            guesses -= 1
            print(f"Your guess of {guess} was lower than my number. You have lost a life. You now have {guesses} lives remaining.")
    return "loss"
def hard_mode():
    guesses = TOTAL_GUESSES
    number = guess_hard()
    while guesses > 0:
        guess = int(input("What is your guess?: "))
        if guess == number:
            print(f"Dang, you have seemed to guess the number right. The number was {number}. You had {guesses} lives remaining!")
            return "win"
        elif guess > number:
            guesses -= 1
            print(f"Your guess of {guess} was higher than my number. You have lost a life. You now have {guesses} lives remaining.")
        elif guess < number:
            guesses -= 1
            print(f"Your guess of {guess} was lower than my number. You have lost a life. You now have {guesses} lives remaining.")
    return "loss"
print("Welcome to Skylar's number guessing game.")
print("The rules are simple, you have a total of 10 guesses to figure out the number.")
print("If you guess higher than the number, I will tell you the number is lower. If you guess lower, I will tell you higher.")
print("There is an easy and hard mode. Easy consists of numbers between 1-50. Hard consists of numbers between 1-100.")
while keep_playing == True:
    if input("\nWould you like to play easy or hard mode: ") == "easy":
        clear_console()
        easy_mode()
        if input("Would you like to play again? 'y' or 'n': ") == 'n':
            keep_playing = False
    else:
        clear_console()
        hard_mode()
        if input("Would you like to play again? 'y' or 'n': ") == 'n':
            keep_playing = False