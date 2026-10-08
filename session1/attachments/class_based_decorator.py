


"""
class Repeat:
    def __init__(self,n_times):
        self.calls=0
        self.n_times=n_times

    def __call__(self, func):
        def wrapper(*args,**kwargs):
            self.calls +=1
            print(f'Print the {self.calls} time for the {func.__name__}')
            for _ in range(self.n_times):
                func(*args,**kwargs)

        return wrapper

@Repeat(n_times=3)
def say_hi():
    print("Hi!")

say_hi()
"""


class Repeat:
    def __init__(self,func):
        self.calls=0
        self.func=func

    def __call__(self, *args,**kwargs):
        self.calls +=1
        print(f'Print the {self.calls} time for the {self.func.__name__}')
        self.func(*args,**kwargs)

@Repeat
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()

