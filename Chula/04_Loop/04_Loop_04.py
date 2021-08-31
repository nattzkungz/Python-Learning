str_input = input()
a_list = []
for i in str_input:
    a_list.append(i)

for i in range(len(a_list)):
    if a_list[i] == "[":
        a_list[i] = "("
    elif a_list[i] == "(":
        a_list[i] = "["
    elif a_list[i] == "]":
        a_list[i] = ")"
    elif a_list[i] == ")":
        a_list[i] = "]"

string = ""
for i in a_list:
    string += i

print(string)
print(''.join(a_list))