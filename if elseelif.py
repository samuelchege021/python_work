marks=int(input("enter marks :"))

if marks>=80 and marks<=100:
    print("you have an A ")

elif marks>=60 and marks<=79:
    print("you have a B ")

elif marks>=40 and marks<=59:
    print("you have got a c")

elif marks >= 0 and marks <= 39:
    print("you have failed terribly")


else:
    print("wrong input")



n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))
n4=int(input("enter the fourth number"))

#
# if number1>number2:
#     print("i am the max",number1)
#
# elif number1>number2:
#     print("i am the max",number1)
#
# elif number1>number3:
#     print("i am the max",number1)
# elif number1>number4:
#     print("i am the max",number1)



#
#
# elif number2 > number3:
#     print("i am the max", number2)
# elif number2 > number3:
#     print("i am the max", number2)
#
# elif number2 > number4:
#     print("i am the max", number2)
#
#
#
#
# elif number3 > number1:
#     print("i am the max", number3)
#
# elif number3 > number2:
#     print("i am the max", number3)
# elif number3 > number4:
#     print("i am the max", number3)
#
#
#
#
#
#
# elif number4 > number2:
#     print("i am the max",number4)
# if number4 > number3:
#     print("i am the max",number4)
# elif number4 > number1:
#     print("i am the max",number4)
#
#
#
#


if n1>n2 and n1>n3 and n1>n4:

    print("i am largest no",n1)

elif  n2>n1 and n2>n3 and n2>n4:
    print("i am largest no", n2)

elif  n3>n1 and n3>n4 and n3>n2:
    print("i am largest no", n3)

elif n4> n1 and n4 > n2 and n4 > n3:
    print("i am largest no", n4)







def checkprime(n):

  if n%n==1:
      return True

  x=checkpri
  print("i am a prime no")



x=int(input("enter number"))

if x>=1 and not(x%2==0) :
    print("i am a prime number")
