# a=[4,5,[6,7],8,9,[12,13]]
# i=0
# sum=0
# while i<len(a):
#     if type(a[i])==list:
#         j=0
#         while j<len(a[i]):
#             sum=sum+a[i][j]
#             j=j+1
#     else:
#         sum+=a[i]
#     i=i+1
# print(sum)








a=[[1,2,3],[4,5,6],8,7,9]
i=0
sum=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            sum=sum+a[i][j]
            j=j+1
    else:
        sum+=a[i]
    i=i+1
print(sum)

# A=2+5//2+9%5+2-9-3%2+5-9+8%4-3
# print(A)





a=[1,-2,-3,-4,5,-6,-7,-8,7,-8]
i=0
b=[]
while i<len(a):
    if a[i]<=0:
        b.append(0)
    else:
        b.append(a[i])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    i=i+1
print(b)



 