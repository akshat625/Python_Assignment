def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()

for _ in range(10):
    print(next(fib))

print("\n------------------------------------------------------------------------------------------------------------------------")

def infinite_multiples(n):
    multiple = n
    while True:
        yield multiple
        multiple += n


multiples = infinite_multiples(3)

for _ in range(5):
    print(next(multiples))

print("\n------------------------------------------------------------------------------------------------------------------------")

def repeat_word(word, times):
    for _ in range(times):
        yield word


for value in repeat_word("hello", 5):
    print(value)

