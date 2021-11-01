num_line = int(input())
win = []
lose = []
for _ in range(num_line):
    match = input().split()
    win.append(match[0]); lose.append(match[1])

never_lose = []
for _ in win:
    if _ not in lose and _ not in never_lose:
        never_lose.append(_)

print(sorted(never_lose))