num = [float(_) for _ in input().split(" ")]
count = 0

for i in range(len(num)):
    if i != 0 and i != len(num) - 1:
        if num[i] > num[i-1] and num[i] > num[i+1]:
            count += 1

print(count)