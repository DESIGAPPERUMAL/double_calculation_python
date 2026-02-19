#this is first coding to github intro
a = (int(input("enter the first value = ")))
b = (int(input("enter the second value = ")))
c = (int(input("enter the third value = ")))
valued_0 = input("Enter the first operation you want: ")
valued_1 = input("Enter the second operation you want: ")
valued_2 = input("enter the third operation you want: ")

def calculator(valued, a, b ,c ):
    if valued == "addition" or "add" or "sum" :
        print(a + b + c )
    elif valued == "subtraction" or "sub" or "minus":
        print(a - b - c )
    elif valued == "multiplication" or "mul" or "product":
        print(a * b * c )
    elif valued == "division" or "div" or "divide":
        print(a / b / c)
    elif valued == "floor division" or "floordiv":
        print(a // b //c)
    elif valued == "modulus" or "mod":
        print(a % b % c)
    else:
        print("this operation not available")
# new project for triple calculation
print("Enter first operation")
calculator(valued_0, a, b , c)
print("Enter the second operation")
calculator(valued_1, a, b , c)
print("enter the third operation")
calculator(valued_2, a ,b , c)
