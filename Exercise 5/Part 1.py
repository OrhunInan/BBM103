num = int(input("Enter the number N value: "))
stars = {i: ["*" for j in range(i)] for i in range(1,num + 1)}
print(stars)