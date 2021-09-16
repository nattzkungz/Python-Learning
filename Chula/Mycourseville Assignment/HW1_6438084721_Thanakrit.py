#@title
# HW1 : Card Game v2
# ID Firstname Lastname

import time
import random

def generate_deck(n_cards, n_shuffles):
    print('Shuffle', end='')
    deck = ''
    for suit in 'CDHS':
        for face in 'A23456789TJQK':
            deck += '|' + face + suit + '|'
        deck = cut(deck, random.randint(0, n_cards))
        deck = shuffle(deck)
        time.sleep(0.1)
        print('.', end='')
    print()
    return deck[:4*n_cards]

def play(n_cards, n_in_hand):
    print('Start a card game with', n_cards, 'cards.')
    deck = generate_deck(n_cards, 20)
    p1, deck = deal_n_cards(deck, n_in_hand)
    p2, deck = deal_n_cards(deck, n_in_hand)
    players = [p1, p2]
    
    table_cards, deck = deal_n_cards(deck, 1)
    fail = False
    turn = 0
    
    while True:
        show_game_status(deck, table_cards)
        show_table_cards(table_cards)
        show_player_cards(players[turn], turn+1)

        k = select_card_number(players[turn])
        n_player_cards = len(players[turn])//4
        
        valid = (k != 0)
        
        if valid: 
            cards = players[turn]
            card = peek_kth_card(cards, k)
            print('      Playing :', card)
            
            valid_left = eq_suit_or_value(card, table_cards[:4])
            valid_right = eq_suit_or_value(card, table_cards[-4:])
            valid = (valid_left or valid_right)
                     
            if valid:
                if valid_right:
                    table_cards += card
                else: # valid_left:
                    table_cards = card + table_cards
                players[turn] = remove_kth_card(cards, k)
                fail = False
        
        if not valid:
            print(' ** Invalid **')
            if len(deck) == 0:
                if fail: break
                fail = True
            if len(deck) > 0:
                print(' >> get a new card')
                card, deck = deal_n_cards(deck, 1)
                players[turn] = card + players[turn]
                
        show_player_cards(players[turn], turn + 1)
        if len(players[turn]) == 0:
            break
        turn = (turn + 1) % len(players)
        
    if len(deck) == 0:
        print('\n** No more cards **')
    print('*'*20)
    if len(deck) == 0 and \
       len(players[0]) == len(players[1]):
        print('Draw!!!')
    elif len(players[0]) < len(players[1]):
        print('Player # 1 win!!!')
    else:
        print('Player # 2 win!!!')

def eq_suit_or_value(card1, card2):
    return card1[1] == card2[1] or \
           card1[2] == card2[2]

