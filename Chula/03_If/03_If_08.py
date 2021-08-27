dd = int(input())
mm = int(input())
yy = int(input())
yy1 = yy - 543

day_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def leap_calc():
    div4 = yy1 % 4
    div100 = yy1 % 100
    div400 = yy1 % 400

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

day = sum(day_in_months[0:mm-1]) + dd

if leap_calc():
    day += 1

print(day)