# This program requires the files to be in the same directory as the python file.
# The python file will overwrite any files that result from the conversion of ':' to '-'.
# The program first gets a list of strings that are all the files in the directory.
# The program then iterates through the list and checks for file names with ':' in them.
# The program then replaces ':' with '-' and copies the old file with the new filename.
# Program is made to run with python 3.6 or higher due to print statement.

import os
import shutil

currDir = os.getcwd()

dirList = os.listdir(currDir)

print(" ")
#print(currDir)
#print(dirList)

numAttempted = 0;
numChanged = 0;

for i in dirList:
    #print(':' in i)
    numAttempted = numAttempted + 1
    if (':' in i):
        #print("True")
        #print(i.replace(":", "-"))
        shutil.copyfile(i, i.replace(":", "-"))
        numChanged = numChanged + 1
    #else:
        #print("False")
        #print(i)
print("Completed. Changed ", numChanged, " out of ", numAttempted, " files in local folder.")
