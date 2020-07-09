class Employee:
    def __init__(self,id,name,salary):
        self.name = name
        self.id = id
        self.salaray = salary
    def __str__(self):
        return("Employee name: "+self.name+", id: "+str(self.id)+", salary: "+str(self.salaray))

e1 = Employee(101,"manoj",35000)
print(e1.__str__())