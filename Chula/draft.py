filename_year = 
fileopen = open(filename_year[0], "rt")

all_std = []


year = filename_year[1][-2:]

score = []

for _ in all_std:
    if _[0][:2] == year:
        score.append(_[1])

print(min(score), max(score), sum(score)/len(score))