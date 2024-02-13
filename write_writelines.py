### Write string content which is referenced to file object

file1  = open("Document1.txt", "w")
for i in range(3):
    name = input("Enter name: ")
    file1.write(name)
    file1.write("\n")

file1.close()

print("Data written")


### Write all string content which is exist in list that is referenced to file object

file2 = open("Document2.txt", "w")
cars = []
for item in range(3):
    car = input("Enter Car Name:")
    cars.append(car + "\n")

file2.writelines(cars)
file2.close()
print("Written All Cars")