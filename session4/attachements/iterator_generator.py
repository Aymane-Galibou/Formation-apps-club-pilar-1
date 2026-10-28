class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

# Usage
my_counter = Counter(1, 3)
print(next(my_counter))  # 1
print(next(my_counter))  # 2

# **************************************** using generators ****************************************
def counter_gen(low, high):
    while low <= high:
        yield low
        low += 1

# Usage — Function call returns an Iterator!
my_gen = counter_gen(1, 3)

print(hasattr(my_gen, "__next__"))  # True (It's an iterator!)
print(next(my_gen))  # 1
print(next(my_gen))  # 2

# Works seamlessly in a for loop
for num in counter_gen(1, 3):
    print(num)  # 1, 2, 3



"""
stop = 4
def inner_st():
    for i in range(1,stop+1):
        yield i

def inner_nd():
    for i in range(stop+1,stop*2 + 1):
        yield i
 
def outer():
    yield from inner_st()
    yield from inner_nd()
    yield stop*2 + 1

print(list(outer()))   # [1, 2, 3 ,4 ,5 ,6 ,7 ,8 ,9 ]
"""