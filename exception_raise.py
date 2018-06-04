

def functionName( level ):
   if level < 1:
      raise "Invalid level!", level
      # The code below to this would not be executed
      # if we raise the exception
   else:
    	print "Hello", level;





try:
	functionName(0)
except "Invalid level!":
	print "Going to close the file"
else:
	print "Going to close the file"
