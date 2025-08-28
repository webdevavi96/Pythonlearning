#Creating a decorator...

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} rans in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
    
example_function(2)