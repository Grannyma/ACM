#By: Tiffany Peck and Noah Coley
#Last Modified: 12/03/22 3:35PM
#
#
#Instructions
#1. To run the file, use CMD or Anaconda(python test1.py) to run the file
#2.
from test1 import userList #get list value from test1
from test1 import readInput #get input value from test1

#Defines the variables for userid, password, and role
class ACM:
    def __init__(self, r):
        self.roles = r

acm1 = ACM(userList)
print(acm1.roles)

#reads through the userList to check if menu option is accessable
def readUserList(role):
    access = False
    for i in userList:
        if i == role:
            access = True
            print("Access Granted")
            displayMenu(role)
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

def displayMenu(role):
    print("------------------------------------------")
    print("         Welcome to {} Access          ".format(role))
    print("------------------------------------------")
    print("There are no functionalities attached to \n this but thank you for downloading!")

print(switch(readInput))