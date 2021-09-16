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
stds.sort(reverse=False) #Just sort it out first, no problem
ids = []
std_grades = []
for _ in stds: #Split the input into two list to work easier
    ids.append(_[0])
    std_grades.append(_[1])

upgrade = [str(i) for i in input().split()]

for _ in upgrade:
    pos = ids.index(_) #Find the id position in the list
    this_std_grade_pos = std_grades[pos] #id and grade should be in the same position, set this variable to use it later
    grade_pos = grades.index(this_std_grade_pos) #find the position of the grade in grade list
    if std_grades[pos] != "A": #If the student grade is not A
        std_grades[pos] = grades[grade_pos - 1] #then it should be upgraded

for i in range(len(ids)):
    print(ids[i], std_grades[i])

