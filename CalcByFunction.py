def add(*args):
    print(num1,"+",num2,"=",num1+num2)

def sub(*args):
    print(num1,"-",num2,"=",num1-num2)

def mult(*args):
    print(num1,"*",num2,"=",num1*num2)

def div(*args):
    print(num1,"/",num2,"=",num1/num2)

operater = input("Select any operater ( * - + / ): ")

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if operater == '+':
    add(num1,num2)
elif operater == '-':
    sub(num1,num2)
elif operater == '*':
    mult(num1,num2)
elif operater == '/':
    div(num1,num2)
else :
    print("Invalid operater!")


