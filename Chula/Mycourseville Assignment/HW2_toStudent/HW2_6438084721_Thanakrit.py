game_map = open("Chula/Mycourseville Assignment/HW2_toStudent/map.txt", "r")
map_to_list = []
count = -1
points = 0
collision = False
for _ in game_map.readlines():
    count += 1
    map_to_list.append(list(_.strip('\n')))

def getPos():
    return int(map_to_list[-1].index("A"))

def charAction(direction):
    global points
    global collision
    if direction == 'a':
        left = map_to_list[count-1][getPos() - 1]
        if left == 'o':
            points += 10
        elif left == 'x'
            collision = True
        map_to_list[count-1][getPos() - 1] = 'A'
    elif direction == 'd':
        right = map_to_list[count-1][getPos() + 1]
        if right == 'o':
            points += 10
        elif right == 'x':
            collision = True
        map_to_list[count-1][getPos() + 1] = 'A'
    else:
        middle = map_to_list[count-1][getPos()]
        if middle == 'o':
            points += 10
        map_to_list[count-1][getPos()] = 'A'

def delLines():
    lineLength = len(map_to_list) - 1
    for _ in range(lineLength):
        map_to_list[lineLength] = map_to_list[lineLength - 1]
        lineLength -= 1

def renderMap():
    for _ in map_to_list:
        print("".join(_))

gameStatus = True
# while gameStatus:
## Visual
for x in range (len(map_to_list)):
    print(map_to_list[x])
print(points)

while 