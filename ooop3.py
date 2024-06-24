# create
# A class called cars with the followin attributes,model,year of manufacture,type,color

# create <a method to print


# MY DREAM CAR IS ..... MANUFACTURED IN.....BEINBG A....TYPE.....,IN COLOURS

# INITIA;LISE WITH ATLEAS 5OBJECTS



class Cars:
   def __init__(self, model, year_of_manufacture, type,color):
       self.model=model
       self.year_of_manufacture=year_of_manufacture
       self.type=type
       self.color=color



   def drive(self):
       print(f"my dream car is to drive {self.model} manufactured in {self.year_of_manufacture} being a {self.type} and  color {self.color} is the best one")



my_car=Cars("sedan",2024,"Bmww3","blue")

my_car.drive()

my_car1=Cars("crossover",2023,"Toyotahighlander","red")

my_car1.drive()

my_car3=Cars("coupe",2025,"Audi A5","lightblue")
my_car3.drive()

my_car4=Cars("minivian",2018,"HondaOdyssey","black")
my_car4.drive()

my_car5=Cars("station wagon",2021,"mercedesbenz","black")
my_car5.drive()



