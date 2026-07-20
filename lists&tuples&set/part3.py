# Exercise 1
fruits=['apple','orange','peach','coconut']
drinks=['cola','pepsi','fanta','sprite']
meals=['pizza','burger','sushi','soup']

collections=[fruits,drinks,meals]

print(collections)

for collect in collections:
    for item in collect:
        print(item,end=" ")
    print()    
    
# Exercise 2
num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#")
)    

for item in num_pad:
    for i in item:
        print(i,end=" ")
    print()    
