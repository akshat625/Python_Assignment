numbers = [1, 2, 3, 4, 5]

all_positive = all(num > 0 for num in numbers)
print(all_positive)

print("\n------------------------------------------------------------------------------------------------------------------------")

numbers = [1, 3, 5, 7, 8]

any_even = any(num % 2 == 0 for num in numbers)
print(any_even)

print("\n------------------------------------------------------------------------------------------------------------------------")

numbers = [1, 3, 7, 11, 15, 18]

divisible_by_five = any(num % 5 == 0 for num in numbers)
print(divisible_by_five)

