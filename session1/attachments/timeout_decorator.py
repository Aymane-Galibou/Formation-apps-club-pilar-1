from functools import wraps
import signal
import time 

"it still contains a problem of nested calls of functions"
def timeout(n_seconds):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def raise_timeout(signum, frame):
                raise TimeoutError(
                    f"Function '{func.__name__}' timed out after {n_seconds}s"
                )
            # it return the previous handler 
            prev_handler = signal.signal(signal.SIGALRM, raise_timeout)

            signal.alarm(n_seconds)

            try:
                return func(*args, **kwargs)
            finally:

                signal.alarm(0)
                signal.signal(signal.SIGALRM, prev_handler)

        return wrapper

    return decorator


@timeout(5)
def display():
    time.sleep(4)
    print("welcome to this shit")

@timeout(3)
def display1():
    time.sleep(4)
    print("welcome to this shiit 1")

display()

display1()