# Exercise 1
def happy_birthday(name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old")
    print("Happy birthday to you!")
    print()

happy_birthday("Davron",21)

# Exercise 2
def add(x,y):
    z=x+y
    return z

def subtract(x,y):
    z=x-y
    return z


def multiply(x,y):
    z=x*y
    return z

def divide(x,y):
    z=x/y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))

# Exercise 3
def create_fullname(firstname,lastname):
    firstname=firstname.capitalize()
    lastname=lastname.capitalize()
    return firstname+" "+lastname

fullname=create_fullname("davron","aslonov")    
print(fullname)

# Exercise 4
def dava(firstname="Davron",lastname="Aslonov"):
    firstname=firstname.capitalize()
    lastname=lastname.capitalize()
    return firstname+" "+lastname

davron=dava("davron123")
print(davron)

# Exercise 5
import time
def counter(start,end=5):
    for i in range(start,end):
        print(i)
        time.sleep(1)
    print('Done!')

counter(0)    

# Exercise 6
def simple(age,greetings,firstname,lastname,classname):
    print(f"{age} : {greetings} : {firstname} : {lastname} : {classname}")

simple(20,"hello",firstname="Davron",lastname="Aslonov",classname="7B")    