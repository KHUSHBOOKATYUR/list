
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