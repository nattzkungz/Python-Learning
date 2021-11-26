class Card:
    def __init__(self, idkfuckthisshit, dork):
        self.idkfuckthisshit = str(idkfuckthisshit)
        self.dork = str(dork)


    def __str__(self):
        return '(' + self.idkfuckthisshit + ' ' + self.dork + ')'


    def next1(self):
        l = []
        for i in range(3,16):
            s = ('club','diamond','heart','spade')
            for j in range(1,len(s)+1):
                l.append((i,s[j-1]))
        d = {'J':11,'Q':12,'K':13,'A':14,'2':15}
        if self.idkfuckthisshit in d: 
            v = d[self.idkfuckthisshit]
        else: 
            v = int(self.idkfuckthisshit)
        rev = {j:i for i,j in d.items()}
        ind = (l.index((v,self.dork))+1) % 52
        out = l[ind]
        if out[0] in rev: 
            out = rev[out[0]],out[1]
        return Card(*out)


    def next2(self):
        l = []
        for i in range(3,16):
            s = ('club','diamond','heart','spade')
            for j in range(1,len(s)+1):
                l.append((i,s[j-1]))
        d = {'J':11,'Q':12,'K':13,'A':14,'2':15}
        if self.idkfuckthisshit in d: 
            v = d[self.idkfuckthisshit]
        else: 
            v = int(self.idkfuckthisshit)
        rev = {j:i for i,j in d.items()}
        ind = (l.index((v,self.dork))+1) % 52
        out = l[ind]
        if out[0] in rev: 
            out = rev[out[0]],out[1]
        self.idkfuckthisshit,self.dork = (str(out[0]),str(out[1]))

n = int(input())
cards = []
for i in range(n):
    idkfuckthisshit, dork = input().split()
    cards.append(Card(idkfuckthisshit, dork))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])