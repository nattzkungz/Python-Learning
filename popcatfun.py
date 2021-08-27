a = input().split(" ")
aa = [float(_) for _ in a] #To change everything in the list to float
b = []
c = aa[0]
for _ in aa:
    if c < _:
        c = _
b.append(c)

for _ in aa:
    if c > _:
        c = _
b.append(c)        

for b in aa:
    aa.remove(b)

print(round((sum(aa)/2), 2))
print(aa)