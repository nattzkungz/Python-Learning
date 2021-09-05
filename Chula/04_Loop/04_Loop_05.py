findthis = input()
sentence = input()
word_count = 0

# countword = word.count(findthis)
delete = '",./;$%^&*()'
for _ in sentence:
    if _ in delete:
        sentence = sentence.replace(_, "")

split_value = []
tmp = ''
for c in sentence:
    if c == ' ':
        split_value.append(tmp)
        tmp = ''
    else:
        tmp += c
if tmp:
    split_value.append(tmp)

print(word_count)
print(sentence)
print(split_value)