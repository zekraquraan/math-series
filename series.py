def fibonacci_recursion(n):
    """Return the nth value in the Fibonacci series using recursion."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


def lucas_recursion(n):
    """Return the nth value in the Lucas series using recursion."""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas_recursion(n-1) + lucas_recursion(n-2)

def sum_series(n, first=0, second=1):
    """Return the nth value in a series with the given recurrence relation
    and starting values.

    If first and second are not specified, the default values are 0 and 1,
    respectively, producing the Fibonacci series.

    If first is 2 and second is 1, the resulting series will be the Lucas
    series.

    If first and second are other values, the resulting series will have a
    recurrence relation of summing the previous two values.

    """
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)
