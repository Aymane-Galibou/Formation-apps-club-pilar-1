

def make_multiplier(factor):
    def multiply(x):
        return x * factor 
    
    factor = 99 
    
    return multiply 

# 
double = make_multiplier(2)

# 
print(double(5))