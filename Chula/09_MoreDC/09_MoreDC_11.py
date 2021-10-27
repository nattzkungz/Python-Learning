line_num = int(input())
process_this = []
for i in range(line_num):
    process_this.append([e for e in input()])

for i in process_this:
    if "." not in i or i[0] != ".":
        pass
    else:
        count_dot = 0
        for q in i:
            if q.isalpha() or q.isnumeric():
                break
            elif q == ".":
                count_dot += 1
        for x in range(count_dot//2):
            i.pop(0)

for g in process_this:
    print("".join(g))