num=int(input("enter the number-:"))                         
count=0
a=[]
i=1
while  i<=num:
    # num=int(input("enter the number-:"))
    if (num%i==0):
            count=count+1
    i=i+1
if (count==2):
        # a.append(num[i])
    print("it is a prime no.")   
else:
    print("it is not prime number")