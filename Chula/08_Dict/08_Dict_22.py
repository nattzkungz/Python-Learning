menu = {}
num_menu = int(input())
for _ in range(num_menu):
    add_menu = input().split()
    menu[add_menu[0]] = float(add_menu[1])

sold_list = {}
num_menu_sold = int(input())
for _ in range(num_menu_sold):
    sold = input().split()
    if sold[0] in sold_list:
        sold_list[sold[0]] += int(sold[1])*menu[sold[0]]
    elif sold[0] in menu:
        sold_list[sold[0]] = int(sold[1])*menu[sold[0]]

total_sales = 0
for _ in sold_list:
    total_sales += float(sold_list[_])

if bool(sold_list):
    top_sales = []
    top_item = max(sold_list, key=sold_list.get)
    top_sales.append(top_item)
    for _ in sold_list:
        if int(sold_list[_]) == sold_list[top_item] and _ != top_item:
            top_sales.append(_)
    rearranged_top_sales = sorted(top_sales)
    print("Total ice cream sales: " + str(total_sales))
    print("Top sales: " + ", ".join(rearranged_top_sales))
else:
    print("No ice cream sales")