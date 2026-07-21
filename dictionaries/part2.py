menu_items={
    "pizza":5.0,
    "lavash":9.0,
    "popcorn":10.0,
    "hamburger":11.0,
    "hot-dog":15.0,
    "cola":5.0
}

print("---------MENU ITEMS---------")
for key,value in menu_items.items():
    print(f"{key:10} : {value: 5}")
print("--------------------------")  

user_choices=[]
total=0
while True:
    food=input("Choose the menu items (q to quit): ").lower()
    if food=="q":
        break
    elif menu_items.get(food) is not None:
        total=total+menu_items.get(food)
        user_choices.append(food)
        
print("-------Your cart menu---------")
for food in user_choices:
    print(food)
print("----------------------")
print(f"Your total is {total}")