name=input()
print(type(name))

name=input("What is your name: ")
age=int(input("How old are you: "))
age=age+1

print(f"Your name is {name}")
print("Happy birthday!")
print(f"You are  {age} years old")


# Rectangle Area Calc
length=float(input("Enter the length: "))
width=float(input("Enter the width: "))
area=length*width

print(f"The area is: {area}cm²")


# Shopping cart Calc
item=input("What item would you like to buy?: ")
price=float(input("What is the price?:"))
quantity=int(input("How many would yo like?: "))

total=quantity*price

print(f"Your have bought {quantity}x {item}")
print(f"Your total is ${total}")