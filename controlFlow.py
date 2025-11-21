num = int(input("Please enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")


print("\n------------------------------------------------------------------------------------------------------------------------\n")

str1 = 'civics'
str2 = 'hello'
reverseStr = ''
for s in str1:
    reverseStr = s + reverseStr
if str1 == reverseStr:
    print(str1, "is palindrome.")
else:
    print(str1, "is not palindrome.")

print("\n------------------------------------------------------------------------------------------------------------------------\n")

num = int(input("Please enter a number: "))
first = 0
second = 1
for i in range(num):
    print(first, end=" ")
    first, second = second, first + second


print("\n------------------------------------------------------------------------------------------------------------------------\n")

a = [1, 2, 3, 4, 5]

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] + a[j] == 9:
            print([a[i], a[j]])


print("\n------------------------------------------------------------------------------------------------------------------------\n")

i = 1

while i <= 20:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1


print("\n------------------------------------------------------------------------------------------------------------------------\n")

numbers = [10, 20, 30, 40, 50]
search_for = 30
index = -1
for n in numbers:
    index = index + 1
    if n == search_for:
        print("Found:", n, "at index ", index)

        break


print("\n------------------------------------------------------------------------------------------------------------------------\n")

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")


print("\n------------------------------------------------------------------------------------------------------------------------\n")

for i in range(5):
    if i == 3:
        pass
    print(i, end=" ")
#there is no effect of pass, above loop prints number from 0 to 4

print("\n------------------------------------------------------------------------------------------------------------------------\n")

day = input("Enter day of the week: ").lower().strip()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")

