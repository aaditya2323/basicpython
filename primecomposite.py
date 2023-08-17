num=int(input("enter any number"))
count=0
if num ==1:
    print("Nither prime nor composite")
    exit()
    
for i in range(1,num+1):
    if num %i ==0 :
        count=count+1
    else :
        count = count

if count ==2:
    print("Prime")
else:
    print("Composite")