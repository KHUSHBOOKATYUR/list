# a=[34,89,78,834,5,6,7,8,9,10,1]
# d=1
# i=0
# p=1
# while i<len(a):
#     if a[i]>d:
#         d=a[i]
#     elif a[i]<p:
#         p=a[i]
#     i=i+1
# print(d)
# print(p)

a=[[3,4],[9,8,7,8],[8,9,7,6],[9,8,7]]
d=1
p=1
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if (a[i],a[j])>d:
            d=a[i],a[j]
        elif a[i],a[j]<p:
            p=a[i],a[j]
            j=j+1
        i=i+1
print(d)
print(p)
