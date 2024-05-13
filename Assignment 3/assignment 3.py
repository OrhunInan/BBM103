import os
import sys


def read_inputs(input_file_name): # Reads input file and divides it into a list of commands.    
    
    global current_dir_path
    reading_file_path = os.path.join(current_dir_path, input_file_name)
    
    with open(reading_file_path, "r") as f:
        
        commands = f.readlines()
    
    return commands

def write_outputs(command_list,output_file): # Function for going through commands and printing outputs of the said commands.
    
    global current_dir_path
    writing_file_path = os.path.join(current_dir_path, output_file)
    
    with open(writing_file_path,"w") as output:
        
        for i in command_list: # Checks which commands will be runned at which order.
            
            if "CREATECATEGORY" in i:
                
                to_be_printed = CREATECATEGORY(i)

            elif "SELLTICKET" in i:
                
                to_be_printed = SELLTICKET(i)
            
            elif "CANCELTICKET" in i:
                
                to_be_printed = CANCELTICKET(i)
            
            elif "BALANCE" in i:
                
                to_be_printed = BALANCE(i)
            
            elif "SHOWCATEGORY" in i:
                
                to_be_printed = SHOWCATEGORY(i)

            print(to_be_printed[:-2]) # Removed last 2 chars since print function already prints '\n' and every string's last 2 chars is '\n'.
            output.write(to_be_printed)

def CREATECATEGORY(input_command): # Reads "CREATECATEGORY" command and reformats given information to fit in stadium_database.
    
    global stadium_database
    info_list = input_command.replace("CREATECATEGORY ","").replace("\n","").split(" ") # Converts command to a list of information.
    
    if info_list[0] in stadium_database: # checks if section is already in stadium_database.
    
        return "Warning: Cannot create the category for the second time. The stadium has already " + info_list[0] + "\n"
    
    else: 
        
        number_of_rows_and_columns = [int(u) for u in info_list[1].split("x")] # Creates a list of rows and columns. index 0 is rows and index 1 is columns.
        stadium_database[info_list[0]] = [["X" for d in range(number_of_rows_and_columns[1])] for q in range(number_of_rows_and_columns[0])] # Adds specified section to database.

        return "The category '" + info_list[0] + "' having " + str(number_of_rows_and_columns[0] * number_of_rows_and_columns[1]) + " seats has been created\n"

def SELLTICKET(input_command): # Reads "SELLTICKET" command and changes database according to salesmade in the command.
    
    global stadium_database
    global alphabet
    final_string = "" # This string is for returning all ticket sales at once.
    ticket_types = { "student" : "S", "full" : "F", "season" : "T"} # changes info to fit into our ddatabase.
    can_be_sold = True
    info_list = input_command.replace("SELLTICKET ","").replace("\n","").split(" ") # Converts command to a list of information.

    for g in range(3,len(info_list)): # Runs through all of the seats in command.
        
        if alphabet[info_list[g][0].upper()] < len(stadium_database[info_list[2]]): # Checks if the number given does exists at given category
        
            if "-" in info_list[g]: # Checks if multiple seats can be sold at once.
            
                through = [ int(y) for y in info_list[g][1:].split("-")] # Reformats range seats for loops.
            
                if through[1] < len(stadium_database[info_list[2]][alphabet[info_list[g][0]]]) : # Checks if there are enough rows.
                    for c in range(through[0], through[1] + 1): # Checks if the seats are empty in the given row and columns.
                
                        if stadium_database[info_list[2]][alphabet[info_list[g][0]]][c] != "X": # checks if the seats are empty.

                            final_string += "Warning: The seats " + info_list[g] + " cannot be sold to " + info_list[0] + " due some of them have already been sold\n"
                            can_be_sold = False
                            break
            
                    if can_be_sold:

                        for u in range(through[0], through[1] + 1): # Sells the seats in range.
                    
                            stadium_database[info_list[2]][alphabet[info_list[g][0]]][u] = ticket_types[info_list[1]]
                
                        final_string += "Success: " + info_list[0] + " has bought " + info_list[g] + " at " + info_list[2] + "\n"

                    can_be_sold = True
                else:

                    final_string += "Error: The category '" + info_list[2] + "' has less column than the specified index " + info_list[g] + "!\n"
            
                through.clear()

            else:

                if stadium_database[info_list[2]][alphabet[info_list[g][0]]][int(info_list[g][1:])] == "X": # Checks if the seat is empty.

                    stadium_database[info_list[2]][alphabet[info_list[g][0]]][int(info_list[g][1:])] = ticket_types[info_list[1]] # Sells the seat.
                    final_string += "Success: " + info_list[0] + " has bought " + info_list[g] + " at " + info_list[2] + "\n"
            
                else : 
                
                    final_string += "Warning: The seat " + info_list[g] + " cannot be sold to " + info_list[0] + " since it was already sold!\n"
        
        else: # This part determines whether only rows are out of range or both rows and columns are out of range. After the check it raises appropriate error.
            
            test = int(info_list[g].split("-")[-1]) if "-" in info_list[g] else int(info_list[g][1:]) # Checks if multiple seats can be sold at once.
                 
            if test < len(stadium_database[info_list[2]][0]):
                
                final_string += "Error: The category '" + info_list[2] + "' has less row than the specified index " + info_list[g] + "!\n"

            else:
                
                final_string += "Error: The category '" + info_list[2] + "' has less row and column than the specified index " + info_list[g] + "!\n"

    
    return final_string

