name = input("Please enter your name: ")
print("Welcome " + name)

print("\n------------------------------------------------------------------------------------------------------------------------\n")

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

print("Sum is", num1 + num2)
print("Multiplication is", num1 * num2)
print("Division is", num1 / num2)

print("\n------------------------------------------------------------------------------------------------------------------------\n")

names = input("Please enter multiple names separated by a comma: ")
nameList = names.split(",")
print(nameList)

print("\n------------------------------------------------------------------------------------------------------------------------\n")

age = input("Please enter your age: ")
if int(age) >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

print("\n------------------------------------------------------------------------------------------------------------------------\n")

print(f"{3.14159:.2f}")