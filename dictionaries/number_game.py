import random
low=1
high=100
random_number=random.randint(low,high)
is_start=True
guesses=0

print(f"Choose select a number between {low} and {high}")

while is_start:
    user_number=input("Enter the number: ")
    if user_number.isdigit() and int(user_number)>=low and int(user_number)<=high :
        guesses+=1
        if int(user_number)>random_number:
           print("Too high! Try to again")
        elif int(user_number)<random_number:
           print("Too low! Try to again")   
        elif int(user_number)==random_number:
            print(f"Correct! The answer was {random_number}")
            print(f"Guesses is {guesses}")
            is_start=False
    else:
            print(f"Choose select a number between {low} and {high}")
            

