data = {}
for n in range(int(input())):
    ppl = input().strip().replace(":", "", 1).translate({ord(","): None}).split(" ")
    data[ppl[0]] = set(ppl[1:])
    
search = data[input()]

pplgo = []
for id in data:
    if search == data[id]:
        pass
    else:
        if search.intersection(data[id]) == set():
            pass
        else:
            pplgo.append(id)

if pplgo == []:
    print("Not Found")
else:
    for _ in pplgo:
        print(_)