num=int(input("enter your no:"))

flag=False

if num==1:
 print("the no is not a prime number")



elif num>1:
    for i  in range (2,num):
      if (num%i)==0 :
       flag=True
       break


    if flag:
      print ("the number  is not a prime number",num)

    else:
     print("the number is  a prime number",num)


