def splitl(word):
    return [str(char) for char in word]

right_ans = splitl(input().lower())
score = 0
std_ans = splitl(input().lower())

if len(right_ans) != len(std_ans):
    print("Incomplete answer")
else:
    for i in range(len(right_ans)):
        if right_ans[i] == std_ans[i]:
            score += 1
    print(score)
