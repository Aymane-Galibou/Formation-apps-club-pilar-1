class EvenNumbers:
    """An object that behaves like an immutable list of even numbers."""
    
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index < 0:
            raise IndexError("Negative indexing not supported")
        
        # Calculate the result dynamically:
        return index * 2

# Usage:
even_nums = EvenNumbers()

print(even_nums[5])      # Output: 10 (calculated on demand)
print(even_nums[1000])   # Output: 2000 (0 memory used to store 1001 numbers)

# It can even be iterated (though with extreme caution as it is infinite without __len__ or stop condition):
# for n in even_nums:
#     print(n)