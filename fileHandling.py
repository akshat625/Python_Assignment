with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

print("\n------------------------------------------------------------------------------------------------------------------------")

with open("words.txt", "r") as file:
    text = file.read()
    word_count = len(text.split())
    print("Number of words:", word_count)

print("\n------------------------------------------------------------------------------------------------------------------------")

with open("output.txt", "w") as file:
    file.write("Hello, Python!")

print("Data written to output.txt")

print("\n------------------------------------------------------------------------------------------------------------------------")

import csv

data = [
    ["Name", "Roll Number", "Marks"],
    ["Alice", "101", "85"],
    ["Bob", "102", "90"],
    ["Charlie", "103", "88"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("students.csv file created successfully")

print("\n------------------------------------------------------------------------------------------------------------------------")

def read_large_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


for line in read_large_file("large_file.txt"):
    print(line)

