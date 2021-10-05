word_inp = input()
plural1 = ["s", "x"]
plural2 = ["ch", "es"]

def checkPlural(word):
    last1 = word[-1:-2]
    last2 = word[-1:-3]
    for _ in plural2:
        if last2 == _:
            sx = True
            return sx
        elif last1 == _:
            ches = True
            return ches
        else:
            return False


if checkPlural(word_inp) == :
    