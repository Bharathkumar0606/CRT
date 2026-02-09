'''
debug- errors
debugging - finding and fixing of errors

Types of errors:
1)Syntax Error - Mising of colon,missing of indentation
2)Runtime Errors - division by zero
3)Logical Errors - missing of logics

Debugging Techniques
1)print()
2)try-except
3)Using pdb - python debugger

purpose:
1)pause the execution code
2)inspect the variable's value
3)To run the code line by line

pdb commands:
1)n-To execute the output in a next line
2)p variable- to get the value of a variable
3)l-list nearby code
4)c-continue the execution
5)s-to start a function
6)r-return from the function
7)h-help
8)q-quite the execution



try:
    a = int(input("Enter a mumber: "))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by zero")
except ValueError:
    print("Invalid input")
'''
import pdb
def add(a,b):
    pdb.set_trace()
    return a+b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(add(a,b))
