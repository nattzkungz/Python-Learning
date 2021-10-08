game_map = open("Chula/Mycourseville Assignment/HW2_toStudent/map.txt", "r")
map_to_list = []
count = -1
points = 0
collision = False
finished = False
for _ in game_map.readlines():
    count += 1
    map_to_list.append(list(_.strip('\n')))
times = count


def getPos(): return int(map_to_list[-1].index("A"))


def renderMap(): 
    for _ in map_to_list: 
        print("".join(_))

def charAction(direction):
    global points
    global collision
    global finished
    num = 0
    if direction == 'a': num = -1
    elif direction == 'd': num = 1
    else: num = 0

    nextPos = map_to_list[count-1][getPos() + num]
    if nextPos == 'o':
        points += 10
    map_to_list[count-1][getPos() + num] = 'A'
    if nextPos == 'x':
        map_to_list[count-1][getPos() + num] = '*'
        collision = True
    if nextPos == 'f':
        finished = True


def delLines():
    lineLength = len(map_to_list) - 1
    for _ in range(lineLength):
        map_to_list[lineLength] = map_to_list[lineLength - 1]
        lineLength -= 1


def highscoreDisplay():
    print("**Highscores**")
    for x in range(3):
        print(highscore_file.readline().strip("\n"))
    

def highscoreHandler(name, score):
    highscore_file = open("Chula/Mycourseville Assignment/HW2_toStudent/highscore.txt", "rt")
    currentHigh = []
    for x in highscore_file.readlines():
        currentHigh.append(x.strip("\n").split(","))
        
gameStatus = True

while gameStatus:
    times -= 1
    if collision or finished:
        renderMap()
        if collision:
            print("---------------\n---------------\n---GAME OVER---\n---------------\n---------------")
        elif finished:
            print("--------------\n--------------\n---CONGRATS---\n--------------\n--------------")
        highscoreDisplay()
        gameStatus = False
    else:
        renderMap()
        charAction(input().lower())
        delLines()


# if gameStatus == False:

#     if finished and points > 0:
#         name = input("Type your name here: ")
#     if collision and points > 0:
#         name = input("Type your name here: ")