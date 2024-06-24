def myfunc():
    print("this is my function")

myfunc()

# def addtwonumbers():
    # num=int(input("enter the firsrt number"))
    # num2=int(input("enter the firsrt number  "))
    # print(f"the sum of {num} and {num2} is", num+num2)
#addtwonumbers()



def calculator():
    num1 = int(input("enter the first no"))
    operator = (input("enter operator(+,-,*,/,% :"))
    num2 = int(input("enter the second"))
    num3 = num1, num2

    if operator == "+":
        print(num1, "+", num2, "is", num1 + num2)


    elif operator == "-":
        print(num1, "-", num2, "is", num1 - num2)


    elif operator == "*":
        print(num1, "*", num2, "is", num1 * num2)

    elif operator == "/":
        print(num1, "*", num2, "is", num1 / num2)

        print(num1, "%", num2, "is", num1 % num2)
calculator()
    elif operator == "%":



def add(x,y):
    return x+y

x=add(3,4)
print(x)