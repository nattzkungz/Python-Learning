def factor(N):
    k = 2
    used = []
    while N != 1:
        if N%k != 0:
            k += 1
        else:
            count = 0
            while N%k == 0:
                N = N//k
                count += 1
            used.append([k, count])
    return used

exec(input().strip())