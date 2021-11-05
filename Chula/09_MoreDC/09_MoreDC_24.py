data = {}
while True:
    q_filter = input()
    if q_filter == "q":
        break
    else:
        character = q_filter.strip().split(",")
        if character[1] not in data:
            data[character[1]] = [character[0]]
        else:
            data[character[1]].append(character[0])

prnt = ""
c = 0
for i in data: 
    prnt += i.strip() + ": " + ", ".join(data[i])
    c += 1
    if c != len(data):
        prnt += "\n"

print(prnt)

