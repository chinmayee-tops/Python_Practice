class Employee:
    def getemp(self, empname):
        self.emp=empname

    def putemp(self):
        print("Employee Name : ",self.emp)

class Dept(Employee):
    def getdept(self, deptname):
        self.dept=deptname

    def putdept(self):
        print("Dept Name : ",self.dept)

D=Dept()
D.getemp("Chinmayee")
D.putemp()
D.getdept("Finance")
D.putdept()
