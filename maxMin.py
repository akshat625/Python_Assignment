numbers = [1, 32, 63, 14, 5, 26, 79, 8, 59, 10]

max_val= max(numbers)
min_val = min(numbers)

print("Maximum:", max_val)
print("Minimum:", min_val)

print("\n------------------------------------------------------------------------------------------------------------------------")

setn = {5, 10, 3, 15, 2, 20}

max_val = max(setn)
min_val = min(setn)

print("Maximum:", max_val)
print("Minimum:", min_val)

print("\n------------------------------------------------------------------------------------------------------------------------")

def find_shortest_and_longest(words):
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    return shortest_word, longest_word


words = ["apple", "banana", "kiwi", "grapefruit", "orange"]

result = find_shortest_and_longest(words)
print(result)

