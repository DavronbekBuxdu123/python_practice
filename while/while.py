# Exercise 1
name=input("Enter your name: ")

while name=="":
      print("You did not enter your name: ")
      name=input("Enter your name: ")
print(f"Hello {name}")      


# Exercise 2
age=int(input("ENter your age: "))

while age<0:
      print("Your age is invalid!")
      age=int(input("Please enter your age: "))
print(f"You are {age} years old")      

# Exercise 3
num=int(input("Enter a between 1-10: "))

while num<1 or num>10:
    print(f"{num} is invalid")
    num=int(input("Please enter a between 1-10: "))
print(f"Your number is {num}")    