def pod1s():
    global i
    global NOP
    if len(pod1) == 0:
        NOP += 1
        pod2s()
    elif len(pod2) == 0 or pod1[-1] < pod2[-1]:
        print("Move disk {} from source A to destination B".format(pod1[-1]))
        pod2.append(pod1[-1])
        pod1.pop()
        i += 1
        NOP +=2
    elif len(pod3) == 0 or pod1[-1] < pod3[-1]:
        print("Move disk {} from source A to destination C".format(pod1[-1]))
        pod3.append(pod1[-1])
        pod1.pop()
        i += 1
        NOP += 3
    else :
        NOP += 1
        pod2s()
def pod2s():
    global i
    global NOP
    if len(pod2) == 0:
        NOP += 1
        pod3s()
    elif len(pod3) == 0 or pod2[-1] < pod3[-1]:
        print("Move disk {} from source B to destination C".format(pod2[-1]))
        pod3.append(pod2[-1])
        pod2.pop()
        i += 1
        NOP +=2
    elif len(pod1) == 0 or pod2[-1] < pod1[-1]:
        print("Move disk {} from source B to destination A".format(pod2[-1]))
        pod1.append(pod2[-1])
        pod2.pop()
        i += 1
        NOP += 3
    else :
        NOP += 1
        pod3s()
def pod3s():
    global i
    global NOP
    if len(pod3) == 0:
        NOP += 1
        pod1s()
    elif len(pod1) == 0 or pod3[-1] < pod1[-1]:
        print("Move disk {} from source C to destination A".format(pod3[-1]))
        pod1.append(pod3[-1])
        pod3.pop()
        i += 1
        NOP +=2
    elif len(pod2) == 0 or pod3[-1] < pod2[-1]:
        print("Move disk {} from source C to destination B".format(pod3[-1]))
        pod2.append(pod3[-1])
        pod3.pop()
        i += 1
        NOP += 3
    else :
        NOP += 1
        pod1s()

number = int(input("please input how many discs there are: "))
count = 2 ** number -1
i = 0
NOP = 1
pod1 = [i for i in range(number,0,-1)]
pod2 = []
pod3 = []
while i < count:
    if NOP % 3 == 1:
        pod1s()
    elif NOP % 3 == 2:
        pod2s()
    else :
        pod3s()