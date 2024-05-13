number= int(input())
counter=0
result= ""
while(number!=0):
    counter +=1
    if (number%(2**counter)!=0):
        result+= "1"
        number= number-(2**(counter-1))
    else:
        result+="0"
for i in range((len(result)-1),-1,-1):
    print(result[i], end="")
