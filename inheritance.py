
class Parent:
	"""docstring for Parent"""

	parentAttr = 100;

	def __init__(self):
		print "Parent constructor call";

	def parentMethod(self):
		print 'Parent method call'

	def setAttr(self,attr):
		Parent.parentAttr = attr;

	def getAttr(self):
		print "Parent attribute: ",Parent.parentAttr;




class Child(Parent):
	def __init__(self):
		print 'Child class constructor call';

	def childMethod(self):
		print 'Child method call';

	def parentMethod(self):
		print 'Child class ParentMethod call'





c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method

		
		