import sys


def karo(argument,step):
    if step == 2*argument-1:
        return (" " * (argument-1) + "*") 

    else:
        if step <= argument:
            return (" " * (argument - step) + ("*" * (2*step-1))+"\n") + karo(argument, step+1)

        else:
            return (" " * (step-argument) + ("*" * (2*(2*argument-step)-1)) + "\n") + karo(argument, step+1)

number = 6
print(karo(number,1))