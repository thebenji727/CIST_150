#with open("write_test.txt", 'w') as file_obj:
#    file_obj.write("writing")

with open('sample_text', 'r') as read_obj:
    with open('sample_text_copy', 'a') as write_obj:
        write_obj.write('\n'+'rewriting again and again')
        #for line in read_obj:
        #    write_obj.write(line)

