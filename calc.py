#imports
from os import system

#globals


#function definitions
def print_menu():
    print("-------------------")
    print("   PyCalc 3000")
    print("-------------------")
    
    print("[1] Sum")
    print("[2] Substract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[X] Exit")

def add(a,b):
    print(a," + ",b," = ", round(a+b,2))
    
def subtract(a,b):
    print(a," - ",b," = ", round(a-b,2))
    
def multiply(a,b):
    print(a," * ",b," = ", round(a*b,2))
    
def divide(a,b):
    if b!=0:
        result=round(a/b,2)
    else: 
        print("ERROR: division by zero")
        result=0
    print(str(a)+" / "+str(b)+" = "+ str(result))

# plain intructions

option=""

while option.upper() != "X":
    system("cls")
    print_menu()
    option = input("Please select an option:")
    if option.upper() == "X":
        break
    
    number1 = float (input("Give a numbre:"))
    number2 = float (input("Give a othrt numbre:"))

    if option == "1":
        add(number1,number2)
    elif option == "2":
        subtract(number1,number2)
    elif option == "3":
        multiply(number1,number2)
    elif option == "4":
        divide(number1,number2)
    else:
        print("error")
    input("press enter to continue...")

print("Thanks, good bye")