'''5
CP 1
ME 2
PE 1
CHE 1
MT 3
6
59301234521 23.6 PE CP MT CHE
59300799921 44.5 ME CP CHE PE
59300081621 37 PE CHE MT CP
59300653521 61.2 PE MT CP ME
59300002121 19.4 CHE CP ME CP
59300048721 7 ME CP CHE MT'''

n = int(input())
dept = {}
for i in range(n):
    s = input().split()
    dept[s[0]] = int(s[1])

pref = {}
ns = int(input())
for i in range(ns):
    pf_d = input().split()
    pref[pf_d[0]] = pf_d[1:]
sorted_pref = sorted(pref, key=pref.get, reverse=True)

print(sorted_pref)

success = []
for i in sorted_pref:
    for x in range(1, len(i[1])-1):
        h = i[1][x]
        if dept[h] > 0:
            success.append([i[0], h])
            dept[h] -= 1
            break

for i in success:
    print(i[0], i[1])
