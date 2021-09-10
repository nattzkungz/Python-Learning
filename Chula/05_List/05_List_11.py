num = ["0","1","2","3","4","5","6","7","8","9"]

str_input = input()

no_in_str = []

for _ in str_input:
    if _.isdigit():
        no_in_str.append(_)

for _ in no_in_str:
    if _ in num:
        num.remove(_)

if len(num) > 0:
    print(",".join(num))
else:
    print("None")
