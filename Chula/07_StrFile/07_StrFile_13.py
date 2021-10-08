unwanted = '><.)(*&^%$#@!:;" '
text = input()
textList = []
nestedList = []
znestedList = []
for _ in text:
    if _ in unwanted:
        textList.append(" ")
    else:
        textList.append(_)
tmp = ''
for _ in textList:
    for x in _:
        tmp += x

znestedList.append(tmp.split())
for _ in znestedList:
    nestedList.append(list(_))

for _ in range(len(nestedList)):
    if _ == 0:
        nestedList[0][0] = nestedList[0][0].lower()
    else:
        nestedList[_][0] = nestedList[_][0].upper()
print(nestedList)
zzz = ''
for _ in nestedList:
    for x in _:
        zzz += x
print(zzz)
