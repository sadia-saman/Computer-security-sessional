from BitVector import *
from math import *
import os
 
directory = "Don't Open this"
parent_dir  = os.getcwd() 
new_dir = os.path.join(parent_dir, directory)
file = new_dir + '/myfile.txt'

check = os.path.exists(file)
print(check,file)

