# a = [int(e, 2) for e in input().split()]

# b = sum(a)
# print(b)
# print(bin(b)[2:])

# Or use this

# print(bin(sum([int(i, 2) for i in input().split()]))[2:])

number = input()


base10 = int(number, base=10)
# binary = int(number, base=2)
bin_function = bin(int(number))

print(base10, bin_function)