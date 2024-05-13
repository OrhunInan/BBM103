number=int(input())
if number%400==0:
    print("{} year is a leap year".format( number))
elif number%100==0:
    print("{} year is not a leap year".format( number))
elif number%4==0:
    print("{} year is a leap year".format( number))
else:
    print("{} year is not a leap year".format( number))




