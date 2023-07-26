class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self, name):
        return f'{self.greeting}, {name}!'


greeter = Greeter('Hello')
print(greeter.greet('Alice'))  # Hello, Alice!


def greeter_f(name, greeting):
    return f'{greeting}, {name}!'


print(greeter_f("Alice", "Hello from greater_f"))  # Hello from greater_, Alice!
