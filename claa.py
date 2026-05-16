class employee:
    
    def __init__(self,name,salary, department):
        self.name = name
        self.salary = salary
        self.department = department
        
    def show_detail(self):
        print(f'{self.name} works in {self.department} and earn {self.salary}')
    
employee1 = employee("garima", 500000, "Ai Team")
employee1.show_detail()
    
employee2 = employee("rahul", 700000, "Backend Team")
employee2.show_detail()
    

class manager(employee):
    def manager_team(self):
        print(f'{self.name} manages team')

employee3 = manager("Garima", 800000, "AI")
employee3.show_detail()
employee3.manager_team()


class developer:
    def __int__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
        
    def show_detail(self):
        print(f'{self.name} works in {self.department} and earns {self.salary}')
        
class developer(employee):
    def employee_team(self):
        print(f'{self.name} writes Python code')
        
developer1 = developer("garima", 500000, "A1")
developer1.show_detail()
developer1.employee_team()



class employee:
    def__int__(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department
        
    def show_detail(self):
        print(f'{self.name} works in {self.department} and earns {self.salary}')
        
class develper(employee):
    def write_code(self):
        print(f'{self.name} writes Python code')
        
class manager(employee):
    def manager_team(self):
        print(f'{self.name} manages team')
        
developer1 = Developer("Garima", 500000, "AI Team")

manager1 = Manager("Rahul", 700000, "Management Team")

employees = [developer1, manager1]

for employee in employees:
    employee.show_details()
        