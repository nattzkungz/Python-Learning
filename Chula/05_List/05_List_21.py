grades = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]

stds = []
status = True
while status:
    std = input()
    if std == "q":
        status = False
    else:
        # Take input as a string and split it into list
        stds.append(std.split())
#Nested list configuration
ids = []
std_grades = []
for _ in stds:
    ids.append(_[0])
    std_grades.append(_[1])

upgrade = [str(i) for i in input().split()]

for _ in upgrade:
    pos = ids.index(_) #
    this_std_grade_pos = std_grades[pos]
    grade_pos = grades.index(this_std_grade_pos)
    if std_grades[pos] != "A":
        std_grades[pos] = grades[grade_pos - 1]


for i in range(len(ids)):
    print(ids[i], std_grades[i])

