def add(x,y):
    return x+y


def subtraction(x,y):
    return x*y
def multiplication(x,y):
    return x*y

def division(x,y):
    return x/y






print("1.add")
print("2subtraction")
print("3.multiplication")
print("4.division")

while True:
 choices=input("enter a choice (1,2,3,4) :")

 if choices in ("1","2","3","4"):
    try:
        num1=int(input("enter the first no"))
        num2=int(input("enter the second no"))
    except ValueError:
        print("invalid syntax")
        continue
    if choices == '1':
           print(num1 ,"+", num2 , "=" ,add(num1,num2))

    if choices == '2':
        print(num1,"-" ,num2, "=", subtraction(num1,num2))

    if choices == '3':
      print(num1,"*",num2 ,"=" , multiplication(num1,num2))

    if choices == '4':
     print(num1,"/",num2 ,"=" ,division(num1,num2))



#
# mybank_account=int(input("show the amount :2"))
#
# if mybank_account>=1000:
#     print("I CAN WITHDRAW")
# else:
#     print("you dont have the enough amount to do a withdral")
#
#





