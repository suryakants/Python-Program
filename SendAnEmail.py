#Send a email

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
	smtpObj = smtplib.SMTP('localhost');
	smtplib.sendmail(sender, receivers, message);
	print("success");
except SMTPException:
   print ("Error: unable to send email")
