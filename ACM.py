#By: Tiffany Peck and Noah Coley
#Last Modified: 12/04/22
#
#
#Instructions
#1. To run the file, use CMD or Anaconda(python test1.py) to run the file
#2. enter in any user information from the 'datafile.csv' file
#3a. Try to access an option within the users capabilities
#3b. Try to access an option outside the users capabilities

from test1 import userList #get list value from test1
from test1 import readInput #get input value from test1

#Defines the acm object
class ACM:
    def __init__(self, r):
        self.roles = r

#Creates an acm object with userList(roles)
acm1 = ACM(userList)

#displays simple menu to show users they have gained acces to the function
def displayMenu(role):
    print("------------------------------------------")
    print("         Welcome to {} Access          ".format(role))
    print("------------------------------------------")
    print("There are no functionalities attached to \nthis but thank you for downloading!")

#reads through the userList to check if menu option is accessable
def readUserList(role):
    access = False
    for i in acm1.roles:
        if i == role:
            access = True
            print("Access Granted")
            displayMenu(role)
    if access == False:
        print("Access Denied")

#restarts user input for switch
def restart():
    readInput = int(input())
    return switch(readInput)

#parses the input at provides access rights dependent on the role(s)
def switch(result):
    if result == 1:
        activeRole = 'admin' #defines a string for the role
        return readUserList(activeRole) #returns output if role is in userList
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
        exit() #exits terminal
    else:
        print("Not a valid input, please try again!")
        restart() #Ask for new input

switch(readInput)
