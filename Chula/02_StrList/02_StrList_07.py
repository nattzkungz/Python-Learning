a = input()
a1 = a[3] + a[10] + a[17] + a[24] + a[31]
a2 = a[7] + a[12] + a[17] + a[22] + a[27]
c = int(a1) + int(a2) + 10000
d11 = str(c)
d12 = d11[-4:-1]
d21 = str(d12)
d22 = []
for _ in d21: d22.append(int(_))
d23 = sum(d22)
d24 = str(d23)
d25 = []
for _ in d24: d25.append(int(_))
d26 = sum(d25)
print(d26)
listsss = ["a", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(d12 + listsss[d26-1].upper())