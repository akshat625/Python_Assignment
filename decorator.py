import time

def time_calculator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Start Time:", start_time)
        print("End Time:", end_time)
        print("Total Time Taken:", end_time - start_time)
    return wrapper


@time_calculator
def append_numbers():
    numbers = []
    for i in range(1, 1001):
        numbers.append(i)


append_numbers()

print("\n------------------------------------------------------------------------------------------------------------------------")

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed:", e)
        return wrapper
    return decorator


@retry(3)
def may_fail(name):
    print(f"Hello, {name}!")


may_fail("Akshat")

print("\n------------------------------------------------------------------------------------------------------------------------")

def validate_positive(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be positive")
        return func(x)
    return wrapper


@validate_positive
def square_root(x):
    return x ** 0.5


print(square_root(16))

print("\n------------------------------------------------------------------------------------------------------------------------")

def cache(func):
    cached_results = {}

    def wrapper(x):
        if x in cached_results:
            print("Returning cached result...")
            return cached_results[x]
        result = func(x)
        cached_results[x] = result
        return result

    return wrapper


@cache
def expensive_computation(x):
    print("Performing computation...")
    return x * x


print(expensive_computation(5))
print(expensive_computation(5))

print("\n------------------------------------------------------------------------------------------------------------------------")

def requires_permission(func):
    def wrapper(user, *args, **kwargs):
        if "admin" in user.get("permissions", []):
            return func(user, *args, **kwargs)
        else:
            print("Access denied")
    return wrapper


@requires_permission
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")


user1 = {'name': 'Alice', 'permissions': ['admin']}
user2 = {'name': 'John', 'permissions': ['dev']}
user3 = {'name': 'Kurt', 'permissions': ['test']}

delete_user(user1, 101)
delete_user(user2, 102)
delete_user(user3, 103)

