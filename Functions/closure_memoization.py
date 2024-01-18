def memoize(function):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = function(*args)
            cache[args] = result
            return result
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(499))
'''
fibonacci(0) = 0
fibonacci(1) = 1
fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 + 0 = 1
fibonacci(3) = fibonacci(2) + fibonacci(1) = 1 + 1 = 2
fibonacci(4) = fibonacci(3) + fibonacci(2) = 2 + 1 = 3
...

In this example, we define a decorator function called **`memoize`** that takes a function as its argument and returns a closure that caches the results of the function calls in a dictionary.

We then apply the **`memoize`** decorator to the **`fibonacci`** function, which calculates the n-th Fibonacci number recursively. Thanks to the closure created by **`memoize`**, the results of the **`fibonacci`** function are cached in the **`cache`** dictionary, allowing the function to be computed more efficiently.

In summary, closures are a powerful and flexible feature of Python that allow functions to retain access to the variables of their enclosing scope even after that scope has completed execution. This makes them a useful tool for implementing caching, memoization, and other advanced programming techniques.
'''

