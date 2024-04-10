# open command
# with open -----> context manager        more recommended

# using open command
#with files: open in read mode, open in write mode, open in append mode
'''
file_obj = open('sample_text', 'r') # with open, default mode is read. using 'r' tells what mode you want to open the file in

print(file_obj.name)
print(file_obj.mode)


# NEED TO CLOSE THE FILE, OR IT WILL CAUSE PROBLEMS. Only needs to be done with open command, with open takes care of itself
file_obj.close()
'''

# with open ---->  cpntext management

with open('sample_text', 'r') as file_obj: #similar to the if blocks and for loops
    #print(file_obj.name)
    #print("Inside the with open:", file_obj. closed)
    #file_contents = file_obj.read()
    #print(file_contents)

#to access one line at a time
    #for line in file_obj:
    #    print(line)


#reads one line, in a sequence
    '''
    file_content = file_obj.readline()
    print(file_content)

    file_content = file_obj.readline()
    print(file_content)
    '''
#reads a number of characters, in a sequence, returns as a string. When there are no more characters to return, it returns as a string
    '''
    size_to_read = 10
    file_contents = file_obj.read(size_to_read)
    print(file_contents)

    file_contents = file_obj.read(size_to_read)
    print(file_contents)
    '''

    size_to_read = 10
    file_cont = file_obj.read(size_to_read)
    while len(file_cont) > 0:
        print(file_cont, end="*")
        file_cont = file_obj.read(size_to_read)

#print(file_obj.closed)