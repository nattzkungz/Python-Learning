import math
num_of_points = int(input())

point_list = []
for i in range(num_of_points): point_list.append(input().split())

data_list = []
for _ in point_list:
    x = float(_[0])
    y = float(_[1])
    distance = math.sqrt(x**2 + y**2)
    pos = point_list.index(_) + 1
    data_list.append([distance, pos, x, y])
data_list.sort(reverse=False)

print("#" + str(data_list[2][1]) + ":" +"("+ str(data_list[2][2]) + ", " + str(data_list[2][3]) + ")")