'''
    fizz buzz program 
    if divided by only 3 -> Fizz
    if divided by only 5 -> BuzzF
    if divided by both 3 and 5 -> FizzBuzz
    else -> Fussaaa

'''

num=int(input("Enter Any Number : \n"))
#checking if wether the number is divisible by 3 and 5
if (num%3==0 and num%5==0):  
    print("FizzBuzz")
#checking if number is disible by 3 only
elif num%3==0:
    print("Fizzz")
#checking if number is divisible by 5 only
elif num%5==0:
    print("Buzz")
# if number is not divisible by both 3 and 5
else :
    print("Fussaa")


print("!!! Thank you for using my program !!!")

