numbers=[1,2,3,4,5]
my_dictionary={1:"A",2:"B",3:"C",4:"D"}
for i in numbers:
    print(i)

for i in numbers:
    print(i,end=" ")

for i in reversed(numbers):
    print(i,end=" ")

for i in (numbers):
    print(i,end="-")

for i in my_dictionary:
    print(i)

for i in my_dictionary.values():
    print(i)

for key,value in my_dictionary.items():
    print(key,value)