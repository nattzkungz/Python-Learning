a = input().split(" ")
aa = [float(_) for _ in a]
b = []
c = aa[0]
for _ in aa:
    if c > _:
        b.append(_)
        c = _
    else:
        pass
print(b)