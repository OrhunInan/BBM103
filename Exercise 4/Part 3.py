import random
mistakes=4
print("guess a number between 1 and 25")
number = random.randint(1,25)
print(number)
guess=int(input("guess a number:"))
for i in range(mistakes):
    if guess==number:
        print("correct")
        break
    else:
        if guess>number:
            guess = int(input("decrease it"))
        else:
            guess = int(input("increase it"))