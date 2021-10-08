original = input().lower()
anagram = input().lower()
countOriginal = {}
countAnagram = {}
for _ in original:
    if _ == ' ':
        pass
    else:
        if _ not in countOriginal:
            countOriginal[_] = 1
        else:
            countOriginal[_] += 1
for _ in anagram:
    if _ == ' ':
        pass
    else:
        if _ not in countAnagram:
            countAnagram[_] = 1
        else:
            countAnagram[_] += 1

if countOriginal == countAnagram:
    print("YES")
else:
    print("NO")
print(countAnagram)
print(countOriginal)