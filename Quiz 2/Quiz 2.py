import sys

try :
    twos = int(sys.argv[1])
    threes = int(sys.argv[2])
    ones = int(sys.argv[3])
    total= str(twos*2+threes*3+ones) #adding up all points
    sys.stdout.write(total)

except:
    def healthStatus(meters,kilos):
        bmi = kilos/(meters**2)
        if bmi >= 30: # checking where bmi lands
            return 'obese'
        elif bmi >= 24.9:
            return 'overweight'
        elif bmi >= 18.5:
            return 'healty'
        else :
            return 'underweight'
# Orhun İnan
