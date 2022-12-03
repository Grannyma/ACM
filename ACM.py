#By: Tiffany Peck and Noah Coley
#Last Modified: 12/03/22 3:35PM
#
#
#Instructions
#1. To run the file, use CMD or Anaconda(python test1.py) to run the file
#2.
import test1
from test1 import user #get user value from test1
from test1 import passI #get pass value from test1
from test1 import userList #get list value from test1
from test1 import readInput #get input value from test1

class ACM:
    def __init__(self,u,p,l):
        self.userInp = u
        self.passInp = p
        self.listing = l
    def switch(read):
        if read == 1:
            return "You can become a web developer."
        elif read == 2:
            return "You can become a backend developer."
        elif read == 3:
            return "You can become a Data Scientist"
        elif read == 4:
            return "You can become a Blockchain developer."
        elif read == 5:
            return "You can become a mobile app developer"
acm1 = ACM(user, passI, userList)
swtich(readInput)
#print(acm1.userInp)
#print(acm1.passInp)
#print(acm1.listing)