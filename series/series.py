
# /////////////fibonacci////////////
def fibonacci(n):
    '''
    This function to calculate the fibonacci of number.
    :param n: int
    :return n: int
    '''
    
    if type(n) != int:
       return "please inter a number"
    if n == 1 or n == 0:
     return n
    else:
        prevNum1=0
        prevNum2=1

        for n in range(2, n+1):
           sum=prevNum1+prevNum2
           prevNum1=prevNum2
           prevNum2=sum
           
        return sum
    # else:
    #    return fibonacci(n-1) + fibonacci(n-2)
                 
         
# ////////////////lucas///////////
def lucas(n):
    '''
    This function to calculate the lucas of number.
    :param n: int
    :return n: int
    '''
    if type(n) != int:
       return "please inter a number"
    if n==0:
        return 2
    if  n == 1:
        return 1
    # else:
    #     prevNum1=2
    #     prevNum2=1

    #     for n in range(2, n+1):
    #        sum=prevNum1+prevNum2
    #        prevNum1=prevNum2
    #        prevNum2=sum
           
    #     return sum
    else:
       return lucas(n-1) + lucas(n-2)
    

# ////////////////sum_series///////////
def sum_series(n,x=0,y=1):
      '''
     This function to calculate the summation series of number.
    :param n ,x,y: int (x,y optional)
    :return n: int
    '''

    if type(n) != int:
          return "please inter a number"
    if x==0 and y==1:
        if n==0 or n==1:
          return n
        else:
           return fibonacci(n-1) + fibonacci(n-2)
    if x==0 and y==2:
        if n==0:
          return 2
        if n==1:
          return 1
        else:
           return lucas(n-1) + lucas(n-2) 
    else:
       prev1=x
       prev2=y
       for n in range(0,n-1):
          sum=prev1+prev2
          prev1=prev2
          prev2=sum
       return sum
    
 
       







def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def Lucas(n):
    if n == 1:
        return 1
    if n == 0:
        return 2
    else:
        return Lucas(n-1) + Lucas(n-2)



  


  



if __name__ == "__main__":
    print(Fibonacci(13))
    print(Lucas(13))