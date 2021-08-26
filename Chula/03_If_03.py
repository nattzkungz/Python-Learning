a = input().split(" ")
aa = [float(_) for _ in a]
b = []
c = aa[0]
d = c
for _ in aa:
    if c < _:
        b.append(_)
        c = _
        
print(b)

print(round((sum(b)/2), 2))