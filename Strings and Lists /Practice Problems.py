
# Problem 4
"""
Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    pass
Example Usage:

my_str = "live"
print(reverse_string(my_str))
Example Output: evil
"""

# SOLUTION
# def reverse_string(my_str):
#     return my_str[::-1]
    
# my_str = "live"
# print(reverse_string(my_str))



# PROBLEM 5
"""
Write a function first_unique_char() that given a string my_str as a parameter, it finds the first non-repeating character in it and returns its index. If it does not exist, then return -1.

def first_unique_char(my_str):
    pass
Example Usage:

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))
Example Output
0
2
-1

"""

# PSEUDOCODE
"""
1) First, create a dictionary to track character occurrences
2) Loop through each character of the input string
  a) Add the character to the dictionary with one occurrence if it's new
  b) Add one to the occurrence of the character in the dictionary
3) Loop through each character of the input string again, but also track the current index
  a) If that character occurs once, return the current index
4) If no character with value 1 is found in the dictionary, return -1

"""

# SOLUTION
def first_unique_char(my_str):
    # we need to find the first NON-duplicate number in the list and return the index
    unique = {}
    for chars in my_str:
        if chars in unique:
            unique[chars] += 1
        else:
            unique[chars] = 1
    
    for index, chars in enumerate(my_str):
        if unique[chars] == 1:
         return index
    return -1
            

my_str = "leetcode"
print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))
# Example Output
# 0
# 2
# -1           




