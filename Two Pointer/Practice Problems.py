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




# QUESTION 2



"""
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. 
The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables 
(also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to 
point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one 
variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the 
pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite 
ends of the list.

def reverse_list(lst):
    pass
Example Input: [1, 2, 3, 4, 5]
Example Output: [5, 4, 3, 2, 1]

"""

# PLANNING
"""
1) Initialize two pointers: one at the beginning (`left`) and one at the end (`right`).
2) While `left` is less than `right`:
  a) Swap the elements at `left` and `right`.
  b) Move `left` pointer one step right (increase by 1).
  c) Move `right` pointer one step left (decrease by 1).
3) Return the list as the elements are now reversed in place.

"""
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    
    while left < right:
        # Swaps elements using a temporary variable
        temp = lst[left]
        lst[left] = lst[right]
        lst[right] = temp
        
        # Move the pointers towards the center
        left += 1
        right -= 1
    
    return lst
    
    """
    Time Complexity: O(n), where n is the length of the list. Because the number of operations grows proportionally with the size of the input list.
    Space Complexity: O(1), because there are no additional data structures or memory that scales with the size of the input list. The only extra space used is for the variables left, right, and temp, which remain constant regardless of the size of the input list.
    """

# Example input
lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))
# Output:
# [5,4, 3, 2, 1]





# SET 2
# QUESTION 2

"""
Write a function is_palindrome() that takes in a string s as a parameter and returns True if the string is a palindrome and False otherwise. You may assume the string contains only lowercase alphabetic characters.

The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

def is_palindrome(s):
    pass
Example Usage:

s = "amanaplanacanalpanama"
s2 = "helloworld"

print(is_palindrome(s))
print(is_palindrome(s2))
Example Output:

True
False
"""

# UNDERSTANDING
"""
What if the string is empty?
- An empty string is considered a palindrome as it reads the same forward and backward.
"""

# PLANNING
"""
1) Initialize two pointers, left at the start (0) and right at the end (length of s - 1)
2) While left pointer is less than right pointer:
  a) If characters at left and right pointers do not match, return False
  b) Increment left pointer and decrement right pointer
3) If all characters match, return True
"""

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
    
    """
    Time Complexity: O(n), where n is the length of the string. This is due to the pointers going through the entire input string until they equal  to each other or cross paths. The number of operations grows linearly with the size of the input string.
    
    Space Complexity: O(1), because no extra space is needed or any data structures that grow in size because of the input. The variables, left and right, are constant.
    """
    
s = "amanaplanacanalpanama"
s2 = "helloworld"
 
print(is_palindrome(s)) # True
print(is_palindrome(s2)) # False





# SET 3
# QUESTION 2


"""
Write a function two_sum() that takes in a sorted list of integers nums and an integer target as parameters and returns the indices of the two numbers that add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the indices in any order.

The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.

def two_sum(nums, target):
    pass
Example Usage:

nums = [2,7,11,15,7]
sol1 = two_sum(nums, 9)
print(sol1)
sol2 = two_sum(nums, 18)
print(sol2)
Example Output

[0,1]
[1,2]
"""

# Understanding
""" 
1. What do we do if there are multiple pairs that could work but we only need one?
Since the problem guarantees exactly one solution, this situation will not occur.
What if the list has negative numbers?
2. The approach still works as the list is sorted, allowing the two-pointer technique to be effective regardless of the sign of the numbers.
"""

# PLANNING
"""
1) Initialize two pointers: `left` at the start of the list and `right` at the end.
2) While the `left` pointer is less than the `right` pointer:
  a) Calculate the `current_sum` of the numbers at the two pointers.
  b) If `current_sum` equals `target`, return the indices `[left, right]`.
  c) If `current_sum` is less than `target`, increment the `left` pointer to try a larger sum.
  d) If `current_sum` is greater than `target`, decrement the `right` pointer to try a smaller sum.
3) Since the problem guarantees a solution, the loop will always return before it terminates.
"""

# Implementation
def two_sum(nums, target):
    left = 0 
    right = len(nums) - 1
    
    while left < right: # while the left pointer is less than the right... (havent met yet)
        current_sum = nums[left] + nums[right] #keeps track of what the pointers add up to
        if current_sum == target: #if the  two pointers are equal to the target:
            return [left, right] # returns the indices of the left and right pointer
        elif current_sum < target: # else-if the pointers add up less than the target:
            left += 1  # Need a larger sum
        else:
            right -= 1  # Need a smaller sum
        
    """
    Time Complexity: O(n), where n is the length of nums. The number of operations grow with the input list "nums". The while loop is also an operator that iterates the pointers through the entire list, taking linear time.
    
    Space Complexity: O(1), because there are no additional data structures that grow with the input list "nums". The variables that are initialized are all constant.
    """
    #


nums = [2,7,11,15,7]
sol1 = two_sum(nums, 9)
print(sol1) # prints [0, 4]
sol2 = two_sum(nums, 18)
print(sol2) # prints [2, 4]
