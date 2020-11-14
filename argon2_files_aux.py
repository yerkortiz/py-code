import glob
import os
import argon2
from argon2 import PasswordHasher
ph = argon2.PasswordHasher()
path = os.curdir
j = 0
f2 = open("argon2_files","w+")
for filename in glob.glob(os.path.join(path, 'crack_file*')):
    f = open(filename, 'r')
    print("Archivo " + filename)
    for l in f:
        if(j == 0):
            l = l[33:len(l) - 1]
        elif(j == 1 or j == 2):
            l = l[50:len(l) - 1]
        elif(j == 3):
            l = l[33:len(l) - 1]
        else:
            l = l[1:len(l) - 1]
        f2.write((ph.hash(l)) +'\n')
    j += 1
f2.close()
    

