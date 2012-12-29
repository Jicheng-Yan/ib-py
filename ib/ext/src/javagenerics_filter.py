#!/usr/bin/python

# The Interactive Brokers API (version 9.65) uses the Vector "Generic" class in Order.java. In later verions of the API this is used even more.
# As a sidenote, it has been recommend against using the Vector class, as it is deprecated. Instead, it is suggested to use ArrayList.

# In any event, java2python r50 seems not to be able to deal with substitution of only Vector not Vector Generic
# e.g. adding this to the cfg/Order.py doesn't seem to work

#typeTypeMap = {
#    'Vector<TagValue>':'list',
#}

# So we will just modify the source code and run this from the make file which downloads the API java source

import re, os, fnmatch

def replace(file, pattern, subst):
    # Read contents from file as a single string
    file_handle = open(file, 'r')
    file_string = file_handle.read()
    file_handle.close()

    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_string = (re.sub(pattern, subst, file_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_handle = open(file, 'w')
    file_handle.write(file_string)
    file_handle.close() 

if __name__ == "__main__":
    javadir='./IBJts/java/com/ib/client/'
    dirlist=os.listdir(javadir)
    for i in dirlist:
        if fnmatch.fnmatch(i,"*.java"):
            replace(javadir+i,"Vector<TagValue>","Vector")



