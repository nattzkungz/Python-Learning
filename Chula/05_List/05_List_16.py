n = int(input())
steps = []
while n != 1:
    steps.append(n)
    if n%2 == 0:
        n //= 2
    else:
        n = 3*n + 1
idk = []
# print(steps)
if len(steps) > 15:
    steps = steps[-14:]

tmp = ''
for _ in steps:
    tmp += str(_) + "->"

tmp += "1"

print(tmp)