class Employee:
    def __init__(self, name, email, depart, comm) -> None:
        self.name = name
        self.email = email
        self.depart = depart
        self.comm = comm
    
    def showEmployee(self):
        print("Name : {}\nemail : {}\nDepartment : {} \nCommision : $ {} ".format(self.name, self.email, self.depart, self.comm))

class Salesman(Employee):
    def __init__(self,name, email, department, commission, level):
        super().__init__(name, email, department, commission)
        self.level = level
              
    def showEmployee(self):
        print("Salesman Profile")       
        super().showEmployee()      
        print("Level : ", self.level)
