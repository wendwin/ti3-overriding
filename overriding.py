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

class It(Employee):
    def __init__(self,name, email, department, divisi, commission):
        super().__init__(name, email, department, commission), 
        self.divisi = divisi
              
    def showEmployee(self):
        print("IT Profile")      
        super().showEmployee()     
        print("Divisi : ", self.divisi)

salesman = Salesman("John Doe", "doejohn@gmail.com", "Sales", 572, "Senior")
salesman.showEmployee()
print("")
it = It("Jennifer Smith", "smithjenn@gmail.com", "IT" ,"Web Developer", 5000)
it.showEmployee()           