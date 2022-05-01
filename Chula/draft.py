<<<<<<< HEAD
def in_mall(malls):
    dup = {}
    mall_count = 0
    for i in malls:
        mall_count += 1
        for j in malls[i]:
            if j not in dup:
                dup[j] = 1
            else:
                dup[j] += 1

    e = []
    for h in dup:
        if dup[h] == mall_count:
            e.append(h)
    return e

def one_mall(malls):
    dup = {}
    mall_count = 0
    for i in malls:
        mall_count += 1
        for j in malls[i]:
            if j not in dup:
                dup[j] = 1
            else:
                dup[j] += 1
    
    e = []
    for h in dup:
        if dup[h] == 1:
            e.append(h)
    return e


hhh = {"a": {"s","g","b"}, "b": {"s","g","k","t","l"}, "c":{"s","g","b"}}
print(one_mall(hhh))



=======
# def prime(number):
#     is_prime = True
#     for i in range(2, number-1):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")

# number = int(input("check this number: ")
# prime(number)
>>>>>>> 61b14555f3d6e1c7cfcaf159f83f3e4998ddd840
