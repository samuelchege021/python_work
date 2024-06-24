class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age







class Student(Person):
    
    def __init__(self,first_name,last_name,age,score):
        self.score=score
        super().__init__(first_name,last_name,age)

    def print_name(self):
        print(f"my name is {self.first_name},{self.last_name}, and I am  {self.age} years old got a score of {self.score} in my unit")


mystudent=Student("samuel","chege",20,"A PLAIN")
mystudent.print_name()

mystudent2=Student("jack","Ma",4,67)
mystudent2.print_name()
mystudent3=Student("eric","kamau",4,50)
mystudent3.print_name()
mystudent4=Student("oliva","ndungu",15,90)
mystudent4.print_name()
mystudent5=Student("wambui","nganga",25,45)
mystudent5.print_name()
mystudent6=Student("bivon","keronche",21,75)
mystudent6.print_name()