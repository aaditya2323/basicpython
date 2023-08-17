"""
Ask name & age of a person
if age is greater than 16 only then
print("you can get citizenship)
if age is greater than 16 and 18
then print(you can vote)
else:
print(you are a child)
replace you by your name 
if age is greater than 70 then
print("you can get briddha bhatta")

"""
print("|||welcome to my program||| \n")

print("this program is to inform about your elegibility accroding to your age")
name=(input("enter you name|| \n"))
age=int(input("enter you age \n"))
if age>16:
    print(f"-{name} can get the citizenship")
else:
    print(f"- {name} cannot get the citiznship")
if age>18:
    print(f"- {name} can able to vote")
else:
    print(f"- {name} is not able to get the citizenship")
if age>70:
        print(f"- {name} can get biddhabhatta")
else:
        print(f"- {name} cannot get briddhabhatta")



        print(f"|||THANK YOU {name} for using our program||||")


    
age=int(input("Enter your age :: \n"))
if age>=16 :
    if age>70:
        print("You are old enough to get briddhavatta")
    elif (age>=16 and age <18):
        print ("You can get citizenship only")
    elif age> 18 :
        print ("You can vote and also get citizenship")
   
    
    
else :
    print("You are child")


