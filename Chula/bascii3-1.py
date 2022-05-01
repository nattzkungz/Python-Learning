def create_deck():
    suit = ["Spades", "Hearts", "Diamonds", "Clubs"]
    deck = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
    completeDeck = []

    for i in deck:
        for j in suit:
            completeDeck.append([str(i),j])

    return completeDeck

def deal_cards(the_deck):
    import random
    p1Deck, p2Deck = [], []
    while len(p1Deck) < 26:
        card = random.choice(the_deck)
        if card not in p1Deck:
            p1Deck.append(card)
            the_deck.remove(card)
    
    p2Deck = the_deck
    random.shuffle(p2Deck)
    return p1Deck, p2Deck

def play_game(p1_cards, p2_cards):
    value = ["2","3","4","5","6","7","8","9","10","Jack", "Queen", "King", "Ace"]
    p1Win, p2Win, drawn = 0,0,0
    print("ALRIGHT, Let's Play...\n")
    for i in range(26):
        p1Hand = p1_cards[i]
        p1Value = value.index(p1Hand[0])
        p2Hand = p2_cards[i]
        p2Value = value.index(p2Hand[0])
        print(f"Hand number: {i+1}")
        print(f"Player 1 has: {p1Hand[0]} of {p1Hand[1]}")
        print(f"Player 1 has: {p2Hand[0]} of {p2Hand[1]}")
        if p1Value > p2Value:
            print("Player 1 wins the hand")
            p1Win += 1
        elif p2Value > p1Value:
            print("Player 2 wins the hand")
            p2Win += 1
        else:
            print("DRAW!!!!!!!!!")
            drawn += 1
        print()
    
    return p1Win, p2Win, drawn
card = deal_cards(create_deck())
game = play_game(card[0], card[1])

p1Win = game[0]
p2Win = game[1]
drawn = game[2]

print("-"*29)
print("FINAL GAME RESULTS:")
print(f"Player 1 won {p1Win} hands")
print(f"Player 2 won {p2Win} hands")
print(f"{drawn} hands were drawn")
print()
if p1Win > p2Win:
    print("PLAYER 1 IS THE WINNER!!")
elif p2Win > p1Win:
    print("PLAYER 2 IS THE WINNER!!")
else:
    print("IT WAS A TIE GAME!!")
