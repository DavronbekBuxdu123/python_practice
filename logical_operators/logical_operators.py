# Exercise 1 -> or 
temp=25
is_raining=True

if temp > 35 or temp < 0 or is_raining:
    print("Do not go outside")
else:
    print("Go outside")    


# Exercise 2 -> and & not
temp=25
is_sunny=False

if temp >= 30 and is_sunny:
    print("It is hot outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is cold outside 🥶")    
    print("It is sunny ☀️")
elif 10 < temp < 30 and is_sunny:
    print("It is warm outside ☂️")   
    print("It is sunny ☀️")
elif temp >= 30 and not is_sunny:
    print("It is hot outside 🥵")
    print("It is cloudy ☁️")
elif temp <= 0 and not is_sunny:
    print("It is cold outside 🥶")    
    print("It is  cloudy ☁️")
elif 10 < temp < 30 and not is_sunny:
    print("It is warm outside ☂️")   
    print("It is  cloudy ☁️")    
