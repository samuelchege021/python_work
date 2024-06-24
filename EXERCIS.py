# create
# A class called cars with the followin attributes,model,year of manufacture,type,color

# create <a method to print


# MY DREAM CAR IS ..... MANUFACTURED IN.....BEINBG A....TYPE.....,IN COLOURS

# INITIA;LISE WITH ATLEAS 5OBJECTS

class Cars:

  def __init__(self,model,yearofmanufactures,type,color):
       self.model=model
       self.yearofmanufactures=yearofmanufactures
       self.type=type
       self.color=color



  def display(self):
    print(f"my dream car  {self.model}manufacrure in  {self.yearofmanufactures} being {self.type} {self.color}")
car1=Cars("ford",2020,"suv","blue")

car1.display()

car2=Cars("ford",2020,"suv","blue")
car2.display()