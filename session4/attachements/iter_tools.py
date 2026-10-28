from itertools import islice,chain ,groupby ,cycle ,count  ,combinations ,permutations  

# islice: take a slice of an infinite/lazy generator
first_ten = list(islice(count(10,2),10))         # [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

de_1_a_5 = list(islice(count(10,2),1,6))        # [12, 14, 16, 18, 20] (indice de fin n'est pas prit en consideration)

# chain: combine several iterables into one
combined = list(chain([1, 2], [3, 4]))            # [1, 2, 3, 4]
combined2 = list(chain('ABC', 'DEF'))            # [A B C D E F]

 
# groupby: group consecutive items sharing a key
data = [1, 1, 2, 2, 3]
groups = {k: list(v) for k, v in groupby(data)}   # {1: [1,1], 2: [2,2], 3: [3]}

text ='WELCOOOMEWWE'
compressed = [(k, len(list(v))) for k, v in groupby(text)]

# cycle : repeat the given sequence indefinitly
repeated_sequence = cycle('ABC') # A B C A B C 

repeated_sequence = cycle(['ABC']) # ABC ABC ABC ABC 

# combinations 
poke_types = ['Bug', 'Fire', 'Ghost', 'Grass', 'Water']
combinations_probs = combinations(poke_types, 2) # r-length tuples in sorted order with no repetead elements

permutations_probs = permutations(poke_types, 2) # r-length tuples with all possible ordering and no repetead elements


