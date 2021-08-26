import math

weight = int(input("Enmter your weight: "))
height = int(input("Enmter your height: "))

mosteller = (math.sqrt(weight*height))/60
haycock = 0.024265 * (weight**0.5378) * (height**0.3964)

boyd_weight = weight**(0.6157-(0.0188 * math.log(weight, 10)))
boyd = 0.0333 * boyd_weight * (height**0.3)

print(mosteller)
print(haycock)
print(boyd)