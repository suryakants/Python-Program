

def printme (str):
	"Just to see the keyboard argument" 
	print str;
	return;


# Now function call

printme(str = "Hello! this is me")


def printInfo(name, age = 25):
	"Function with two arguments"
	print "Name :", name;
	print "Age :", age;

printInfo( name = "Suresh");