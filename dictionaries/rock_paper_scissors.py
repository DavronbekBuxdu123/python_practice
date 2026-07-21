import random

items=("rock","paper","scissors")
is_running=True
while is_running:
    computer=random.choice(items)
    user_input=input("Please choose a option: (rock,scissors,paper): ").lower()
    if user_input not in items:
        print('Your value is invalid!')
        continue

    if computer==user_input:
        print("It's a tie!")
    elif user_input=='rock' and computer=='scissors':
        print("You win!")        
    elif user_input=='scissors' and computer=='paper':
        print("You win!")        
    elif user_input=='paper' and computer=='rock'  :
        print("You win!")  
    else:
        print("You lose!")
    again=input("Are you going to play again? Y/N: ")
    if again.lower()=='y':
            is_running=True
    else:
            is_running=False

 
print("Thanks for playing!")