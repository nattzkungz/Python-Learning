int_list = []
status = True
while status:
    xy_input = input()

    if xy_input == 'Zig-Zag' or xy_input == 'Zag-Zig':
        status = False
    else:
        int_list.append(xy_input.split())


red = []
blue = []

for _ in range(len(int_list)):
    if xy_input == 'Zig-Zag':
        if _ % 2 != 0:
            red.append(int_list[_][0])
        if _ % 2 == 0:
            blue.append(int_list[_][1])
    elif xy_input == 'Zag-Zig':
        if _ % 2 != 0:
            blue.append(int_list[_][0])
        if _ % 2 == 0:
            red.append(int_list[_][1])


printthis = ''
if xy_input == "Zig-Zag":
    printthis += str(max(red)) + ' ' + str(min(blue))
else:
    printthis += str(min(blue)) + ' ' + str(max(red))

print(printthis)