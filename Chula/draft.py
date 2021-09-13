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
    
    left_half = decklist[0:round((len(decklist)/2))]
    right_half = decklist[round((len(decklist)/2)):len(decklist)]
    
    shuffled = []
    
    for i in range(len(decklist)):
        if i % 2 == 0:
            shuffled.append(left_half[])
            
        elif i % 2 != 0:
            shuffled.append(right_half[])
            
    
    print_to_string = ''
    for _ in shuffled:
        print_to_string += '|' + _ + '|'

    new_deck = print_to_string
    print(new_deck)

shuffle('|2H||3H||4H||5H||JS||QS||KS||5H||JS||QS||KS||5H||JS||QS||KS||5H||JS||QS||KS||5H||JS||QS||KS||5H||JS||QS||KS|')