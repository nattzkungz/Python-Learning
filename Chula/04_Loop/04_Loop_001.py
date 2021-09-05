P = float(input())
k = 1
t = 1

while True:
    t = (t*(365-(k-1)))/365
    if 1 - t >= P:
        break
    else:
        k += 1

print(k)