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
        ans2 = []
        for i in l:
            ans2.append(i*c)
        ans.append(ans2)

    return ans

def mult(A, B):
    result1 = []
    for f in A:
        res2 = []
        for g in range(len(B[0])):
            b_total = [i[g] for i in B]
            res2.append(sum(f[h]*b_total[h] for h in range(len(f))))
        result1.append(res2)

    return result1
                
exec(input().strip())