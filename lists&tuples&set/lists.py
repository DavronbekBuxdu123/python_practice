fruits=['apple','orange','banana','peach']
fruits2={'apple','orange','banana','peach','peach'}

print(fruits[0])
print(fruits)

for fruit in fruits:
    print(fruit)

print(dir(fruits))
print(help(fruits))    

print('peach' in fruits)
print(len(fruits))

fruits.append("coconut")
fruits.remove("apple")
fruits.insert(0,"pineapple")
fruits.sort()
fruits.reverse()
print(fruits.index("orange"))
print(fruits.count('banana'))
fruits.clear()
print(fruits)


fruits2.add("watermelon")
fruits2.remove("apple")
fruits2.pop()
fruits2.clear()
print(fruits2)