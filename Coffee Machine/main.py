from menu import MENU as menu

machineStatus = True
water = 300
milk = 200
coffee = 100
money = 0


def resource_checker(menu_selection):
    global water, milk, coffee
    water_used = int(menu[menu_selection]["ingredients"]["water"])
    coffee_used = int(menu[menu_selection]["ingredients"]["coffee"])
    if water - water_used >= 0 and coffee - coffee_used >= 0:
        if "milk" in menu[menu_selection]["ingredients"]:
            milk_used = int(menu[menu_selection]["ingredients"]["milk"])
            if milk - milk_used >= 0:
                return True
            else:
                print("Not enough milk")
                return False
        else:
            return True
    else:
        print("Not enough ingredient")
        return False


def resources_manager(menu_selection):
    global water, milk, coffee
    water -= int(menu[menu_selection]["ingredients"]["water"])
    coffee -= int(menu[menu_selection]["ingredients"]["coffee"])
    if "milk" in menu[menu_selection]["ingredients"]:
        milk -= int(menu[menu_selection]["ingredients"]["milk"])


def cashier(menu_selection):
    global money
    menu_cost = int(menu[menu_selection]["cost"])
    print("Please insert coin")
    b1 = int(input("1 Baht: "))
    b2 = int(input("2 Baht: "))
    b5 = int(input("5 Baht: "))
    b10 = int(input("10 Baht: "))
    total_money = b1 + (b2 * 2) + (b5 * 5) + (b10 * 10)
    print(f"Total inserted money is {total_money} Baht")
    if total_money < menu_cost:
        return False
    else:
        change = total_money - menu_cost
        print(f"Your change is {change} Baht")
        money += menu_cost
        return True


while machineStatus:
    usr_prompt = input("What would you like? (espresso/latte/cappuccino): ")
    if usr_prompt == 'report':
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nMoney: {money}")
    elif usr_prompt == 'off':
        machineStatus = False
    else:
        if resource_checker(usr_prompt):
            if cashier(usr_prompt):
                resources_manager(usr_prompt)
                print(f"Heres your {usr_prompt}")
            else:
                print("Not enough money, money refunded")
        else:
            print("Not enough resources")
