maps = {
    "A":{"K":3,"J":7},
    "B":{"C":1,"F":7},
    "C":{"B":1,"D":2,"G":6},
    "D":{"C":2,"J":8},
    "E":{"F":1},
    "F":{"B":7,"H":4,"E":1},
    "G":{"K":5,"I":3,"C":6},
    "H":{"K":5,"I":2,"F":4},
    "I":{"H":2,"G":3},
    "J":{"A":7,"D":8},
    "K":{"A":3,"G":5,"H":5},
}

def route_disp(route):
    route_taken_s = ""
    for place in range(len(route)):
        if place == 0:
            route_taken_s = route[place]
        else:
            route_taken_s += " >> " + route[place]
    return route_taken_s


def avbl_route(current_pos):
    route_avbl = []
    for route in maps[current_pos]:
        route_avbl.append([route, maps[current_pos][route]])
    return route_avbl


def finished(status):
    if status == True:
        print("\nCONGRATULATIONS!! YOU REACHED THE DESTINATION\n")
    else:
        print("\nOUT OF STAMINA. BETTER LUCK NEXT TIME\n")


def check_finished(stamina, current_pos):
    if stamina >= 0 and current_pos == "E":
        return True
    elif stamina <= 0:
        return False


def finished_screen(stamina, path):
    print(f"Your stamina is {stamina}")
    print(f"You have travelled : {path}")


current_pos = "A"
count, cost, stamina = 0, 0, 25
route_taken = [current_pos]
print("Game has started.......................")
print("You have a full stamina of 25 .........")
while True:
    if check_finished(stamina, current_pos) is True:
        print(f"Your current Stamina is : {str(stamina)} You have used up {cost} from the total stamina")
        finished(True)
        finished_screen(stamina, route_disp(route_taken))
        break
    elif check_finished(stamina, current_pos) is False:
        finished(False)
        finished_screen(stamina, route_disp(route_taken))
        break
    if count > 0:
        print(f"Your current Stamina is : {str(stamina)} You have used up {cost} from the total stamina")
        print(f"Your current route is : {route_disp(route_taken)}")
    print(f"You are currently at : {current_pos}")
    print("Choose your destination................")
    avbl_way = avbl_route(current_pos)
    path_avbl, path_cost = [path[0] for path in avbl_way], [path[1] for path in avbl_way]
    for route in avbl_way:
        print(f"{route[0]}: {route[1]}")
    found = False
    while found == False:
        next_pos = input()
        if next_pos in path_avbl:
            cost = path_cost[path_avbl.index(next_pos)]
            if stamina - cost > 0:
                route_taken.append(next_pos)
            stamina -= cost
            current_pos = next_pos
            found = True
        else:
            print("Invalid Input!!! Choose your next destination")
    count += 1
