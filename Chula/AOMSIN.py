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

    print("ALRIGHT, Let's Play...")
    print()

    p1WinCount = 0
    p2WinCount = 0
    drawCount = 0
    for game_num in range(26):
        player1Hand = p1_cards[game_num]
        player2Hand = p2_cards[game_num]
        player1HandValue = checkValue(player1Hand[0])
        player2HandValue = checkValue(player2Hand[0])

        result = checkWinner(player1HandValue, player2HandValue)

        print("Hand number: " + str(game_num+1))
        print("Player 1 has: " + player1Hand[0] + " of " + player1Hand[1])
        print("Player 2 has: " + player2Hand[0] + " of " + player2Hand[1])

        if result is True:
            print("Player 1 wins the hand")
            p1WinCount += 1
        elif result is False:
            print("Player 2 wins the hand")
            p2WinCount += 1
        elif result is None:
            print("DRAW!!!!!!!!!")
            drawCount += 1
        print()

    return p1WinCount, p2WinCount, drawCount

card_deck = create_deck()
player1card, player2card = deal_cards(card_deck)
p1WinCount, p2WinCount, drawCount = play_game(player1card, player2card)

print()
print("-----------------------------")
print("FINAL GAME RESULTS:")
print("Player 1 won " + str(p1WinCount) + " hands")
print("Player 2 won " + str(p2WinCount) + " hands")
print(str(drawCount) + " hands were drawn")
result = checkWinner(p1WinCount, p2WinCount)
print()
if result is True:
    print("PLAYER 1 IS THE WINNER!!")
elif result is False:
    print("PLAYER 2 IS THE WINNER!!")
elif result is None:
    print("IT WAS A TIE GAME!!")