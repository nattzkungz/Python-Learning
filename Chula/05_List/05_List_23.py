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
    data_list.append([pos, x, y, distance])

rearrange = []
for _ in data_list: rearrange.append(_[3])
rearrange.sort(reverse=False)
print(rearrange)
position = []
for _ in range(len(data_list)):
    pos = data_list[_].index(rearrange[_])
    pos_data = data_list.index(pos)
    print(data_list[_])
    # position.append(data_list[pos])
print(pos)
# print(position[2])