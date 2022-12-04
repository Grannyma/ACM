#By: Tiffany Peck and Noah Coley
#Last Modified: 12/03/22 3:35PM
#
#
#Instructions
#1. To run the file, use CMD or Anaconda(python test1.py) to run the file
#2.
import test1
import csv
from test1 import user #get user value from test1
from test1 import passI #get pass value from test1
from test1 import userList #get list value from test1
from test1 import readInput #get input value from test1
readInput = int(readInput)

# target = ''
# msg = ''
# def roleSearch(userRoles):
#     userRoles = csv.reader(userList)
#     for roles in userRoles:
#         if roles == target:
#             return msg

class ACM:
    def __init__(self,u,p,r):
        self.userInp = u
        self.passInp = p
        self.roles = r

def switch(result):
    if result == 1:
        return "You can become a web developer."
    elif result == 2:
        return "You can become a backend developer."
    elif result == 3:
        return "You can become a Data Scientist"
    elif result == 4:
        return "You can become a Blockchain developer."
    elif result == 5:
        return "You can become a mobile app developer"

acm1 = ACM(user, passI, userList)
print(switch(readInput))
#print(acm1.passInp)
#print(acm1.listing)