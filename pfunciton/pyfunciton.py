
# Remember - Python reads your code from top to bottom. It's not going to look ahead in order to find a function you forgot to put in the right place 

import math


def message() :
    print("Enter a value...")

print("We started here...")
message()
print("We ended here....")

# Guess what has been done here ? Fucntion named has been assinged a value as a varablie.
message = 1
print(message)

# -- Call the function again.. it will through an error.
# message() # It will throw error since its no logner a function. 

# Parameterized function
def shownumber(number) :
    print("The number is:", number)

shownumber(100)
shownumber(200)
shownumber(300)
shownumber(400)


def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))



def is_prime(num):
    # If given number is greater than 1
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between, # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

print(is_prime(11))


def is_prime(num):
    
    prime_flag = False
    # A natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.
    if num > 1:
        if num == 2: return True
        #for i in range(2, int(num/2) + 1):
        for i in range(2, num):
            if num % i == 0:
                #print(f"The number {num} isn't prime! ")
                prime_flag = False
            else:
                prime_flag = True
                #print(f"The number {num} is prime! ")
                
    return prime_flag
    
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()


# The compact function idea
# We know from school that the sum of two arbitrary sides has to be longer than the third side.
def is_it_a_perfect_triangle1(a, b, c):
     if a + b <= c: 
          return False
     if b + c <= a: 
          return False
     if c + a <= b: 
          return False
     return True

print(is_it_a_perfect_triangle1(1, 1, 1))
print(is_it_a_perfect_triangle1(2, 2, 2))
print(is_it_a_perfect_triangle1(1, 1, 3))

# a bit compact version
def is_it_a_perfect_triangle2(a, b, c):
     #print(f"The bit compact version of above {a}, {b} {c}")
     if a + b <= c or b + c <= a or c + a <= b: 
          return False
     return True

print(is_it_a_perfect_triangle2(1, 1, 1))
print(is_it_a_perfect_triangle2(2, 2, 2))
print(is_it_a_perfect_triangle2(1, 1, 3))

# One more compact version of this is
def is_it_a_perfect_triangle3(a, b, c):
        #print(f"The bit compact version of above {a}, {b} {c}")
        return a + b > c and b + c > a and c + a > b  

print(is_it_a_perfect_triangle3(1, 1, 1))
print(is_it_a_perfect_triangle3(2, 2, 2))
print(is_it_a_perfect_triangle3(1, 1, 3))



def is_a_right_triangle(a, b, c):
    if not is_it_a_perfect_triangle3(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


def heron(a, b, c):
     p = (a + b + c) / 2
     return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def area_of_a_triangle(a, b, c):
     if not is_it_a_perfect_triangle3(a, b, c):
          return None
     return heron(a, b, c)
          

#a = float(input("Please enter the first side\'s length: "))
#b = float(input("Please enter the second side\'s length: "))
#c = float(input("Please enter the third side\'s length: "))

print(is_a_right_triangle(2, 3, 4)) 
#print(f"The area of a triangel is {area_of_a_triangle(a, b, c)}")
print(area_of_a_triangle(1., 1., 2. ** .5))


'''

def factorial_fn(n):
     if n < 0:
          return None
     if n < 2:
          return 1
     product = 1

     for i in range(2, n+1):
          product *= i
     return product

for n in range(1, 6):  # testing
    print(n, factorial_fn(n))
'''
