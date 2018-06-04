
# try to open a file, where you do not have write permission, so it raises an exception

try:
   fh = open("testfile.txt", "r")
   # fh.write("This is my test file for exception handling!!")
   str = fh.read(10);
   print "Read String is : ", str

except IOError:
   print "Error: can\'t find file or read data"
# else:
#    print "Written content in the file successfully"