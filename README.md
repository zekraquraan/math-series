
## LAB - Class 02
## Project: MATH-SERIES
## Author: Zekra Quraan
## Links and Resources
# back-end server url (when applicable)
# front-end application (when applicable)

## Setup
# .env requirements (where applicable)
# i.e.

# PORT - Port Number
# DATABASE_URL - URL to the running Postgres instance/db
# How to initialize/run your application (where applicable)
# python series.py



**Tests**
using pytest to write and run tests for code
using **TDD** process:

- **pip install pytest**
- **import pytest**
- create a file  "__init__.py"
- creating first test function for the fibonacci series :
    
    ```
    def test_fibonacci_one():
    actual=fibonacci(1)
    excepted=1
    assert actual == excepted

    ```
testing by run **pytest**
- create a folder (series) and make it as a module by "__init__.py"
- import a function from the module series folder in the test_series.py

    ```
    from series.series import fibonacci
    ```
- creating fibonacci series function :
     
    ```
    def fibonacci(n):
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
    ```
- refactoring a function.
      
    ```
    if type(n) != int:
       return "please inter a number"
    ```
