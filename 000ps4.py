







class Forex:
    def __init__(self,buy,sell):
        self.buy=buy
        self.sell=sell



class Fibo(Forex):
    def __init__(self, levels, buy, sell):
        super().__init__(buy, sell)
        self.levels=levels



     def Trade(self):
      if self.levels ==50:
            print(f"Markert is reversing at ,{self.levels} ,buy or sell acorrding to the markert trend so ,{self.buy} or {self.sell}")


Trade1=Fibo(50,"sell" , "buy")
Trade1.Trade()