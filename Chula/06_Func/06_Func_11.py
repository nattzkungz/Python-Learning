a = [int(e, 2) for e in input().split()]

b = sum(a)

print(bin(b)[2:])