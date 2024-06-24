class employees:
    def __init__(self,name,employee_ID,salary):
        self.name=name
        self.employee_ID=employee_ID
        self.salary=salary

    def display_employee(self,):
        print(self.name,self.employee_ID,self.salary)
        print("my annual salary",self.salary*12)


class managers(employees):
    def __init__(self,name,employee_ID,salary,department,list_of_employees):
        super().__init__(name,employee_ID,salary)

        self.department=department
        self.list_of_employees=list_of_employees = []

        self.list_of_employees.append ([])


    def display_employees(self,add):
       list_of_employees=self.list_of_employees.append(add)
       print("this are list of the the employees I manage",self.list_of_employees)

class developers(employees):
    def __init__(self, name, employee_ID, salary,list_of_programming_languages):
        self.list_of_programming_languages=list_of_programming_languages
        super().__init__(name,employee_ID,salary)

    def add_skill(self):

        print("this are my skill set",self.list_of_programming_languages)

class interns(employees):
    def __init__(self, name, employee_ID, salary,school_name,graduation_year):
        self.school_name=school_name
        self.graduation_year=graduation_year
        super().__init__(name,employee_ID,salary,)

    def display_interns(self):
      print(f"my name is {self.name} and I am currently studying at {self.school_name} and I will graduate at {self.graduation_year}")



# person=employees("eric",3567,3000)
# person.display_employee()

Manager=managers("sam,",5678,7000,"x",["chege","julius"])
employee1=employees("SAM",3,2)
Manager.display_employees(employee1)


Developers=developers("eric",4567,6000,"python,csharp,python,django,javascript")
Developers.add_skill()

Intern=interns("samuel chege",67899,900,"cuea",2025)
Intern.display_interns()