def show_game_status(deck, table):
    print('-'*40)
    print('Deck remaining: {} | On table : {}'.format(len(deck)//4, len(table)//4))
    
def show_player_cards(cards, k):
    print('   Player #', k, ':', cards)

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            return 0
            #pass

def select_card_number(player):
    nc = len(player)//4
    k = input_int('  Select card # (1-'+str(nc)+') : ')
    if not (1 <= k <= nc):
        k = nc
    return k

#----------------------------------------------------------------------------------
#  TODO:
#    Complete the body of the function.
#    If your program is correct in each, the game will be played until game over.
#    If any of you code is wrong you will see the test messages about each of the
#    testcase that the output is not as expected.
#----------------------------------------------------------------------------------
def peek_kth_card(cards, k):
    # cards is a string storing cards (may be one card) e.g., "|2H||4S||TD||AC|"
    # k is an integer indicating card number that is interested (leftmost is 1)

    # TODO: 
    #   assign the variable the_kth_card to store a string that represents 
    #     the kth card in cards 

    # Example:
    #   cards stores "|2H||4S||TD||AC|", k is 2 
    #   the_kth_card ---> "|4S|"
    """
    >>> peek_kth_card("|2H||4S||TD||AC|", 1)
    '|2H|'
    >>> peek_kth_card("|2H||4S||TD||AC|", 2)
    '|4S|'
    >>> peek_kth_card("|2H||4S||TD||AC|", 3)
    '|TD|'
    >>> peek_kth_card("|2H||4S||TD||AC|", 4)
    '|AC|'
    """

    the_kth_card = cards[(k*4)-4:(k*4)]
    return the_kth_card

#----------
def remove_kth_card(cards, k):
    # cards is a string storing cards (may be one card) e.g., "|2H||4S||TD||AC|" 
    # k is an integer indicating card number that is interested (leftmost is 1)

    # TODO: 
    #   assign the variable new_card to be the same as cards but removing the kth card, 
    #     the original cards remain unchanged 

    # Example: 
    #   cards stores "|2H||4S||TD||AC|", k is 2
    #   new_cards ---> "|2H||TD||AC|"
    """
    >>> remove_kth_card('|2H||4S||TD||AC|', 1)
    '|4S||TD||AC|'
    >>> remove_kth_card('|2H||4S||TD||AC|', 2)
    '|2H||TD||AC|'
    >>> remove_kth_card('|2H||4S||TD||AC|', 3)
    '|2H||4S||AC|'
    >>> remove_kth_card('|2H||4S||TD||AC|', 4)
    '|2H||4S||TD|'
    """
    
    new_cards = cards[0:(k*4)-4] + cards[(k*4):len(cards)]
    return new_cards

#----------
def deal_n_cards(deck, n):
    # deck is a string storing cards (may be one card) e.g. "|2H||4S||TD||AC||AD||AS|"
    # n is an integer indicates the number of card to be dealed from the deck (n leftmost cards)

    # TODO: assign variable cards to store n leftmost cards from deck 
    #       assign variable new_deck to be the same as deck which remove n leftmost cards
    #       Note that, n always <= number of cards in deck

    # Example: deck stores "|2H||4S||TD||AC|", n stores 3
    #          cards ---> "|2H||4S||TD|"
    #          new_deck ---> "|AC|"
    """
    >>> deal_n_cards('|2H||4S||TD||AC|', 1)
    ('|2H|', '|4S||TD||AC|')
    >>> deal_n_cards('|2H||4S||TD||AC|', 3)
    ('|2H||4S||TD|', '|AC|')
    >>> deal_n_cards('|2H||4S||TD||AC|', 4)
    ('|2H||4S||TD||AC|', '')
    >>> deal_n_cards('|2H||4S||TD||AC|', 5)
    ('|2H||4S||TD||AC|', '')
    """

    cards = deck[0:(n*4)]
    new_deck = deck[(n*4):len(deck)]
    
    return cards, new_deck

#----------
def cut(deck, m):
    # deck is a string storing cards, e.g. "|2H||4S||TD||AC||3H||4H||5H||6H||7H||8H|" 
    # m is an integer for m leftmost cards of deck (0 <= m <= number of cards in deck)

    # TODO: 
    #   assign variable new_deck to store string result from move m leftmost cards 
    #     of deck append to the right of deck

    # Example: 
    #   deck stores "|2H||3H||4H||5H||6H|", m stores 3
    #   new_deck ---> "|5H||6H||2H||3H||4H|"
    """
    >>> cut('|2H||3H||4H||5H||6H|', 1)
    '|3H||4H||5H||6H||2H|'
    >>> cut('|2H||3H||4H||5H||6H|', 3)
    '|5H||6H||2H||3H||4H|'
    >>> cut('|2H||3H||4H||5H||6H|', 4)
    '|6H||2H||3H||4H||5H|'
    """

    decklist = deck.split("|")
    for _ in decklist:
        if _ == "":
            decklist.remove(_)
    
    swap = decklist[0:m]
    
    for _ in swap:
        if _ in decklist:
            decklist.remove(_)

    decklist += swap

    print_to_string = ''
    for _ in decklist:
        print_to_string += '|' + _ + '|'
    new_deck = print_to_string
    return new_deck

#----------
def shuffle(deck):
    # deck is a string storing cards, e.g. "|2H||4S||TD||AC||3H||4H||5H||6H||7H||8H|"

    # TODO: 
    #   assign variable new_deck to store cards taken from left half and right 
    #     half of deck one card at a time

    # Example: when the number of cards is odd
    #   deck stores "|2H||3H||4H||5H||JS||QS||KS|"
    #   new_deck ---> "|2H||JS||3H||QS||4H||KS||5H|"
    #      when the number of cards is even
    #   deck stores "|2H||3H||4H||5H||JS||QS||KS||AS|"
    #   new_deck ---> "|2H||JS||3H||QS||4H||KS||5H||AS|"
    """
    >>> shuffle('|2H||3H||4H||5H||JS||QS||KS|')
    '|2H||JS||3H||QS||4H||KS||5H|'
    >>> shuffle('|2H||3H||4H||5H||JS||QS||KS||AS|')
    '|2H||JS||3H||QS||4H||KS||5H||AS|'
    """
    decklist = deck.split("|")
    for _ in decklist:
        if _ == "":
            decklist.remove(_)
    import math 
    left_half = decklist[0:math.ceil(len(decklist)/2)]
    right_half = decklist[math.ceil(len(decklist)/2):len(decklist)]
    
    shuffled = []
    l = 0
    r = 0
    for i in range(len(decklist)):
        if i % 2 == 0:
            shuffled.append(left_half[l])
            l += 1

        elif i % 2 != 0:
            shuffled.append(right_half[r])
            r += 1
    print_to_string = ''
    for _ in shuffled:
        print_to_string += '|' + _ + '|'

    new_deck = print_to_string
    return new_deck

#----------
def show_table_cards(cards):
    # cards is a string storing cards (may be one card) e.g. "|2H||4S||TD||AC|" 
    # the maximum number of cards to be display on the table is 5
    
    # TODO: 
    #   If the table is large enough to display all the cards, show them all.
    #   When there are more cards to be displayed than the table, 
    #     shows 2 leftmost, and 2 rightmost cards and show .... in the middle 
    #   this function return nothing
    """
    >>> show_table_cards("|2H|")
    -----------
    Table: |2H|
    -----------
    >>> show_table_cards("|2H||3H||4H||5H|")
    -----------------------
    Table: |2H||3H||4H||5H|
    -----------------------
    >>> show_table_cards("|2H||3H||4H||5H||6H|")
    ---------------------------
    Table: |2H||3H||4H||5H||6H|
    ---------------------------
    >>> show_table_cards("|2H||3H||4H||5H||6H||7H|")
    ---------------------------
    Table: |2H||3H|....|6H||7H|
    ---------------------------
    >>> show_table_cards("|2H||3H||4H||5H||6H||7H||8H|")
    ---------------------------
    Table: |2H||3H|....|7H||8H|
    ---------------------------
    """
    
    decklist = cards.split("|")
    for _ in decklist:
        if _ == "":
            decklist.remove(_)
    show_this = ''
    tmp = []
    tmp1 = []
    if len(decklist) <= 5:
        show_this += cards
    else:
        print_to_string = ''
        tmp += decklist[0:2]
        for _ in tmp:
            show_this += '|' + _ + '|'
        show_this += "...."
        tmp1 += decklist[len(decklist)-2:len(decklist)]
        for _ in tmp1:
            show_this += '|' + _ + '|'

    cards_to_show = show_this
    border = '-'*(len(show_this)+7)
    print(border)
    print('Table:', cards_to_show)
    print(border)
  
#-------------------------------------------------
if __name__ == "__main__":
  import doctest
  doctest.testmod()
#-------------------------------------------------

"""### Play the game"""
n_cards = 15
initial_hand_size = 5
play(n_cards, initial_hand_size)
