filename_year = input().split()
year_input = filename_year[1][-2:]

fileopen = open(filename_year[0], "rt")
all_std = []
for _ in fileopen.readlines():
    all_std.append(_.split())
DNE = False
score = []
std_year = []
for _ in all_std:
    std_year.append(_[0][:2])

for _ in all_std:
    if year_input in std_year:
        if _[0][:2] == year_input:
            score.append(float(_[1]))
    else:
        DNE = True



def average(a): return sum(a)/len(a)
if DNE:
    print("No Data")
else:
    print(min(score), max(score), average(score))
