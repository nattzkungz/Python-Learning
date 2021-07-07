from random import randint
from os import system

def clear(): system("clear")

def guessingGame():
    number = randint(1,100)
    life_counter = 0
    win = False
    print("Welcome to number guessing game")
    print("I'm thinking of number 1 to 100")
    print("Try to guess it")
    print(f"Pssst the answer is {number}")

    if input("Do you want to play on 'easy' or 'hard' level: ") == "easy":
        life_counter += 10
    else:
        life_counter += 5
    
    while life_counter > 0:
        life_counter -= 1
        user_guess = int(input("Guess a number: "))
        if user_guess > number:
            print("Too high")
        elif user_guess < number:
            print("Too low")
        elif user_guess == number:
            print("You got the correct answer")
            win = True
            break
        print(f"You have {life_counter} guess left")

    if life_counter == 0 and win == False:
        print("You lose")
    else:
        print(f"You got it the answer was {number}")

STATUS = True

while STATUS:
    clear()
    guessingGame()
    if input("Do you want to play number guessing game? press 'enter' to play and 'n' to stop: ") == "n":
        STATUS = False
