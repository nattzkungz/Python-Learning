class Complex:

    def __init__(self, a, b):
        self.real_num = a
        self.imagi_num = b
        if self.imagi_num >= 0:
            self.operand = "+"
        else:
            self.operand = "-"

    def __str__(self):
        if self.imagi_num == 0:
            return str(self.real_num)
        elif self.imagi_num == 1 or self.imagi_num == -1:
            if self.real_num == 0:
                if self.imagi_num > 0:
                    return "i"
                return str(self.operand) + "i"
            return str(self.real_num) + self.operand + "i"
        elif self.real_num == 0:
            return str(self.imagi_num) + "i"
        else:
            if self.imagi_num < 0:
                self.operand = ""
            return str(self.real_num) + self.operand + str(self.imagi_num) + "i" 
    
    def __add__(self, rhs):
        self.real_num_result = self.real_num + rhs.real_num
        self.imagi_num_result = self.imagi_num + rhs.imagi_num
        return Complex(self.real_num_result, self.imagi_num_result)

    def __mul__(self, rhs):
        self.real_num_result = (self.real_num*rhs.real_num) - (self.imagi_num*rhs.imagi_num)
        self.imagi_num_result = (self.real_num*rhs.imagi_num) + (self.imagi_num*rhs.real_num)
        return Complex(self.real_num_result, self.imagi_num_result)
    
    def __truediv__(self, rhs):
        self.real_num_result = ((self.real_num*rhs.real_num) + (self.imagi_num*rhs.imagi_num)) / (rhs.real_num**2 + rhs.imagi_num**2)
        self.imagi_num_result = ((-self.real_num*rhs.imagi_num) + (self.imagi_num*rhs.real_num)) / (rhs.real_num**2 + rhs.imagi_num**2)
        return Complex(self.real_num_result, self.imagi_num_result)



t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1: print(c1)
elif t==2: print(c2)
elif t==3: print(c1+c2)
elif t==4: print(c1*c2)
else:print(c1/c2)