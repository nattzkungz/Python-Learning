character = list(input())
last1 = character[-1:]
last2 = character[-2:]
if last1 == ['s'] or last1 == ['x'] or last2 == ['c','h'] or last2 == ['e','s']:
    character.append("es")
elif last1 == ['y'] and character[-2] not in ["a","e","i","o","u"]:
    character.pop(-1)
    character.append("ies")
else:
    character.append("s")


print("".join(character))