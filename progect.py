condition=4
while condition==4:

  print("...welcome...|")

  print("1. enter '1' to add details")
  print("2. entern '2' to search details")
  print("3. enter '3' to exit")
  name=[]
  booknumber=[]
  gener=[]
  publication=[]
  price=[]
  ans=int(input("enter:::" " "))
  if ans==1:
    print("Enter your book details...\n")
    i_name=input(">> enter book name:::>")
    i_booknumber=int(input(">> enter book number:::>"))
    i_gener=input(">> enter book gener:::>")
    i_publication=input(">> enter book publication:::> ")
    i_price=int(input(">> enter book price:::>"))
    

    print("...your details are saved as...\n")
    print("**ABOUT BOOK** \n")
    name.append(i_name)
    booknumber.append(i_booknumber)
    gener.append(i_gener)
    publication.append(i_publication)
    price.append(i_price)
    print(f" > NAME = {i_name}")
    print(f" > BOOKNUMBER = {i_booknumber}")
    print(f" > GENER = {i_gener}")
    print(f" > Publication = {i_publication}")
    print(f" > price = {i_price}")
    condition=int(input(">> enter '4' to add another details:::>"))



  elif ans==2:
    print("chose  any way to search... \n")
    print(">> enter '1' to search by book name")
    print(">> enter'2' to search by book number \n")
    choseway=int(input("enter::>"))
    if choseway==1:
      search_byname=input("ENTER BOOK NAME::>")
      if search_byname=={i_name}:
        print("THE BOOK IS AVILABLE AS")
        print(f" > NAME = {i_name}")
        print(f" > BOOKNUMBER = {i_booknumber}")
        print(f" > GENER = {i_gener}")
        print(f" > Publication = {i_publication}")
        print(f" > price = {i_price}")

      
      

      
      


    elif choseway==2:
      search_bynumber=int(input("ENTER BOOK NUMBER::>"))
      if search_bynumber=={i_booknumber}:
        print("THE BOOK IS AVILABLE AS")
        print(f" > NAME = {i_name}")
        print(f" > BOOKNUMBER = {i_booknumber}")
        print(f" > GENER = {i_gener}")
        print(f" > Publication = {i_publication}")
        print(f" > price = {i_price}")

      else:
        print("THE BOOK IS NOT AVILABLE")

  elif ans==3:
    print("THANK YOU")
    exit()

  else:
    exit()



     
        

      
    



    
    



    
  





        

        

  
    



  



  

 

    


    
    





    





    

