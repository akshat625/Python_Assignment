class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Akshat", 25)
print("Name:", person.name)
print("Age:", person.age)

print("\n------------------------------------------------------------------------------------------------------------------------")

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def check_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("12345", "Alice", 1000)
account.deposit(500)
account.withdraw(300)
account.check_balance()

print("\n------------------------------------------------------------------------------------------------------------------------")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(", ")
        return cls(title, author)


book = Book.from_string("Python Programming, John Doe")
print("Title:", book.title)
print("Author:", book.author)

print("\n------------------------------------------------------------------------------------------------------------------------")

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

print("\n------------------------------------------------------------------------------------------------------------------------")

class Father:
    def father_method(self):
        print("This is father method")


class Mother:
    def mother_method(self):
        print("This is mother method")


class Child(Father, Mother):
    def child_method(self):
        print("This is child method")


child = Child()
child.father_method()
child.mother_method()
child.child_method()

print("\n------------------------------------------------------------------------------------------------------------------------")
