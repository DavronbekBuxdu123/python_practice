import math

a=9
b=9.1
result=math.sqrt(a)
result1=math.ceil(b)
result2=math.floor(a)
result3=math.floor(b)

print(math.pi)
print(math.e)
print(result)
print(result1)
print(result2)
print(result3)


# Circumference
radius=float(input("Enter the radius: "))
circumference=2*math.pi*radius

print(f"The circumference is: {round(circumference,2)}cm")


# Area of the circle
radius=float(input("Enter the radius: "))
area=math.pi*pow(radius,2)
print(f"The area of rectangle is: {round(area,2)}cm²")


# Side C
a=float(input("Enter side A: "))
b=float(input("Enter side B: "))
c=math.sqrt(pow(a,2)+pow(b,2))

print(f"The side C= {c}")