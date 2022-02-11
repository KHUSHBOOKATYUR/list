# i=0
# a=[]
# while i<20:
#     num=int(input("enter the number:-"))
#     a.append(num)
#     i=i+1
# print(a)
# k=0
# even=0
# odd=0
# posetive=0
# nagetive=0
# b=[]
# c=[]
# d=[]
# e=[]
# while k<len(a):
#     if a[k]%2==0:
#         b.append(a[k])
#         even=even+1
#     if a[k]%2!=0:
#         c.append(a[k])
#         odd=odd+1
#     if a[k]>0:
#         d.append(a[k])
#         posetive=posetive+1
#     elif a[k]<0:
#         e.append(a[k])
#         nagetive=nagetive+1
#     k=k+1
# print(b,"even")
# print(c,"odd")
# print(d,"posetive")
# print(e,"nagetive")







a=[1,2,-3,4,-5,-6,-7,-8,9,10,-11]
posetive=0
nagetive=0
d=[]
e=[]
k=0
while k<len(a):
    if a[k]>0:
        d.append(a[k])
        posetive=posetive+1
    elif a[k]<0:
        e.append(a[k])
        nagetive=nagetive+1
    k=k+1
print(d,"posetive")

