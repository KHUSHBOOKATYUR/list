# list=['red','green','white','black','pink','yellow']
# i=0
# a=[]
# while i<len(list):
#     l=list[i]
#     a.append(l)
#     i=i+1
# print(a)
# a.remove('red')
# a.remove('pink')
# a.remove('yellow')
# print(a)


list=[1,2,3,[],7,[],9,[]]
i=0
a=[]
while i<len(list):
    l=list[i]
    a.append(l)
    i=i+1
# print(a)
a.remove([])
a.remove([])
a.remove([7])
print(a)


# list=[1,2,2,5,8,4,4,8]
# i=0
# a=[]
# while i<len(list):
#     l=list[i]
#     a.append(l)
#     i=i+1
# # print(a)
# a.remove(2)
# a.remove(8)
# a.remove(4)
# print(a)