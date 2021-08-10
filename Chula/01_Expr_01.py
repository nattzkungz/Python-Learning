import math

n = int(input("A number"))

lower_bound = math.sqrt(2*(math.pi)) * n**(n+1/2) * math.e**(-n + 1/((12*n)+1))
upper_bound = math.sqrt(2*(math.pi)) * n**(n+1/2) * math.e**(-n + 1/((12*n)))
print(lower_bound)
print(upper_bound)