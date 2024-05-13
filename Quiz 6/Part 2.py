import sys


number = int(sys.argv[1])
list_of_stars = [["*" for j in range(2*(i+1)-1)] if i < number else ["*" for j in range(2*(2*number-i)-3)] for i in range(2 * number - 1)]
for i in range(2*number-1):
    print((" "*(number-i-1)) if i < number else " "*(i-number+1) , end= "")
    print(*list_of_stars[i], sep="")