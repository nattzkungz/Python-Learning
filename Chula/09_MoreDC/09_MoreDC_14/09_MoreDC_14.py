courses = [tuple(_.strip("\n").split(",")) for _ in open("Chula/09_MoreDC/09_MoreDC_14/courses.txt").readlines()]
teachers = [tuple(_.strip("\n").split(",")) for _ in open("Chula/09_MoreDC/09_MoreDC_14/teachers.txt").readlines()]
database = [tuple(_.strip("\n").split(",")) for _ in open("Chula/09_MoreDC/09_MoreDC_14/database.txt").readlines()]

matched = []
c_list = [g[0] for g in courses]
t_list = [g[0] for g in teachers]
for _ in database:
    temp = []
    course = _[0]; teacher = _[1]
    if course not in c_list or teacher not in t_list:
        matched.append("record error")
    else:
        for i in courses:
            for j in teachers:
                if i[0] == course and j[0] == teacher:
                    matched.append([i[1], j[1]])

tmp = ""
for _ in matched:
    if isinstance(_, list):
        tmp += _[0] + "," + _[1]
    else:
        tmp += _
    if matched.index(_) != len(matched)-1:
        tmp += "\n"

print(tmp)