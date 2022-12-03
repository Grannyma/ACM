#By: Tiffany Peck and Noah Coley
#Last Modified: 12/02/22
#
#
#Instructions
#1. To run the file, use CMD or Anaconda(python test1.py) to run the file
#2.
import pandas as pd
import numpy as np
import test1
from test1 import user #get user value from test1
from test1 import passI #get pass value from test1
from test1 import userList #get list value from test1
datafile = pd.read_csv("datafile.csv") # to read csv file named
class ACM:
    def __init__(self,u,p,l):
        self.userInp = u
        self.passInp = p
        self.listing = l
acm1 = ACM(user, passI, userList)
print(acm1.userInp)
print(acm1.passInp)
print(acm1.listing)