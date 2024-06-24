class Employee:
    def _init_(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Salary: ${self.salary}")

    def calculate_annual_salary(self):
        return self.salary * 12


class Manager(Employee):
    def _init_(self, name, employee_id, salary, department, employees_managed=None):
        super()._init_(name, employee_id, salary)
        self.department = department
        self.employees_managed = employees_managed if employees_managed else []

    def display_information(self):
        super().display_information()
        print(f"Department: {self.department}")
        print(f"Employees Managed: {[employee.name for employee in self.employees_managed]}")

    def add_employee(self, employee):
        self.employees_managed.append(employee)

    def display_employees_managed(self):
        print("Employees Managed:")
        for employee in self.employees_managed:
            print(f" - {employee.name} (ID: {employee.employee_id})")


class Developer(Employee):
    def _init_(self, name, employee_id, salary, programming_languages=None):
        super()._init_(name, employee_id, salary)
        self.programming_languages = programming_languages if programming_languages else []

    def display_information(self):
        super().display_information()
        print(f"Programming Languages: {', '.join(self.programming_languages)}")

    def add_programming_language(self, language):
        if language not in self.programming_languages:
            self.programming_languages.append(language)


class Intern(Employee):
    def _init_(self, name, employee_id, salary, school_name, graduation_year):
        super()._init_(name, employee_id, salary)
        self.school_name = school_name
        self.graduation_year = graduation_year

    def display_information(self):
        super().display_information()
        print(f"School Name: {self.school_name}")
        print(f"Graduation Year: {self.graduation_year}")


# Create some employees
manager = Manager("Erick", 1, 90000, "Engineering")
developer = Developer("Keysha", 2, 80000, ["Python", "JavaScript"])
intern = Intern("daniel", 3, 30000, "State University", 2024)

# Display their information
manager.display_information()
print()
developer.display_information()
print()
intern.display_information()

# Manager adds employees to manage
manager.add_employee(developer)
manager.add_employee(intern)

# Display the list of employees managed by the manager
manager.display_employees_managed()

# Developer adds a new programming language
developer.add_programming_language("Java")
developer.display_information()

# Calculate and print annual salaries
print(f"{manager.name}'s Annual Salary: Ksh{manager.calculate_annual_salary()}")
print(f"{developer.name}'s Annual Salary: KSH{developer.calculate_annual_salary()}")
print(f"{intern.name}'s Annual Salary: KSH{intern.calculate_annual_salary()}")