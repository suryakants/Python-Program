# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print "Read String is : ", str

str1 = fo.read(10);
print "Read String is : ", str1


# Check current position
position = fo.tell();
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
print "Current file position : ", position
str = fo.read(10);
print "Again read String is : ", str
# Close opend file
fo.close()