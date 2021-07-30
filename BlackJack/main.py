import random
from art import logo
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

flag = False

def clear(): system('clear')

def blackjack():

  player_cards = []
  computer_cards = []

  def random_user(): player_cards.append(random.choice(cards))

  def random_computer(): computer_cards.append(random.choice(cards))

  def win_msg(): print(f"Computer cards are {computer_cards} which scores {computer_score}")

  def check_ace(cards):
      if 11 in cards and len(cards) == 2:
          cards.remove(11)
          cards.append(1)

  gameStatus = True
  blackjack = False
  userBlackjack = False
  comBlackjack = False

  for x in range(2):
    random_user()
    random_computer()

  player_score = sum(player_cards)
  computer_score = sum(computer_cards)

  if 10 in player_cards and len(player_cards) == 2:
    if 11 in player_cards and len(player_cards) == 2:
      player_score = 0
      blackjack = True
      userBlackjack = True

  if 10 in computer_cards and len(computer_cards) == 2:
    if 11 in computer_cards and len(computer_cards) == 2:
      computer_score = 0
      blackjack = True
      comBlackjack = True

  while sum(computer_cards) < 17:
    if computer_score < 17:
      random_computer()
      check_ace(computer_cards)
    else:
      break

  if not blackjack:
    while gameStatus:
      player_score = sum(player_cards)
      computer_score = sum(computer_cards)
      print(f"  Your cards are {player_cards} and current score is {player_score}")
      print(f"  Computer first card is {computer_cards[0]}")
      if player_score < 21:
        if input("To draw another card enter 'y' and pass enter 'n': ") == "y":
          random_user()
        else:
          
          if player_score > 21:
            print(f"  {win_msg()}  You went over, you lose")
            gameStatus = False
          elif computer_score > 21:
            print(f"  {win_msg()}  You Win, computer went over")
          elif player_score > computer_score:
            print(f'  {win_msg()}  You Win!!!')
          elif player_score < computer_score:
            print(f"  {win_msg()}  You lose /sadface")
          elif player_score == computer_score:
            print("Tie")
          gameStatus = False
      elif player_score > 21:
        check_ace(player_cards)
        if sum(player_cards) > 21:
            print("You went over, you lose")
            gameStatus = False
      else:
        if player_score > 21:
          print(f"{win_msg()}  You went over, you lose")
          gameStatus = False
        elif computer_score > 21:
          print(f"  {win_msg()}  You Win, computer went over")
        elif player_score > computer_score:
          print(f'  {win_msg()} \n  You Win!!!')
        elif player_score < computer_score:
          print(f"  {win_msg()} You lose /sadface")
        elif player_score == computer_score:
          print("Tie")
          
  elif blackjack:
    if userBlackjack and comBlackjack:
      print(f"  Your cards are {player_cards}\n  Computer cards are {computer_cards}\n  You lose, computer also got blackjack")
    elif userBlackjack:
      print(f"  Your cards are {player_cards} and u got blackjack\n   Computer cards are {computer_cards}\n YOU WIN")
    elif comBlackjack:
      print(f"  You lose, computer got blackjack {computer_cards}")

if input("To play blackjack press 'enter' and 'n' to quit") == 'n':
  print("bye")
  flag = False
else:
  flag = True
  while flag:
    clear()
    print(logo)
    blackjack()
    if input("Do you want to play another game? press 'enter' to play, 'n' to stop: ") == "n":
      flag = False
      break
    else:
      flag = True

print("Yay")