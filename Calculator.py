def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def Division(a,b):
    if(b!=0):
        return a/b
    else:
        print("Error: Division by Zero")
print("*"*10,"Calculator","*"*10)
while True:
    print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")
    choice = int(input("Enter Your Choice (1-5): "))
    if(choice<5):
        num1 = int(input("Enter value of Number 1: "))
        num2 = int(input("Enter value of Number 2: "))
    if(choice==1):
        print(num1,"+",num2,"=",Addition(num1,num2))
    elif (choice==2):
        print(num1,"-",num2,"=",Subtraction(num1,num2))
    elif (choice==3):
        print(num1,"*",num2,"=",Multiplication(num1,num2))
    elif (choice==4):
        print(num1,"/",num2,"=",Division(num1,num2))
    elif (choice == 5):
        print("Thank You!!")
        break
    else:
        print("Invalid Choice!!!!\nPlease Enter Correct choice")