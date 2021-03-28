string=input("Enter the string to add at the beginning: ")
num=input("Enter items to make them as a list: ")
list=num.split(" ")
final_list=[]

for i in range(len(list)):
    k=string+' '+list[i]
    final_list.append(k)
print(f"The final list formed is: {final_list}")
