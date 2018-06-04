

try:
   fh = open("testfile.txt", "r")
   fh.write("This is my test file for exception handling!!")
finally:
   print "Error: can\'t find file or read data"


# More clean code.

try:
   fh = open("testfile.txt", "w")
   try:
      fh.write("This is my test file for exception handling!!")
   finally:
      print "Going to close the file"
      fh.close()
except IOError:
   print "Error: can\'t find file or read data"
