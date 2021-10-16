phonebook = {}
num_of_ppl = int(input())

for _ in range(num_of_ppl):
    name_tel = input().split()
    tel_no = name_tel[2]
    name = name_tel[0] + " " + name_tel[1]
    phonebook[name] = tel_no

check_times = int(input())

rev_phonebook = {}
for _ in phonebook:
    rev_phonebook[phonebook[_]] = _

prnt = []
for _ in range(check_times):
    chk_this = input()
    if chk_this in phonebook:
        prnt.append(str(chk_this) + " --> " +phonebook[chk_this])
    elif chk_this in rev_phonebook:
        prnt.append(str(chk_this) + " --> " +str(rev_phonebook[chk_this]))
    else: prnt.append(str(chk_this) + " --> " +"Not found")

for _ in prnt: print(_)
