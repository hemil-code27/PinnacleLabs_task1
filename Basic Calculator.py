# Basic Calculator

print("---BASIC CALCULATOR---")

num1=float(input("enter first number:"))
num2=float(input("enter second number:"))

print("\nChoose operation")
print("1. addition\n2. subtraction\n3. multiplication\n4. division")

choice=int(input("enter choice (1,2,3 or 4):"))

if choice==1:
    result= num1 + num2
    print("Result=", result)

elif choice==2:
    result= num1- num2
    print("Result=", result)

elif choice==3:
    result= num1 * num2
    print("Result", result)

elif choice==4:
    if num2!=0:
        result= num1/num2
        print("Result=",result)
    else:
        print("Error! Division by zero is not allowed")

else:
    print("Invalid Choice")
