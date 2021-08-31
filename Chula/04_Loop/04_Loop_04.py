str_input = input()
no = False
for _ in str_input:
    if _ == "(":
        str_input.replace("(", "[")
    elif _ == "[":
        str_input.replace("[", "(")
    elif _ == ")":
        str_input.replace(")", "]")
    elif _ == "]":
        str_input.replace("]", ")")
    # else:
    #     no = True


print(str_input)