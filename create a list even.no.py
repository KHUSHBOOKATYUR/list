
i=0
a=[]
even=0
while i<5:
    num=int(input("enter the number"))
    if num[i]%2==0:
        a.append(num[i])
        even=even+1
    
        print(a,"even no")
    i=i+1