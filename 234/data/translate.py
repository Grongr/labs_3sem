#! Inputs file 'data.dat' 
import sys

error_param = 0

FILE_NAME = sys.argv[1]

fi = open("./" + FILE_NAME, "r")
fo = open("./translated/" + FILE_NAME, "w")

inp = fi.readlines()

for i in range(len(inp)):
        inp[i] = inp[i].replace(",", ".")

for i in inp:
    a = str(i).split()
    if len(a) >= 2:
        fo.write(a[0] + " " + a[1] + "\n")

fi.close()
fo.close()

if error_param == 0:
    print("File ./translated/" + FILE_NAME + " was generated correctly")
