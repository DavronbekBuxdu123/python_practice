# Basic Calculator
operator=input("Enter the operator (+ - * /): ")
num1=float(input("Enter the number: "))
num2=float(input("Enter the number: "))

if operator=="+":
    result=num1+num2
    print(round(result))
elif operator=="-":
    result=num1-num2
    print(round(result))
elif operator=="*":
    result=num1*num2
    print(round(result))    
elif operator=="/":
    result=num1/num2
    print(round(result))    
else:
    print(f"{operator} is not valid")