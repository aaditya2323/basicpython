print("Welcome")
array1=[]
array2=[]
array3=[]
for i in range(3):
    x=int(input("enter any number in list1 \n"))
    y=int(input("enter any number in list2 \n "))
    array1.append(x)
    array2.append(y)
    mult=array1[i]*array2[i]
    array3.append(mult)
   
print(array3)