
def printinfo(arg1, *varTuple):
	"This prints a variable passed arguments"
	print "Output is: "
	print arg1;
	for var in varTuple:
		print var;

printinfo(1,2,3,4,5);


