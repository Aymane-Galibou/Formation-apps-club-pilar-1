

def process_numbers(numbers, operation):
    """Higher-order function: takes a list and a function as arguments."""
    return [operation(n) for n in numbers]


# Define some simple functions to pass in
def double(x):
    return x * 2


def square(x):
    return x**2


# Usage
numbers = [1, 2, 3, 4]

print(process_numbers(numbers, double))  
print(process_numbers(numbers, square))  

print(process_numbers(numbers, lambda x: x + 10))  