import numpy as np
listlines = []
file = open('Chula/Mycourseville Assignment/HW4_Students (Shared)/scores_utf8.csv','r')

for line in file :
    lines = line.strip().split(',')
    listlines.append(lines)

oldarraylines = np.array(listlines)
arraylines = np.delete(oldarraylines,0,0)
nonamearray = np.delete(arraylines, 0,1)

sumscores = np.sum(nonamearray)
print(sumscores)