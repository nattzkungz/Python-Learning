correspond_names = {}
number_of_names = int(input())

for _ in range(number_of_names):
    name_nick = input().split()
    correspond_names[name_nick[0]] = name_nick[1]

check_times = int(input())

rev_correspond_name = {}
for _ in correspond_names:
    rev_correspond_name[correspond_names[_]] = _

prnt = []
for _ in range(check_times):
    chk_this = input()
    if chk_this in correspond_names:
        prnt.append(correspond_names[chk_this])
    elif chk_this in rev_correspond_name:
        prnt.append(rev_correspond_name[chk_this])
    else: prnt.append("Not found")

for _ in prnt: print(_)
