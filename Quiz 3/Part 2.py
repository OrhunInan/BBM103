import sys

numbers = [int(i) for i in sys.argv[1].replace("\"","").split(",")]
counter = 1
to_be_popped = [i for i in range(len(numbers)) if numbers[i] < 0]
to_be_popped.reverse()
for j in to_be_popped:
    numbers.pop(j)
while numbers[counter] < len(numbers):
    mini_counter = numbers[counter]
    control = numbers[counter]
    to_be_popped.clear()
    while mini_counter <= len(numbers):
        to_be_popped.append(mini_counter)
        mini_counter += numbers[counter]
    to_be_popped.reverse()
    for q in to_be_popped:
        numbers.pop(q-1)
    print(*numbers)
    if control == numbers[counter]:
        counter += 1