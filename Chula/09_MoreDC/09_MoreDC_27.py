def knows(R, x, y):
    if y in R[x]:
        return True
    else:
        return False

def is_celeb(R, x):
    for key,i in R.items() :
        if x not in i and key != x: 
            return False
    if len(R[x]) == 1 and x in R[x]: 
        return True
    if len(R[x]) > 0 : return False
    return True

def find_celeb(R):
    for ppl in R:
        if is_celeb(R, ppl):
            return ppl
    return None

def read_relations():
    R = dict()
    while True:
        s = input()
        if s == "q":
            return R
        else:
            d = s.split()
            if len(d) == 1: break
            else:
                if d[0] in R:
                    R[d[0]].add(d[1])
                elif d[1] not in R:
                    R[d[1]] = set(d[1])
                else:
                    R[d[0]] = set(d[1])
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print("Not Found")
    else:
        print(c)

exec(input().strip())
