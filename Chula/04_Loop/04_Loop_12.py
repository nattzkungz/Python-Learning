int_list = []
num_pair = int(input())

for _ in range(num_pair):
    xy_input = [int(_) for _ in input().split(" ")]
    int_list.append(xy_input)

way = input()

red = []
blue = []

for _ in range(len(int_list)):
    if way == 'Zag-Zig':
        if _ % 2 != 0:
            red.append(int_list[_][0])
            blue.append(int_list[_][1])
        if _ % 2 == 0:
            blue.append(int_list[_][0])
            red.append(int_list[_][1])
    elif way == 'Zig-Zag':
        if _ % 2 != 0:
            blue.append(int_list[_][0])
            red.append(int_list[_][1])
        if _ % 2 == 0:
            blue.append(int_list[_][1])
            red.append(int_list[_][0])

print(str(min(red)) + " " + str(max(blue)))