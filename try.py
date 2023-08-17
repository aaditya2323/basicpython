name=[]
age=[]
fav_game=[]

number_of_details=input("How many details you want : ")
number_of_details=int(number_of_details)

for i in range(number_of_details):
    new_name=input("Enter name : ")
    new_age=input("Enter age : ")
    new_fav_game=input("Enter name of fav game : ")
    name.append(new_name)
    age.append(new_age)
    fav_game.append(new_fav_game)

    #result
for i in range(number_of_details):
    print(f"{name[i]} is {age[i]} years old and he likes {fav_game[i]}")

