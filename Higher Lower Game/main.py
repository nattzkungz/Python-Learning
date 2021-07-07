from random import randint
from game_data import data
from os import system
from art import logo, vs


def clear(): system("clear")


ALREADY_USED = []


def random_data():
    status = True
    while status:
        person_number = randint(0, len(data)-1)
        person = data[person_number]
        if person_number not in ALREADY_USED:
            ALREADY_USED.append(person_number)
            status = False
            return person
        else:
            status = True


def print_choice(person):
    print(f"{person['name']}, a {person['description']}, from {person['country']}")


score_counter = 0
gameStatus = True


def compare_data(user_choice, another_choice):
    if user_choice['follower_count'] > another_choice['follower_count']:
        global score_counter
        score_counter += 1
        print(f"Correct!, your score is {score_counter}")
        return True
    else:
        global gameStatus
        gameStatus = False
        print(f"You Lost, your score is {score_counter} point")
        return False


choiceA = random_data()

while gameStatus:
    clear()
    choiceB = random_data()
    print(logo)
    print_choice(choiceA)
    print(vs)
    print(ALREADY_USED)
    print_choice(choiceB)
    user_input = input("Who has more follower? 'A' or 'B': ").lower()
    if len(ALREADY_USED) == len(data):
        print("Out of choices")
        print(f"You won the game with whopping {score_counter} points")
        gameStatus = False
    elif user_input == 'a':
        compare_data(user_choice=choiceA, another_choice=choiceB)
    elif user_input == 'b':
        compare_data(user_choice=choiceB, another_choice=choiceA)
        choiceA = choiceB
    else:
        print("Wrong letter")
