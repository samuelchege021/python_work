class Account:
 def __init__(self,account_holder,balance):
      self.account_holder=account_holder
      self.balance=balance

 def sendmoney(self,amount):
     if amount<0:
        print("insufficient funds")
     else:
      self.balance+=amount
      print(f"i have deposited {amount} and my balance is {self.balance}")



 def withdraw(self,amount):
    if self.balance<amount:
          print("insufficient fund ")

    else:
       self.balance-=amount
       print(f"{amount} withdrawn successfully and the remaining fund is {self.balance}")

account=Account("samido",1000)




class savings(Account):
    def __init__(self,account_holder,balance,interest_rate):
         super().__init__(account_holder,balance)
         self.interest_rate=interest_rate


    def save(self,balance,saving,interest_rate,years):
        self.balance+=balance*saving*interest_rate/100*years
        print(f"able to save and my account is having{self.balance}")
account.sendmoney(1000)
account.withdraw(60)

mysaving=savings("sam",2000,14,)
mysaving.sendmoney(300)
mysaving.save(0,300,7,4)
