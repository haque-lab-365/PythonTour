import time
import math 


# https://www.w3schools.com/python/python_ref_exceptions.asp
# ArithmeticError	Raised when an error occurs in numeric calculations
# https://www.tutorialspoint.com/python-exception-base-classes
# https://www.tutorialspoint.com/python/python_cgi_programming.htm


#OverFlowError : An OverflowError exception is raised when an arithmetic operation exceeds the limits to be represented. This is part of the ArithmeticError Exception class.
#ZeroDivisionError
#FloatingPointError

try:
    arithmatic = 5/1
    print(f'The arithmatic error is: {arithmatic}')
except ArithmeticError:
    print("Aha... probably we have made an arithmatic error!!")


# curtime = [tm for tm in time.localtime()]

try:
    print("We are going to explore with the exponential value:")
    print(math.exp(1000))
except OverflowError as oe:
    print("After overlfow !! ", oe)
# print(1.2 - 1.0)

# overflow error comes again
j = 5.0
try:
    for i in range(1, 1000):
        j = j**i
        print(j)
except OverflowError as ex:
    print("Overflow error happened")
    print(f"{ex}, {ex.__class__}")

""" The below code is responisble for mitingating assertion error <Python | Assertion Error> """
try:
    x = 1
    y = 0
    assert y != 0, "Definitely invalid operation!!!" 
    print("This message isn't printed intentionally ?")

except AssertionError as msg:
    print(msg) 

""" Attribute errors in Python are generally raised when an invalid attribute reference is made. """
class Boss:

    def __init__(self):

        self.a = "Boss is coming"
        self.b = "Boss will leave at 4:00 PM"
    
    def SayHello(self):
        print(f'Hello boss you are late {time}')

# Driver code
obj_boss = Boss()
try:
    print(f'The whole things boiled down to...{obj_boss.a}')
    #raise an atrribute err | We have no c attribute in the Boss class
    print(obj_boss.c)
except AttributeError as ae:
    print("There is no such attribute " + str(ae) )


# EOFError is short for "End-of-Line Error." This error occurs when Python has reached the end of user input without receiving any input.
try:
     string = input() # Cntrl+Z
     print(string)
except EOFError:
     print("No data provided to input function!")

"""
try:
    n = int(input())
    print(n * 10)  
except EOFError as e:
    print(e)

"""