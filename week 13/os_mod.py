import os

print((os.getcwd()))
#change to a different directory
## List all files at the current location
os.chdir('C:\\Users\\beg91\\CIST 150')   ## Double the \s in the directory
print(os.listdir())

## mkdir ---. create a single directory
## makedirs --> used to create a hierarchy of directories

#os.mkdir('Test_Dir')
#os.makedirs("Test_Dir1\\sub1\\sub2")
#os.rmdir('Test_Dir')
#os.removedirs("Test_Dir1\\sub1\\sub2")