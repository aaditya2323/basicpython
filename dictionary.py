persons = {


    "person1" :{

    "name":"Aaditya",
    "age": 17,
    "fav_food" :["momo","chowmin"]

    },
    "person2" : {
        "name":"kushal"
    }

}
print(persons["person1"].values())




phone=input("phone::>" "")
words={
"1":"one",
"2":"two",
"3":"three",
"4":"four",
"5":"five"
}
output=""
for i in phone:
  output+=words.get(i, "!")+" "
print(output)
