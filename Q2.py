l1 = []
l2 = []
a = 0
n = int(input("enter size of elements for 1st list: "))
for i in range(0,n):
    elem = input("enter the element: ")
    l1.append(elem)
m = int(input("enter size of elements for 2nd list: "))
for i in range(0,m):
    elem = input("enter the element: ")
    l2.append(elem)
for x in l1:
    for y in l2:
        if x==y:
            a = a+1
if (a==0):
    print("False")
else:
    print("True")
