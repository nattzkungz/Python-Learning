d,m,y = [int(_) for _ in input().split()]

def leap_calc():
    div4 = y % 4
    div100 = y % 100
    div400 = y % 400

    if div4 == 0:
        if div100 == 0:
            if div400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

y -= 543
day_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = 0
if day_in_months[m-1] == 30:
    n = 30
else:
    if m == 2:
        if leap_calc():
            n = 29
        else:
            n = 28
    else:
        n = 31
    
d = d + 15

if d > n:
    d -= n
    m += 1
if m > 12:
    m -= 12
    y += 1

y += 543
print(str(d) + "/" + str(m)+ "/"+ str(y))