# import math

# L = 0
# a = float(input())
# U = a

# x = (U + L) / 2

# while abs(a - (x**2)) <= (10**-10)*max(a,x**2):
#     if x**2 > a:
#         U = a
#     else:
#         L = x
#     x = (U + L) / 2

# print(x)




L = 0
a = float(input())
U = a
x = (L + U) / 2
while abs(a-10**x) > 10**(-10)*max(a,10**x) :
    if 10**x > a : U = x
    elif 10**x < a : L = x
    x = (L + U) / 2 
print(round(x,6))