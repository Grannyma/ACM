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

# def displayMenu(menuOption):
#     print("------------------------------------------")
#     print("         Welcome to Admin Access          ")
#     print("------------------------------------------")
#     print("Please chose an option:")
#     print("[1] Transfer Ownership of an object ")
#     print("[2] Grant rights to a subject")
#     print("[3] Delete rights to an object ")
#     print("[4] Modify object(s)")
#     print("[5] Modify Subject(s)")
#     print("[0] Go back")

#Defines the variables for userid, password, and role
class ACM:
    def __init__(self,u,p,r):
        self.userInp = u
        self.passInp = p
        self.roles = r

#reads through the userList to check if menu option is accessable
def readUserList(role):
    access = False
    for i in userList:
        if i == role:
            access = True
            print("Access Granted")
    if access == False:
        print("Access Denied")


#parses the input at provides access rights dependent on roles
def switch(result):
    if result == 1:
        activeRole = 'admin'
        return readUserList(activeRole)
    elif result == 2:
        activeRole = 'author'
        return readUserList(activeRole)
    elif result == 3:
        activeRole = 'ae'
        return readUserList(activeRole)
    elif result == 4:
        activeRole = 'editor'
        return readUserList(activeRole)
    elif result == 5:
        activeRole = 'reviewer'
        return readUserList(activeRole)
    elif result == 0:
        print("Logging out...")
        exit()
    else:
        print("Not a valid input, please try again!")
        readInput = int(input())

print(switch(readInput))
acm1 = ACM(user, passI, userList)
#print(acm1.passInp)
#print(acm1.listing)