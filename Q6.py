def intersection(a, b):
    return list(set(a) & set(b))
 
def main():
    alist=[]
    blist=[]
    n1=int(input("Enter number of elements for list 1: "))
    n2=int(input("Enter number of elements for list 2: "))
    print("---> For list1 <---")
    for x in range(0,n1):
        element=input("Enter element " + str(x+1) + " : ")
        alist.append(element)
    print("---> For list2 <---")
    for x in range(0,n2):
        element=input("Enter element " + str(x+1) + " : ")
        blist.append(element)
    print("Common items are: ")
    print(intersection(alist, blist))
main()