d1ct = {}
str_input = input().lower()
for _ in str_input:
    if _.isalpha(): 
        if _ in d1ct:
            d1ct[_] += 1
        else:
            d1ct[_] = 1

l1st = [[-d1ct[i], i] for i in d1ct]

z = sorted(l1st)

for _ in z: print(_[1] + " -> " + str(-(_[0])))