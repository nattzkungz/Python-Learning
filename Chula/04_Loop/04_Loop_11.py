str_input = input()

characters = {}

for _ in str_input:
    characters[_] = str_input.count(_)
printthis = ''
for _ in characters:
    printthis += _ + " " +str(characters[_])

print(printthis)