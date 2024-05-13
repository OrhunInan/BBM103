import os

def read_inputs(input_file_name): # Reads input fike and divides it into a list of commands.    
    global current_dir_path
    reading_file_path = os.path.join(current_dir_path, input_file_name)
    with open(reading_file_path, "r") as f:
        commands = f.readlines()
    return commands
def name_create(input_command): # Reads "create" command and reformats given information to fit in patient_database.
    global patient_database
    info_list = input_command.replace("create ","").replace("\n","").split(", ") # Converts command to a format similar to patient_database
    if info_list[0] in patient_database[0]: # checks if patient is already in patient_database
        return "Patient " + info_list[0] + " cannot be recorded due to duplication.\n" 
    else: 
        for i in range(6): # ads patient to patient_database
            if i% 2 == 0:
                patient_database[i].append(info_list[i])
            elif i%3 == 0:
                patient_database[i].append(int(info_list[i].replace("/100000","")))
            else :
                patient_database[i].append(float(info_list[i]))
        return "Patient " + info_list[0] + " is recorded.\n"
def name_remove(input_command): # Reads "remove" command and removes given patient from from patient_database.
    global patient_database
    global final_printed_text
    name = input_command.replace("\n","").split(" ")[-1] # Gets patients name.
    if name in patient_database[0]:
        num = patient_database[0].index(name) # Removes patient from patient_database.
        for i in patient_database:
            i.pop(num)
        return "Patient " + name + " is removed.\n"
    else :
        return "Patient " + name + " cannot be removed due to absence.\n"
def name_probability(input_command): # reads "probability" command and prints given patient's probability of having cancer.
    global patient_database
    global final_printed_text
    name = input_command.replace("\n","").split(" ")[-1] # Gets patient's name.
    if name in patient_database[0]:
        name_probability_calculate(name)
        text = "Patient " + name + " has a probability of "
        prob = round(name_probability_calculate(name)*100,2) # Reformats probability.
        if int(prob) == prob :
            text += str(int(prob))
        else :
            text += str(prob)
        text += "% of having " + patient_database[2][patient_database[0].index(name)].lower() + ".\n"
        return text
    else :
        return "Probability for " + name + " cannot be calculated due to absence.\n"
def name_probability_calculate(patient_database_name): # Calculates given patient's probability of having cancer.
    global patient_database
    incidence = patient_database[3][patient_database[0].index(patient_database_name)]
    accuracy = patient_database[1][patient_database[0].index(patient_database_name)]
    healthy = ((10 ** 5) - incidence) / (10 ** 5)
    cancerous = incidence / (10 ** 5)
    probability = (cancerous * accuracy) / ((healthy * (1 - accuracy)) + (cancerous * accuracy))
    return probability
def name_recommendation(input_command): # Calculates if treatment is reasonable for given patient 
    global patient_database
    global final_printed_text
    name = input_command.replace("\n","").split(" ")[-1]
    if name in patient_database[0]:
        if patient_database[5][patient_database[0].index(name)] > name_probability_calculate(name): # Compares treatment risk with probability of patient having cancer.
            return "System suggests " + name + " NOT to have the treatment.\n"
        else :
            return "System suggests " + name + " to have the treatment.\n"
    else:
        return "Recommendation for " + name + " cannot be calculated due to absence.\n"
def print_list(): # Prints patient_database to output text file.
    global patient_database
    list = "Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\n"
    list += "Name\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk\n"
    list += "-" * 73 + "\n"
    for q in range(len(patient_database[0])): # Prints patients.
        list += patient_database[0][q] + "\t" * (2 - (len(patient_database[0][q]) // 4))
        list += str(patient_database[1][q]*100) 
        if len(str(patient_database[1][q]*100)) == 4:
            list += "0"
        list += "%\t\t"
        list += patient_database[2][q] + "\t" * (4 - (len(patient_database[2][q]) // 4))
        list += str(patient_database[3][q]) + "/100000\t"
        list += patient_database[4][q] + "\t" * (4 - (len(patient_database[4][q]) // 4))
        list += str(int(patient_database[5][q]*100)) + "%\n"

    
    return list
def write_outputs(command_list,output_file): # Function for going through commands and printing outputs of the said commands.
    global current_dir_path
    writing_file_path = os.path.join(current_dir_path, output_file)
    with open(writing_file_path,"w") as output:
        for i in command_list: # Checks which commands will be runned at which order.
            if "create" in i:
                output.write(name_create(i))
            elif "remove" in i:
                output.write(name_remove(i))
            elif "probability" in i:
                output.write(name_probability(i))
            elif "recommendation" in i:
                output.write(name_recommendation(i))
            elif "list" in i:
                output.write(print_list())

current_dir_path = os.getcwd()
patient_database = [[],[],[],[],[],[]] # Multidimesional list for recording patients. Lines stores informatin in the order given by "create" function.
write_outputs(read_inputs("doctors_aid_inputs.txt"),"doctors_aid_outputs.txt")