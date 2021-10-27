def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c, A):
    ans = []
    for l in A:
        for i in l:
            ans.append([i*c])
    return ans

def mult(A, B):
    result = []
    p = len(A)
    for x in range(p):
        for h in B
            for g in A:

    return result
                
print(mult(read_matrix(), read_matrix()))