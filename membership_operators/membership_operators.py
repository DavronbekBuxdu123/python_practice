# Exercise 1
word="APPLE"

user_input=input("Please enter the letter: ")

if user_input not in word:
    print(f"The letter->{user_input}  not found")
else:
    print("Ok")    


# Exercise 2
students={"Shermat","Ermat","Bobomurod","Elmurod"}
user_input=input('Enter the name: ')

if user_input not in students:
    print(f"{user_input} was not found")
else:
    print(f"{user_input} is a student")    

# Exercise 3
students_grade={"Shermat":4,"Bobomurod":5,"Elmurod":2}
user_input=input("Enter the name of student: ")

if user_input not in students_grade:
    print(f"{user_input} was not found")
else:
    print(f"{user_input}'s grade is {students_grade[user_input]}")    


# Exercise 4
user_input=input("Enter your email address: ")
if "@" not in user_input or "." not in user_input:
    print("Invalid email")
else:
    print("Valid email")    