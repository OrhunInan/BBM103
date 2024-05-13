numbers = [int(i) for i in input("please input list as comma seperated elements: ").split(", ")].sort(reverse = True)
nth_element = int(input("please input a number: "))
print(numbers[nth_element-1])