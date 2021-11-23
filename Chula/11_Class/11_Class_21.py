class Complex:

    def __init__(self, a, b):
        self.real_num = a
        self.imagi_num = b
        if self.imagi_num >= 0:
            self.operand = "+"
        else:
            self.operand = "-"

    def __str__(self):
        num_list = [str(self.real_num), self.operand ,str(self.imagi_num), "i"]
        if num_list[0] == "0":
            num_list.pop(0)
            if num_list[1] == "+":
                num_list.pop(0)
        if num_list[2] == "0":
            for x in range(3): num_list.pop(1)
        if num_list[2] == "1" or num_list[2] == "-1":
            num_list.pop(2)
        if num_list[1] == "1" or num_list[1] == "-1":
            num_list.pop(1)
        tmp = ""
        for g in num_list:
            tmp += g
        return tmp
    
    def __add__(self, rhs):
        self.real_num_result = self.real_num + rhs.real_num
        self.imagi_num_result = self.imagi_num + rhs.imagi_num
        if self.imagi_num_result < 0:
            operand = "-"
        else:
            operand = "+"
        return str(self.real_num_result)+operand+ str(self.imagi_num_result) +"i"

    def __mul__(self, rhs):
        self.real_num_result = (self.real_num*rhs.real_num) - (self.imagi_num*rhs.imagi_num)
        self.imagi_num_result = (self.real_num*rhs.imagi_num) + (self.imagi_num*rhs.real_num)
        if self.imagi_num_result < 0:
            operand = "-"
        else:
            operand = "+"
        return str(self.real_num_result)+operand+ str(self.imagi_num_result) +"i"
    
    def __truediv__(self, rhs):
        self.real_num_result = ((self.real_num*rhs.real_num) + (self.imagi_num*rhs.imagi_num)) / (self.imagi_num**2 + rhs.imagi_num**2)
        self.imagi_num_result = ((-self.real_num*rhs.imagi_num) + (self.imagi_num*rhs.real_num)) / (self.imagi_num**2 + rhs.imagi_num**2)
        if self.imagi_num_result < 0:
            operand = "-"
        else:
            operand = "+"
        return str(self.real_num_result)+operand+ str(self.imagi_num_result) +"i"



t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1: print(c1)
elif t==2: print(c2)
elif t==3: print(c1+c2)
elif t==4: print(c1*c2)
else:print(c1/c2)

