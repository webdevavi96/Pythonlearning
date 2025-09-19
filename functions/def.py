def myFun():
    print("Hello User!")


myFun()

# Find the square of 4 using lambda function.

square = lambda x: x**2
print(square(2))


# Recursion Function.


def Factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * Factorial(n - 1)


print(Factorial(5))
