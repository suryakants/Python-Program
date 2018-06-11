

# setting/ getting and deleting and checking existance of an attribute 


class Employee:
	"This is my first python class"
	empCount = 0;

	def __init__(self, empId , name , salary, age):
		self.name = name;
		self.salary = salary;
		self.empId = empId
		self.age = age
	def getEmpId(self):
		print "Employee Id: ", self.empId;

	def employeeDetails(self):
		print "Employee Id : ",self.empId + "  Name : ", self.name + "  Salary : ", self.salary;




#creating Employee object 
emp1 = Employee("1038","Zara", 2000, 25);

if hasattr(emp1, "age"):
	print "Employee age : ", getattr(emp1,"age")
	setattr(emp1,"age",30);
	print "Employee age : ", getattr(emp1,"age")
	delattr(emp1,"age");
	# print "Employee age : ", getattr(emp1,"age")
else:
	print "Employee has not age attribute";

print "\n\n"
print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__


# hasattr(emp1, 'age')    # Returns true if 'age' attribute exists
# getattr(emp1, 'age')    # Returns value of 'age' attribute
# setattr(emp1, 'age', 8) # Set attribute 'age' at 8
# delattr(empl, 'age')    # Delete attribute 'age'