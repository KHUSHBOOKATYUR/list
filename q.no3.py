# places=["delhi" ,"gujrat", "rajasthan", "punjab", "kerala"]
# i=0
# while i<len(places):
#     print(places[-1-i])
#     i=i+1

# list1=[1,2,3,4,5,6,7,8]
# i=0
# while i<len(list1):
#     print(list1[-1-i])
#     i=i+1


a=[25,257,8876,85,65]
i=0
c=[]
while i<len(a):
    sum=0
    while a[i]>0:
        sum=sum+(a[i]%10)
        a[i]//=10
    c.append(sum)
    i+=1
print(c)





