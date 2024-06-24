class student:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname



    def display(self):
     print(self.firstname,self.lastname)


my_student=student("john","smith")
my_student.display()
my_student=student("eric","were")
my_student.display()