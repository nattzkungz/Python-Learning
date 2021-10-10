highscore_file = open("Chula/Mycourseville Assignment/HW2_toStudent/highscore.txt")
map_to_list = [list(_.strip("\n")) for _ in open("Chula/Mycourseville Assignment/HW2_toStudent/map.txt", "rt").readlines()]
points = 0
collision = False
finished = False
count = len(map_to_list) - 1

def getPos(): return int(map_to_list[-1].index("A"))


def renderMap():
    for _ in map_to_list: 
        print("".join(_))


def charAction(direction):
    global points, collision, finished
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
        if _ == len(map_to_list) - 1:
            map_to_list.pop(-1)
            map_to_list.insert(0, map_to_list[0])
        else:
            map_to_list[lineLength] = map_to_list[lineLength - 1]
        lineLength -= 1


def highscoreDisplay():
    print("High Scores:")
    highscoreDisp = open("Chula/Mycourseville Assignment/HW2_toStudent/highscore.txt")
    for x in range(3):
        print(highscoreDisp.readline().strip("\n"))


def highscoreHandler(score):
    currentHigh = []
    temp = open("Chula/Mycourseville Assignment/HW2_toStudent/highscore_cache.txt", "w")
    for x in highscore_file.readlines():
        currentHigh.append(x.strip("\n").split(","))
    highscore_file.close()
    for _ in range(len(currentHigh)):
        if score >= int(currentHigh[_][1]):
            name = input("Enter Your Name: ")
            if name > currentHigh[_][0]: shift_amt = 0
            elif name < currentHigh[_][0]: shift_amt = 1
            else: shift_amt = 0
            currentHigh.insert(_ + shift_amt, [name,score])
            currentHigh.pop(-1)
            for e in currentHigh:
                temp.write(e[0] + "," + str(e[1]) + "\n")
            return True


def transferData():
    import os
    os.remove("Chula/Mycourseville Assignment/HW2_toStudent/highscore.txt")
    toThis = open("Chula/Mycourseville Assignment/HW2_toStudent/highscore.txt", "w")
    fromThis = open("Chula/Mycourseville Assignment/HW2_toStudent/highscore_cache.txt")
    for _ in fromThis:
        toThis.write(_)
    toThis.close()
    fromThis.close()
    os.remove("Chula/Mycourseville Assignment/HW2_toStudent/highscore_cache.txt")


while True:
    if collision or finished:
        renderMap()
        if collision: print("-"*15+"\n---GAME OVER---\n"+"-"*15)
        elif finished: print("-"*14+"\n---CONGRATS---\n"+"-"*14)
        if highscoreHandler(points):
            transferData()
        highscoreDisplay()
        break
    else:
        renderMap()
        charAction(input().lower())
        delLines()
