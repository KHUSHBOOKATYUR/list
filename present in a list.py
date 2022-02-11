i=0
a=[]
while i<10:
    num=int(input("enter the number-:"))
    a.append(num)
    i=i+1
print(a)
k=0
n=int(input("enter the number-"))
while k<len(a):
    if a[k]==n:
        print(n,"it is present in list")
    k=k+1  

# i=0
# a=[]
# count=0
# while i<10:
#     num=input("enter the number-:")
#     a.append(num)
#     i=i+1
#     if num==a:
#         print(num,"it is a present")
#         count=coun+1
