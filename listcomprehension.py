my_list=[10,20,30,40,50,60]

for index,character in enumerate (my_list):
     if index%2==0:
      my_list[index]=character*2


     else:
         my_list[index]=character*5
print(my_list)




#define two lists

bank_customers=["sam","eric","john","byt"]
customers_saving=[1000,1000,5000,8000]



for index,character in enumerate(bank_customers):
    print(f"my name is:{character} and my money is : {customers_saving[index]}")


my_list2=["a","b","c","d"]

for index,element in enumerate(my_list2,start=1):
  print(f"index  {index}, element {element}")


#list

my_list4=["banana","oranges","mangoes","onions"]


my_dic={index:element for index,element in  enumerate(my_list4)}

print(my_dic)








