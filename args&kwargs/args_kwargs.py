# Exercise 1
def example(a,b):
    return a+b

print(example(1,2))

# Exercise 2
import time
def exmaple2(*args):
    for i in args:
        print(i)
        time.sleep(1)

exmaple2(1,2,3,4,5)    


# Exercise 3
def example3(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value} ")

example3(firstname="davron",lastname='aslonov')    


# Exercise 4
def example4(*args,**kwargs):
    print(args,kwargs)
    print("\n----------------")  
    print("My args: ")
    for i in args:
        print(i,end=" ")
    print("\n----------------")    
    print("My kwargs: ")
    for key,value in kwargs.items():
        print(kwargs.get(f"{key}"))    

example4("Davron",1,2,3,4,5,country="Uzbekistan",state="Bukhara",job="Freelancer")