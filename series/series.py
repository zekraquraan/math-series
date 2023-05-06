
def sum_series(n, first_num = 0, second_num = 1):
    if n <= 0:
        return first_num
    if n == 1:
        return second_num
    
    return sum_series(n-1, first_num, second_num) + sum_series(n-2, first_num, second_num)


def lucas(n):
    return sum_series(n, 2, 1)


def fibonacci(n):
    return sum_series(n)
    
 
       










  


  

