import math

a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))

innersqrt = (b**2)-(4*a*c)
x_1 = (-b-math.sqrt(innersqrt))/(2*a)
x_2 = (-b+math.sqrt(innersqrt))/(2*a)

print(f"{round(x_1, 3)} {round(x_2, 3)}")