def CANCELTICKET(input_command): # Reads "CANCELTICKET" command and removes given tickets if a) tickets exists b) tickets have been sold to someone.

    global stadium_database
    global alphabet
    final_string = "" # This string is for returning all ticket cancelations at once.
    info_list = input_command.replace("CANCELTICKET ","").replace("\n","").split(" ") # Converts command to a list of information.

    for s in range(1,len(info_list)):

        if alphabet[info_list[s][0]] < len(stadium_database[info_list[0]]) and int(info_list[s][1:]) < len(stadium_database[info_list[0]][0]): # checks if the seat exists.

            if stadium_database[info_list[0]][alphabet[info_list[s][0]]][int(info_list[s][1])] != "X": # Checks if the seat is empty.

                stadium_database[info_list[0]][alphabet[info_list[s][0]]][int(info_list[s][1])] = "X" # cancels ticket.
                final_string += "Success: The seat " + info_list[s] + " at " + info_list[0] + " has been canceled and now ready to sell again\n"

            else:

                final_string += "Error: The seat " + info_list[s] + " at " + info_list[0] + " has already been free! Nothing to cancel\n"

        else: # # This part determines whether rows, columns or both of them are out of range. After the check it raises appropriate error.

            if alphabet[info_list[s][0]] < len(stadium_database[info_list[0]]):

                final_string += "Error: The category '" + info_list[0] + "' has less column than the specified index " + info_list[s] + "!\n"
            
            elif info_list[s][1] < len(stadium_database[info_list[0]][0]):

                final_string += "Error: The category '" + info_list[0] + "' has less row than the specified index " + info_list[s] + "!\n"
            
            else:

                final_string += "Error: The category '" + info_list[0] + "' has less column and row than the specified index " + info_list[s] + "!\n"

    return final_string

def SHOWCATEGORY(input_command):

    global stadium_database
    global alphabet
    info_list = input_command.replace("SHOWCATEGORY ","").replace("\n","") # Converts command to a list of information.
    final_string = "Printing category layout of " + info_list + "\n\n" # This string is for returning one return that contains all of the information at once.
    reverse_alphabet = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    if info_list in stadium_database: # checks if the category exists.
    
        for a in range(len(stadium_database[info_list])-1, -1, -1): # runs through rows backwards.
        
            final_string += reverse_alphabet[a] + " " # Puts the letters.
        
            for u in range(len(stadium_database[info_list][0])): # prints the seats in the row.

                final_string += stadium_database[info_list][a][u] + "  "  if u != len(stadium_database[info_list][0]) - 1 else stadium_database[info_list][a][u] + "\n"
    
        for l in range(0, len(stadium_database[info_list][0])): # puts columns name.

            final_string += "%3s"%(str(l))
            
    
        final_string += "\n"

        return final_string

    else :
        
        return "Category '" + info_list + "' doesn't exist."

def BALANCE(input_command):

    global stadium_database
    global alphabet
    final_string = ""
    info_list = input_command.replace("BALANCE ","").replace("\n","") # Converts command to a list of information.

    if info_list in stadium_database: # checks if the category exists.
    
        students = sum([i.count("S") for i in stadium_database[info_list]]) # Number of student tickets.
        fulls = sum([i.count("F") for i in stadium_database[info_list]]) # Number of full tickets.
        seasons = sum([i.count("T") for i in stadium_database[info_list]]) # Number of season tickets.

        final_string += "category report of '" + info_list + "'\n" # Returns the information in the desired format.
        final_string += "-------------------------------\n"
        final_string += "Sum of students = " + str(students)
        final_string += ", Sum of full pay = " + str(fulls)
        final_string += ", Sum of season ticket = " +str(seasons)
        final_string += ", and Revenues = " + str((students * 10) + (fulls * 20) + (seasons * 250)) + " Dollars\n"

    else:
        final_string = "Category '" + info_list + "' doesn't exist."

    return final_string


alphabet = { "A" :  0, "B" :  1, "C" :  2, "D" :  3, "E" :  4, "F" :  5, "G" :  6, "H" :  7, "I" :  8, "J" :  9, # A dictionary for giving intager values to letters.
             "K" : 10, "L" : 11, "M" : 12, "N" : 13, "O" : 14, "P" : 15, "Q" : 16, "R" : 17, "S" : 18, "T" : 19,    
             "U" : 20, "V" : 21, "W" : 22, "X" : 23, "Y" : 24, "Z" : 25 } 
current_dir_path = os.getcwd()
stadium_database = {} # dictionary of lists for recording categorys and seats.

write_outputs(read_inputs(sys.argv[1]),"output.txt") # Execution of inputs.