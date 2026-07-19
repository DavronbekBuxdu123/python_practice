# Exercise 1
age=int(input("Enter  your age: "))

if age>=100:
    print("No")
elif age>=18:
    print("Ok")    
elif age<0:
    print("No")
else:
    print("No")        


# Exercise 2
response=input("Would you like food (Y/N): ")

if response=="Y":
    print("Have some food")
else:
    print("No food for you")    


# Exercise 3
name=input("Enter your name: ")

if name=="":
    print("Type Error")
else:
    print(f"Hello {name}")    

# Exercise 4
is_online=True

if is_online:
    print("User is online")
else:
    print("User is offline")    