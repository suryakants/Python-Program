#!/usr/bin/python

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

   globalContent = globals();
   print "Global content : ", globalContent
   print "\n"
   localContent = locals();
   print "local content : ", localContent


#print Money
AddMoney()
#print Money
print "\n\n"
globalContent = globals();
print "Global content : ", globalContent
print "\n"

localContent = locals();
print "local content : ", localContent