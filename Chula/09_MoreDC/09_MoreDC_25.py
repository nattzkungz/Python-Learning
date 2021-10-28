def row_number(t, e):
    row_num = len(t)
    for i in range(row_num):
        if e in t[i]:
            return i

def flatten(t):
    flatted = []
    for i in t:
        for h in i:
            if h != 0:
                flatted.append(h)
    return flatted

def inversions(x):
    times = 0
    x_leng = len(x)
    for i in range(x_leng):
        for h in range(i, x_leng):
            if x[h] < x[i]: 
                times += 1
    return times

def solvable(t):
    num_of_rows = len(t)
    num_of_invse = inversions(flatten(t))
    zero_location = row_number(t, 0)
    if num_of_rows%2 == 1 and num_of_invse%2==0: 
        return True
    elif num_of_rows%2 == 0:
        if num_of_invse%2==0 and zero_location%2 == 1: 
            return True
        elif num_of_invse%2==1 and zero_location%2 == 0: 
            return True
        return False
    return False

exec(input().strip())