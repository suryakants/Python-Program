class MyClass(object):
	"docstring for myClass -- description for this class"
	a = 10
	def func(self):
				print('Hello')


print(MyClass.a)
print(MyClass.func)
print(MyClass.__doc__)