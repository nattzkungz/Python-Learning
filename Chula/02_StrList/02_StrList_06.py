a = input()[1:-1].split(", ")
al = [float(_) for _ in a]
b = input()[1:-1].split(", ")
bl = [float(_) for _ in b]
print(al,'+',bl,'=',[al[0]+bl[0],al[1]+bl[1],al[2]+bl[2]])