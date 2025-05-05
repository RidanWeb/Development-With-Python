from manu import Manu


class Restaurant:

    def __init__(self, name):

        self.name = name
        self.employees = []
        self.manu = Manu() #Confusing part, ================(Confusion Clear)======================
                 
    
    def add_employee(self, employee):

        self.employees.append(employee)
        print(f"Employee {employee.name} added to {self.name}.")

    
    def view_employees(self):

        if not self.employees:
            print(f"No employees found in {self.name}.")
        else:
            print(f"Employees in {self.name}:")

            print(f"Name\tPhone\tEmail\tAddress\tAge\tDegination\tSalary")
            for emp in self.employees:
                
                print(f"{emp.name}\t{emp.phone}\t{emp.email}\t{emp.address}\t{emp.age}\t{emp.degination}\t{emp.salary}")
