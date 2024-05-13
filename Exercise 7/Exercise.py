import os
import sys


def create_students(input_file_name): 
    
    reading_file_path = os.path.join(os.getcwd(), input_file_name)
    
    with open(reading_file_path, "r") as f:
        
        students = f.readlines()
    
    return students

students_unformated = [i.replace("\n", "") for i in create_students(sys.argv[1])]
checks = sys.argv[2].split(",")
students_formated = {}

for i in students_unformated:
    temp_list = i.split(":")
    students_formated[temp_list[0]] = temp_list[1].split(",")

del temp_list, students_unformated

for j in checks:

    try:
        
        print("Name: {}, University: {}, {}".format(j,students_formated[j][0],students_formated[j][1]))

    except:

        print("No record of '{}' was found!".format(j))

