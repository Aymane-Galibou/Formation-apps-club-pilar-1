

def memoize(func):
    cache ={}
    def wrapper(n,*args,**kwargs):
        if n not in cache:
            cache[n] = func(n,*args,**kwargs)
        else:
            print(f'This calculation of {n} already exist in the cache')
        return cache[n]
    return wrapper



@memoize
def fibonaci(n):
    if n <= 2:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

result1 = fibonaci(40)
print(result1)

result2 = fibonaci(20)
print(result2)

result3 = fibonaci(40)
print(result3)


