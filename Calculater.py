operater = input("Select any operater ( * - + / ): ")

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

if operater == '+':
    print(num1,"+",num2,"=",num1+num2)
elif operater == '-':
    print(num1,"-",num2,"=",num1-num2)
elif operater == '*':
    print(num1,"*",num2,"=",num1*num2)
elif operater == '/':
    print(num1,"/",num2,"=",num1/num2)
else :
    print("Invalid operater!")


