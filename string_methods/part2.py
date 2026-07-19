# Exercise 1
username=input("Enter your username: ")
# print(username.find(" "))
if len(username)>12:
    print("Your username is invalid")
elif not username.find(" ")==-1:
    print("Your username is invalid")
elif not username.isalpha():
    print("Your username is invalid")
else:
    print(f"Welcome {username}")        