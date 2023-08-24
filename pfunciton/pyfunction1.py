def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0

    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum

    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))


# Using the recursion
def factorial_function_recursion(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function_recursion(n - 1)

for n in range(1, 6):  # testing
    print(n, factorial_function_recursion(n))