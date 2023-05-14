def sum_series(n, first_num=0, second_num=1):
    """
    Returns the nth value in a series starting with first_num and second_num.
    
    Parameters:
    - n (int): The index of the value to return.
    - first_num (int): The first value in the series (default is 0).
    - second_num (int): The second value in the series (default is 1).
    
    Returns:
    int: The nth value in the series.
    """
    if n <= 0:
        return first_num
    if n == 1:
        return second_num

    return sum_series(n-1, first_num, second_num) + sum_series(n-2, first_num, second_num)


def lucas(n):
    """
    Returns the nth value in the Lucas series.
    
    The Lucas series is similar to the Fibonacci series but starts with 2 and 1 instead of 0 and 1.
    
    Parameters:
    - n (int): The index of the value to return.
    
    Returns:
    int: The nth value in the Lucas series.
    """
    return sum_series(n, 2, 1)


def fibonacci(n):
    """
    Returns the nth value in the Fibonacci series.
    
    The Fibonacci series starts with 0 and 1, and each subsequent value is the sum of the two preceding ones.
    
    Parameters:
    - n (int): The index of the value to return.
    
    Returns:
    int: The nth value in the Fibonacci series.
    """
    return sum_series(n)
