int_input = [int(i) for i in input().split()]
int_input.sort(reverse=False)
print(int_input)
duplicate = []
tmp = ''
diff_value = []
for _ in int_input:
    if tmp == _:
        duplicate.append(_)
    else:
        tmp = _
        diff_value.append(_)
diff_value.sort(reverse=False)
diff_count = len(diff_value)
print(diff_count)
print(diff_value[0:10])

