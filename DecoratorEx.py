
def greet(name):
    return "Hello {}".format(name)

print(greet("Alice"))

def greet2(name):
    def greet_message():
        return "Hello"
    return "{} {}".format(greet_message(),name)

print(greet2("Alice"))


def change_name_greet(func):
    name = "Alice"
    return func(name)

print(change_name_greet(greet))

def upper(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

print(upper(greet)("Alice"))
