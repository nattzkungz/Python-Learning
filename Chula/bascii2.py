#Question 2

#call file name
filename = ("pollutiondaily.txt")

def day_average(daylist):
    
#use split line function
    lines= open(filename).read().splitlines()
    
#use split coma function 
    scores= [x.split(",") for x in lines if x!=""]
    
#convert x into demical value 
    for x in scores:
        for i in range(len(x)):
            x[i]=float(x[i])
            
#display final average result
    for i in range(len(scores)):
        scores[i]= sum(scores[i])/len(scores[i])
    print("The daily averages are as follows: ")
    count = 0
    for x in scores:
        count += 1
        print("Day",count, "average: ", round(x,2))
        
        
day_average(filename)