class Employee:
    def empmethod(self):
        print("Employee parent class and method")

class Developer(Employee):
    def devmethod(self):
        print("Developer child class and method")
        
ed = Developer()
ed.empmethod()
ed.devmethod()


