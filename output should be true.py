a=["python",2,2.0 ,True]
i=0
b=[]
while i<len(a):
    if type(a[i])==str:
        b.append(a[i])
    i=i+1
print(b)


# a=input("enter the anything-")
# i=0
# while i<1:        
#     if "." in a:
#         print(b,"it is float value")
#     elif "+" and "j" in a:
#         print("it is complex value")
#     elif a=="0" or "9":
#         print("it is int value")
#     else :
#         print("it is string value")
#     i=i+1
