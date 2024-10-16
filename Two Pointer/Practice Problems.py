# SET 1
# QUESTION 1

"""
Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. 
A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.

def is_prime(n):
    pass
Example Usage:

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))
Example Output:

True
False
False
"""

"""
PLANNING:
1) If n is less than or equal to 1, return False (not a prime).
2) Use a loop to check divisibility from 2 up to the square root of n:
  a) If n is divisible by any number in this range, it's not a prime, return False.
  b) If no divisors are found, it's a prime, return True.
"""

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
