import math

n = int(input("A number"))

print(math.sqrt(2*(math.pi)) * n**(n+1/2) * math.e**(-n + 1/((12*n)+1)))
print(math.sqrt(2*(math.pi)) * n**(n+1/2) * math.e**(-n + 1/((12*n))))