# What you write:
numbers = [1, 2, 3]

for num in numbers:
    print(num)

# --------------------------------------------------
# What Python ACTUALLY executes behind the scenes:
# --------------------------------------------------

#  Get an iterator from the iterable
iterator_obj = iter(numbers)

#  Infinite loop to pull elements
while True:
    try:
        # Get the next item
        num = next(iterator_obj)
        print(num)
    except StopIteration:
        # Catch the exception and exit when items run out
        break