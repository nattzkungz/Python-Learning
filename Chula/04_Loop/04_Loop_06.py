height = int(input())
space = height
times = 0
spacee = 0
for _ in range(height-1):
    if _ == 0:
        print(" " * (height - 1) + "*")
    else:
        print(" " * (space-1) + "*" + " " * (spacee-2) + "*")
    space -= 1
    times += 1
    spacee = (2*times) + 1

print("*" * ((2*height)-1))