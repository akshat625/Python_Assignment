a = [1, 2, 3, 4]
double = map(lambda x: x * 2, a)
print(list(double))

print("\n------------------------------------------------------------------------------------------------------------------------")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

print("\n------------------------------------------------------------------------------------------------------------------------")

from functools import reduce

words = ["apple", "banana", "cherry", "date"]
longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest_word)

print("\n------------------------------------------------------------------------------------------------------------------------")

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

squared_rounded = list(map(lambda x: round(x ** 2, 1), my_floats))
print(squared_rounded)

print("\n------------------------------------------------------------------------------------------------------------------------")

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

short_names = list(filter(lambda name: len(name) <= 7, my_names))
print(short_names)

print("\n------------------------------------------------------------------------------------------------------------------------")


numbers = [1, 2, 3, 4, 5]

total_sum = reduce(lambda a, b: a + b, numbers)
print(total_sum)

