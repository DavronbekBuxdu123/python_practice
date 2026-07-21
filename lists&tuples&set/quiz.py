questions=["O'zbekiston poytaxti qayer?",
           "O'zbekistonda nechta viloyat bor?",
           "Futbolda necha kishi o'ynaydi?(bir jamoada)",
           "Hafta kunlari sonini toping?",
           "Nechta fasl bor bir yilda?"
           ]

options=[
    ["A. Toshkent","B. Buxoro","C. Samarqand ","D. Xiva"],
    ["A. 10","B. 12","C. 20 ","D. 8"],
    ["A. 1","B. 2","C. 11 ","D. 20"],
    ["A. 7","B. 8","C. 4 ","D. 41"],
    ["A. 1","B. 3","C. 4 ","D. 10"],
]

answers=["A","B","C","A","C"]

is_start=False
user_input=input("Testni boshlaymizmi? (Y/N): ")
if user_input=="Y":
    is_start=True
else:
    print("Keyingi safar urinib ko'ring!")

while is_start:
    score=0
    s=0
    user_answers=[]
    for question in questions:
        print("--------------")
        print(question)
        for option in options[s]:
                print(option)
        user_answer=input("Javobingizni kiriting: (A,B,C,D): ")
        user_answers.append(user_answer)
        if user_answer==answers[s]:
            score=score+1
        s=s+1
    is_start=False
    print("--------------")
    print("To'g'ri javoblar")
    for i in answers:
         print(i,end=" ")

    print("\n--------------")
    print("Sizning javoblaringiz")
    for j in user_answers:
        print(j,end=" ")     
    print("\n------------")    
    print(f"\nSizning natijangiz {score} ta to'g'ri javob. Foizda {score*100/len(answers)}"     )
