    if i == len(num):
        if num[i] > num[i-1]:
            count += 1
    elif i == 0:
        if num[i] > num[i-1]:
            count += 1
    else: