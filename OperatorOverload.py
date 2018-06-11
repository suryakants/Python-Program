


class Vector:
	def  __init__(self, x, y):
		self.x = x;
		self.y = y;


	def  __add__(self, otherVector):
		print('__add__')
		return Vector(self.x + otherVector.x, self.y + otherVector.y)

	def __str__(self):
		print("__str__")
		return "Vector (%d, %d) :" % (self.x, self.y);

v1 = Vector(10,20);
v2 = Vector(20,30);

print v1 + v2;
		