a = [1,2,3,4,5]

for _ in range(len(a)-1):
    d = a[_]
    a[_ + 1] = a[_+2]
print(a)