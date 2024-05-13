b=int(input("b:" ))
c= int(input("c:"))
delta= ((b**2)-(4*c))
ddbt= (delta**(1/2))/2 #delta divided y two
rest= (b/2) # rest of the formula
if delta < 0:
    print("there is no real root for formula.")
else:
    print("""roots of the formula is "{}" and "{}".""".format(rest+ddbt,rest-ddbt))