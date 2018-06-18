# Server program

import socket   					# Import socket module

s = socket.socket();  				# Create socket object
host = socket.gethostname()				## Get local machine name
port = 12345						# reserve a port for your service
s.bind((host, port)); 				# Bind to the port


s.listen(5)							# Now wait for client connection.

while True:
	c, address = s.accept(); 		# Establish connection with client.
	print ('Got connection from', address)
	c.send("Thank you for connecting")
	c.close()                		# Close the connection

