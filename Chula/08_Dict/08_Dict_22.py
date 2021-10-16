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
        sold_list[sold[0]] += sold[1]
    elif sold[0] in menu:
        sold_list[sold[0]] = sold[1]

total_sales = 0
for _ in sold_list:
    total_sales += float(sold_list[_]) * menu[_]

top_sales = []
for _ in sold_list:
    if int(sold_list[_]) > 10:
        top_sales.append(_)
rearranged_top_sales = sorted(top_sales)
tmp = ""
for _ in rearranged_top_sales:
    tmp += _ + ", "

if bool(sold_list):
    print("Total ice cream sales: " + str(total_sales))
    print("Top sales: " + tmp)
else:
    print("No ice cream sales")