number = int(input("please input an intager"))
aritmetic = 0
sum = 0
for i in range(1,number+1):
    if i%2!=0:
        sum+=i
    else:
        aritmetic+=i
aritmetic = aritmetic / int((number/2))
print("sum of odds is {}, mean of evens is {}.".format(sum,aritmetic))