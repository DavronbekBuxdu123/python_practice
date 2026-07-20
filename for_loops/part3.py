for x in range(0,20):
    print(x,end="\n")

for x in range(0,20):
    print(x,end="")

for x in range(0,20):
    print(x,end=" ")


for x in range(3):
    for y in range(1,10):
        print(y,end="")
    print()    


rows=int(input("Enter the rows: "))
columns=int(input("Enter the columns: "))
symbol=input("Enter the symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()    
