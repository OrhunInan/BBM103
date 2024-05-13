import sys
number1, number2 = int(sys.argv[1]),int(sys.argv[2])
control_number = number1 ** number2
printed_string = "{}^{} = {}".format(number1, number2, control_number)

while len(str(control_number)) != 1:
    printed_string += " = "
    control_number_as_list = []
    for i in range(len(str(control_number))):
        control_number_as_list.append(control_number % 10)
        control_number //= 10
    for j in range(len(control_number_as_list)-1,-1,-1):
        if j != 0:
            printed_string += "{} + ".format(control_number_as_list[j])
        else : 
            printed_string += "{} = {}".format(control_number_as_list[j],sum(control_number_as_list))
        control_number = sum(control_number_as_list)

sys.stdout.write(printed_string)
