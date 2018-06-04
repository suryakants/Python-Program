
# Open a file
fo = open("foo11.txt", "wb")
fo.write( "Python is a great language.\nYeah its great!!\n");

# Close opend file
fo.close()
del fo;


# Open a file
fo = open("foo00.txt", "r+")
str = fo.read(10000);
print "Read String is : ", str
# Close opend file
fo.close()
del fo;

fo = open("foo.txt", "a");
fo.write("See! this is just an eample of Python file input/output, so just chill!!! \n understand!!!")



# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10000);
print "Read String is : ", str
# Close opend file
fo.close()
del fo;