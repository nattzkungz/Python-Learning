array = "a b c"
pos = 0
count = 0
for i in array:
    pos = indexof(" ", pos) + 1
    if pos != -1:
        count += 1
    else:
        pass