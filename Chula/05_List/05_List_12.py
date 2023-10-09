fullname = ["Robert", "William" , "James" , "John" ,"Margaret" , "Edward" , "Sarah" , "Andrew" , "Anthony" , "Deborah"]
nickname = ["Dick","Bill","Jim","Jack", "Peggy","Ed","Sally","Andy","Tony","Debbie",]

times = int(input())

for _ in range (times):
    name = input()
    if name in fullname:
        print(nickname[fullname.index(name)])
    elif name in nickname:
        print(fullname[nickname.index(name)])
    else:
        print("Not found")
