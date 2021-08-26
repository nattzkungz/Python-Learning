a = input()
b = int(input())

if b > len(a):
    c = b - len(a)
    print("0"*c + a)
else:
    print(a)