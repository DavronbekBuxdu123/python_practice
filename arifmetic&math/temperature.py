# Temperature
unit=input("Enter to Celsius or Fahrenheit C/F: ")
temperature=float(input("Enter the temparature: "))

if unit=="C":
    result=(temperature*1.8)+32
    print(f"The temperature is {round(result,1)}°F ")
elif unit=="F":
    result=(temperature-32)/1.8    
    print(f"The tempature is {round(result,1)}°C ")
else:
    print(f"The {unit} is not valid")    
