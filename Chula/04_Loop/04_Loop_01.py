status = True
num_list = []

while status:
    num_input = input()
    if num_input == "q":
        status = False
    else:
        num_list.append(float(num_input))

if num_list == []:
    print("No Data")
else:
    print(round(sum(num_list)/len(num_list),2))