a = 10
b = 0

try:
    result = a / b
    print(result)
except ZeroDivisionError as e:
    print("Error:", e)

print("\n------------------------------------------------------------------------------------------------------------------------")

my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError as e:
    print("Error:", e)

print("\n------------------------------------------------------------------------------------------------------------------------")

def safe_divide(a, b):
    try:
        result = a / b
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid data type for division")
    finally:
        print("Execution completed")


safe_divide(1, 0)
safe_divide(1, "a")

