n = int(input())
first = []
for i in range(n):
    f_input = int(input())
    first.append(f_input)
second = [int(_) for _ in input().split()]

status = True

third = []
while status:
    third_input = int(input())
    if third_input == -1:
        status = False
    else:
        third.append(third_input)

added = third[::-1] + second[::-1] + first[::-1]

even = []
odd = []
for i in range(len(added)):
    if i % 2 == 0:
        even.append(added[i])
    else:
        odd.append(added[i])

even += odd[::-1]

print(even)