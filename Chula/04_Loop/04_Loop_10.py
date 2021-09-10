import math

L = 0
a = float(input())
U = a

num_U = 0

while U != 0: 
    U = U//10
    num_U += 1

U = num_U

x = (U + L) / 2


while abs(a-(10**x)) > (10**(-10))*max(a,10**x):
    if 10**x > a: 
        U = x
    else:
        L = x
    x = (U + L) / 2
    
print(round(x,6))

