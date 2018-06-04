


class Employee:
	"This is my first python class"
	empCount = 0;

	def __init__(self, empId , name , salary):
		self.name = name;
		self.salary = salary;
		self.empId = empId

	def getEmpId(self):
		print "Total Employee: ", self.empId;

	def employeeDetails(self):
		print "Employee Id : ",self.empId + "  Name : ", self.name + "  Salary : ", self.salary;





#"This would create first object of Employee class"
emp1 = Employee("1038","Zara", 2000)
emp1.getEmpId();
emp1.employeeDetails();
#"This would create second object of Employee class"
emp2 = Employee("123", "Manni", 5000)
emp2.getEmpId();
emp2.employeeDetails();


