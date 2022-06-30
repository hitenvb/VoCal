import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init()
engine.setProperty("rate",125)

def aud(a1):
    engine.say(a1)
    engine.runAndWait()

print("Welcome to VoCal ")
aud("Welcome to VoCalc ")

def sp1(f,z):
    if f == '':
        r=sr.Recognizer()

        with sr.Microphone() as source:
            print(z)

            r.adjust_for_ambient_noise(source, 2)

            audio = r.listen(source)
        try:
            global a
            a=r.recognize_google(audio)
            a=float(a)
            print("You said, ",a)

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not get results from Google, please check your network connection")

def sp2(f,z):
    if f == '':
        r=sr.Recognizer()

        with sr.Microphone() as source:
            print(z)

            r.adjust_for_ambient_noise(source, 2)

            audio = r.listen(source)
        try:
            global b
            b=r.recognize_google(audio)
            b=float(b)
            print("You said, ",b)

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not get results from Google, please check your network connection")
    else:
        pass

aud("Enter 1st Number to perform operations: ")
a=(input("\nEnter 1st Number to perform operations:"))
sp1(a,z="Say 1st Number to perform operations:")
aud("Enter 2nd number to perform operation: ")
b=(input("Enter 2nd number to perform operation"))
sp2(b,z="\nSay 2nd number to perform operations:")

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

def sp3(f,z):
    if f == '':
        r=sr.Recognizer()

        with sr.Microphone() as source:
            print(z)

            r.adjust_for_ambient_noise(source, 2)

            audio = r.listen(source)
        try:
            global x
            x=r.recognize_google(audio)
            print("You said, ",x)

        except sr.UnknownValueError:
            print("Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not get results from Google, please check your network connection")
    else:
        pass

aud("Enter or Say 1 for addition,Enter or Say 2 for Subtraction,Enter or Say 3 for Multiplication,Enter or Say 4 for Division: ")

x=input("Enter 1 for addition,\nEnter 2 for Subtraction,\nEnter 3 for Multiplication,\nEnter 4 for Division: ")
sp3(x,z="")
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
      sp3(x,z="Say 1 for addition,Say 2 for Subtraction,Say 3 for Multiplication,Say 4 for Division: ")
      calcit()
    else:
      exit()
