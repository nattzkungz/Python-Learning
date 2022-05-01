# # s= "Don't worry. Be happy."
# # print(s[6::-2])


# # a = "9876543210"
# # b = a[-2::-2]
# # print(b)

# # h = "123E-2"
# # expo = h.split("E")[1]
# # print(expo)

# # sentence = "This is a "
# # if sentence[0].upper():
# #     print("true")

# # for e in d:
# #     if e in p_number:
# #         count += 1


# # x = 75
# # if 50 <= x <= 100:
# #     print(True)
# # count = 0
# # for i in range(1,101,2):
# #     if i%3 == 0:
# #         count += 1

# # print(count)

# def f(x):
#     x = x*2
#     print("x in function", x)
#     return x

# x = 5
# f(x)
# print("x in main", x)


# x = [1,2,3,4,5,6,7]
# if i in range(len(x)):
#     if x[i]%2 == 0:
#         x.remove(i)

# print(x)


# a = int(input())
# value = 0
# for i in range(5):
#     print(i)
#     value += (((-1)**i)*((i+a)**3))/(2*a+1)

# print(value)


# data = [1,0,1,0]
# count = 0
# for i in data:
#     if i == 1:
#         count += 1

# if count%2 == 0:
#     data.append(0)
# else: 
#     data.append(1)


# hexa = input().upper()
# output = 0
# i = 0
# for c in hexa:
#     hex_list = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
#     length = len(hexa) - 1
#     value = hex_list.index(c)
#     output += value*(16**(length - i))
#     i += 1
        
# print(output)


h = int(input())
m = int(input())
delta_h = int(input())
delta_m = int(input())

new_h = h + delta_h
new_m = m + delta_m
if new_h >= 24:
    new_h = new_h - 24
elif new_h <= 0:
    new_h = 24-new_h

if new_m >= 60:
    new_h += 1
    new_m = new_m - 60
elif new_m < 0:
    new_h -= 1
    new_m = 60 - new_m

txt = "output: {:02d}:{:02d}".format(new_h, new_m)
print(txt)