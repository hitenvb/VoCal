import pyttsx3
engine=pyttsx3.init()
engine.setProperty("rate",125)
def aud(a1):
    engine.say(a1)
    engine.runAndWait()
print("Welcome to VoCal ")
aud("Welcome to VoCalc ")
aud("Enter 1st Number to perform operations: ")
a=float(input("\nEnter 1st Number to perform operations:"))
aud("Enter 2nd number to perform operation")
b=float(input("Enter 2nd number to perform operation"))
def add(a,b):
    c=a+b
    print("The Addition of two numbers is: ",c)
    c=str(c)
    aud("The Addition of two numbers is: "+c)
def mul(a,b):
    c=a*b
    print("The Product of two numbers is: ",c)
    c=str(c)
    aud("The Product of two numbers is: "+c)
def div(a,b):
    c=a/b
    print("The Division of two numbers is: ",c)
    c=str(c)
    aud("The Division of two numbers is: "+c)
def sub(a,b):
    c=a-b
    print("The subtraction of two numbers is: ",c)
    c=str(c)
    aud("The subtraction of two numbers is: "+c)
aud("Enter 1 for addition,Enter 2 for Subtraction,Enter 3 for Multiplication,Enter 4 for Division: ")
x=input("Enter 1 for addition,\nEnter 2 for Subtraction,\nEnter 3 for Multiplication,\nEnter 4 for Division: ")
def calcit():
    if x=="1":
     add(a,b)
    elif x=="2":
     sub(a,b)
    elif x=="3":
     mul(a,b)
    elif x=="4":
     div(a,b)
    else:
     print("Please select from given options !")
     aud("Please select from given options !")
calcit()
j="1"
while j=="1":
    aud("\n Press Enter key, to exit, or press 'c', for performing more operations on same input: ")
    inp1=input("\n Press Enter key to exit or press 'c' for performing more operations on same input: ")
    if inp1=='c':
      x=input("Enter 1 for addition,\nEnter 2 for Subtraction,\nEnter 3 for Multiplication,\nEnter 4 for Division: ")
      calcit()
    else:
      exit()
