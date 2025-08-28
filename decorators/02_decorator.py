#Creating a decorator which prints value of its arguments every time the function called.


def decor(func):
    def wrapper(*args, **kwargs):
        arg_values = ", ".join(str(arg) for arg in args)
        kwargs_values = ", ".join(f"{k} = {v}" for k, v in kwargs.items())
        print(f"calling {func.__name__} with args {arg_values} and kwargs{kwargs_values}")
        
        return func(*args, **kwargs)
    
    return wrapper

@decor
def hello():
    print("Hello")

@decor
def great(name, message="hello"):
    greating = f"{message}, {name}"
    print(f"{message}, {name}")
    return greating

@decor
def sum(*args, **kwargs):
    print(f"{args} and {kwargs}")

hello()

great("Developer")

sum(1,2, "Hello, Dear", great("Sid"))