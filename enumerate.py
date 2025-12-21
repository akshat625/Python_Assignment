fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)

print("\n------------------------------------------------------------------------------------------------------------------------")

person = {"name": "Alice", "age": 30, "city": "New York"}
for index, (key, value) in enumerate(person.items()):
    print(key, value)

print("\n------------------------------------------------------------------------------------------------------------------------")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
result = [(index, value) for index, value in enumerate(fruits, start=1) if index % 2 == 0]
print(result)

