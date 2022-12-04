class Employee:

    def __init__(self, last_name, first_name, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.salary = salary

    def employee_description(self):
        print(f"Employee: {self.last_name} {self.first_name} Salary: {self.salary}")

    def employee_full_name(self):
        print(f"Full name: {self.last_name} {self.first_name}")
        return self.last_name+' '+self.first_name

    def employee_monthly_salary(self):
        print(f"Monthly salary: {self.salary}")
        return self.salary

    def employee_yearly_salary(self):
        print(f"Yearly salary: {self.salary * 12}")
        return self.salary * 12

    def employee_salary_raise(self, percent):
        print(f"{self.last_name} {self.first_name} has a salary raise of {percent}%")
        self.salary += percent * self.salary / 100
        print(f"Monthly raised salary: {self.salary}")
        print(f"Yearly raised salary: {self.salary * 12}")
