def factorial(n):

    """This doc string is a test"""
    return 1 if n < 1 else n * factorial(n-1)

if __name__ == "__main__": 

    print(factorial(42))
    print(help(factorial))