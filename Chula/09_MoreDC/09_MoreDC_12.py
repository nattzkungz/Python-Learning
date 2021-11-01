num_lines = int(input())
if num_lines == 0:
    print("0")
    print("0")
else:
    data = []
    for x in range(num_lines):
        data.append(set(input().split()))
    union_data = data[0]
    intersect_data = data[0]
    for i in range(len(data)):
        union_data = union_data.union(data[i])
        intersect_data = intersect_data.intersection(data[i])
    print(len(union_data))
    print(len(intersect_data))