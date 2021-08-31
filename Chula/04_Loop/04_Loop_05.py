word = input()
sentence = input().split(" ")
count = 0
for _ in sentence:
    if _ == word:
        count += 1

print(count)