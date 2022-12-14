#By: Tiffany Peck and Noah Coley
#Last Modified: 12/04/22
#
#
import pandas as pd
import numpy as np
file = pd.read_csv("datafile.csv") # to read csv file named


print("-----------------------------------------")
print("                  WELCOME!               ")
print("          TO THE EDITORIAL MANAGEMENT    ")
print("                   SYSTEM                ")
print("-----------------------------------------")

#enter login information
user = input("Enter User: ")
found = False
foundPass = False
userList = []
indexofUser=0

#Finding the username in csv
while not found:
 for i in file['userid']:
  if(i==user):
   found=True
   indexofUser = file[file['userid']==i].index.values
 if found:   
    userList = file.iloc[indexofUser, 2]
    break
 print("Not Found..")
 user = input("Enter User: ")

#Finding the pass in csv
passI = input("Enter Pass: ")
while not foundPass:
 for z in file['passid']:
  if(z==passI):
   foundPass=True
 if foundPass:   
    break
 print("Not Found..")
 passI = input("Enter Pass: ")

#Splitting the userList so it accepts the roles as seperate elements
userList = [item.split(', ') for item in userList]
userList = [item for l in userList for item in l]
print("SUCCESS!!")
print("------------------------------------------")
print("                  MENU               ")
print("Welcome "+ user) #display username
print("Your roles are:", *userList) #display roles
print("")

#Menu Options
print("[1] Admin Access ") #admins only
print("[2] Manuscripts") #author only
print("[3] Invites ") #ae only
print("[4] Score Review") #editors only
print("[5] See Review ") #reviewers only
print("[0] Log Out")
readInput = int(input())
#print("----------------------------------------")