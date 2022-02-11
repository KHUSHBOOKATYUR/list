num=[90,40,70,5,26,58,45]
a=0
i=0
while i<len(num):
    if num[i]>a:
        a=num[i]
    i=i+1
print(a)
i=0
b=0
while i<len(num):
    if num[i]>b:
        if num[i]!=a:
            b=num[i]
    i=i+1
print(b)
i=0
c=0
while i<len(num):
    if num[i]>c:
        if num[i]!=a and num[i]!=b:
            c=num[i]
    i=i+1
print(c)


# i=0
# while i<3:
#     a=int(input("enter the number-"))
#     b=int(input("enter the number"))
#     c=int(input("enter the number"))
#     if a>b or a>c:
#         print(a,"is greater than")
#     if b>a or b>c:
#         print(b,"is greater than") 
#     elif c>a or c>b:
#         print(c,"is greater than")
#     i=i+1


