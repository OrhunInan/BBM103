import os
import sys


current_dir_path = os.getcwd()
message_codes = []
messages = {}
reading_file_path = os.path.join(current_dir_path, sys.argv[1])
f = open(reading_file_path, "r")
writing_file_path = os.path.join(current_dir_path, sys.argv[2])

for i in f.readlines():

    info = i.split("\t")
    
    if info[0] not in messages:
        
        messages[info[0]] = {}
        message_codes.append(info[0])

    messages[info[0]][info[1]] = info[2].replace("\n", "")

f.close()
message_codes.sort()
   
with open(writing_file_path,"w") as output:

    for j in range(len(messages)):

        output.write("Message\t{}\n".format(j+1))

        for k in range(len(messages[message_codes[j]])):
            output.write("{}\t{}\t{}\n".format(message_codes[j], k, messages[message_codes[j]][str(k)]))
