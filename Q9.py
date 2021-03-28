l1 = []
n = int(input("Enter the no. of elements to enter in List:  "))
for i in range(n):
    elements = input("enter the element: ")
    l1.append(elements)
print(l1)
p = int(input("Enter the nth element: "))
print([l1[i::p]for i in range(p)])
