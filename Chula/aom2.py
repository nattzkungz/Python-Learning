def create_deck():
    typeOfCards = ["Clubs", "Diamonds", "Hearts", "Spades"]
    cardNumber = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    deck = list()
    for card in cardNumber:
        for type in typeOfCards:
            deck.append([card, type])
    return deck

def deal_cards(the_deck):
    import random
    random.shuffle(the_deck)
    player1Card = the_deck[0:26]
    player2Card = the_deck[26:53]
    return player1Card, player2Card

def checkWinner(p1Hand,p2Hand):
        if p1Hand > p2Hand:
            return True
        elif p2Hand > p1Hand:
            return False
        else:
            return None

def play_game(p1_cards, p2_cards):

    def checkValue(hand):
            if hand == "Ace":
                value = 14
            elif hand == "King":
                value = 13
            elif hand == "Queen":
                value = 12
            elif hand == "Jack":
                value = 11
            else:
                value = int(hand)
            return value

    p1WinCount = 0
    p2WinCount = 0
    drawCount = 0
    for game_num in range(26):
        player1Hand = p1_cards[game_num]
        player2Hand = p2_cards[game_num]
        player1HandValue = checkValue(player1Hand[0])
        player2HandValue = checkValue(player2Hand[0])

        result = checkWinner(player1HandValue, player2HandValue)

        if result is True:
            p1WinCount += 1
        elif result is False:
            p2WinCount += 1
        elif result is None:
            drawCount += 1

    return p1WinCount, p2WinCount, drawCount

numberOfSimulations = int(input("Enter in number of simulations of War game:"))
def sim_num_games(sim_num):
    p1WinCountTotal, p2WinCountTotal, drawCountTotal = 0,0,0
    for gameNumber in range(sim_num):

        card_deck = create_deck()
        player1card, player2card = deal_cards(card_deck)
        p1WinCount, p2WinCount, drawCount = play_game(player1card, player2card)
        result = checkWinner(p1WinCount, p2WinCount)

        if result is True:
            print("Sim " + str(gameNumber+1) + " : PLAYER 1 IS THE WINNER!!")
            p1WinCountTotal += 1
        elif result is False:
            print("Sim " + str(gameNumber+1) + " : PLAYER 2 IS THE WINNER!!")
            p2WinCountTotal += 1
        elif result is None:
            print("Sim " + str(gameNumber+1) + " : THE GAME WAS A DRAW!!")
            drawCountTotal += 1

    return p1WinCountTotal, p2WinCountTotal, drawCountTotal


p1WinCountTotal, p2WinCountTotal, drawCountTotal = sim_num_games(numberOfSimulations)
print("---------------------------------------")
print("After " + str(numberOfSimulations) + " simulations the results are:")
print(f"Player 1 won {p1WinCountTotal} times")
print(f"Player 2 won {p2WinCountTotal} times")
print(f"There were {drawCountTotal} (ties)")
