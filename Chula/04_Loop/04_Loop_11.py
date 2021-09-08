str_input = input()

tmp = str_input[0]
count = 0
printthis = ''
for _ in range(len(str_input)):
    if str_input[_] == tmp:
        count += 1
        tmp = str_input[_]
    elif str_input[_] != tmp:
        printthis += tmp + ' ' + str(count) + ' '
        count = 1
        tmp = str_input[_]
    if _ == (len(str_input) - 1):
        printthis += tmp + ' ' + str(count)

print(printthis)