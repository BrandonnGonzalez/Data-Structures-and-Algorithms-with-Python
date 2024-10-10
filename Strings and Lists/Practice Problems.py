# QUESTION 1
"""
Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.

def swap_ends(my_str):
    pass
Example Usage:

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
Example Output: toab
"""


def swap_ends(my_str):
    return my_str[-1:] + my_str[1:-1] + my_str[:1]
    
    """
  1) Slice the last character from the input string
2) Slice the middle (excluding the first and last) characters from the input string
3) Slice the first character from the input string
4) Return these three components added together in the order: last, middle, first
"""


my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)


# QUESTION 2
"""
Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.

def is_pangram(my_str):
    pass
Example Usage:

my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))
Example Output:

True
False
"""

# PLANNING
"""
1. set a string equal to all of the letters in the alphabet
2. for all of the letters in the alphabet:
3. if those letters are also in the my_str:
4. return True
5. else, return False

T(C): O(n), where n is the length of the input string, and because we are iterating through both the alphabet and input string.
S(C): O(1), because no additional space is needed that grows with the input size n
"""

def is_pangram(my_str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for chars in alphabet:
        if chars in my_str:
            return True
        else:
            return False
    
my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))
# output: True



# QUESTION 3:

"""
Problem 4: Reverse String
Write a function reverse_string() that takes a string my_str as a parameter and returns the string reversed.

def reverse_string(my_str):
    pass
Example Usage:

my_str = "live"
print(reverse_string(my_str))
Example Output: evil
"""

# PLANNING
"""
1. return and slice the my_str by starting and ending it from the end of the string, ::-1
T(c): o(n), because copying a string of length n takes O(n) time because each character is visited once during the copying process.
S(c): o(n), because when using slicing ([::-1]), a new string is created to hold the reversed version.The new string requires O(n) additional space, as it stores the same number of characters as the original string
"""
def reverse_string(my_str):
    return my_str[::-1]

my_str = "live"
print(reverse_string(my_str))
# Output: "evil"




# QUESTION 4:

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

# PLANNING
"""
1) First, create a dictionary to track character occurrences
2) Loop through each character of the input string
  a) Add the character to the dictionary with one occurrence if it's new
  b) Add one to the occurrence of the character in the dictionary
3) Loop through each character of the input string again, but also track the current index (which is what enumerate does)
  a) If that character occurs once, return the current index
4) If no character with value 1 is found in the dictionary, return -1
"""

def first_unique_char(my_str):
    char_count = {}
    for nums in my_str:
        if nums in char_count:
            char_count[nums] += 1
        else:
            char_count[nums] = 1
    
    for index, nums in enumerate(my_str):
        if char_count[nums] == 1:
            return index

    return -1
# Time complexity: o(n), where n is the length of the input string. The worst case T(c) is o(n) because we are iterating through the input string to find potential unique values

# Space complexity: o(n). In the worst case, if all characters in my_str are unique, the dictionary will have n entries. The dominant space usage comes from the dictionary
  
 # Example input/output:
my_str = "leetcode"
print(first_unique_char(my_str))
# output: 0th index

str2 = "loveleetcode"
print(first_unique_char(str2))
# output: 2nd index

str3 = "aabb"
print(first_unique_char(str3))
# -1 (no unique values)



# QUESTION 6

"""
Write a function min_distance() that takes in a list of strings words and two strings word1 and word2' as parameters. The function should return the minimum distance between word1 and word2 in the list of words. The distance between one word and an adjacent word in the list is 1.

"""
# PLANNING:
"""
1) Set an initial minimum distance to be the worst case (word1 and word2 are first and last in the list of words)
2) Loop through the list of words
  a) If the word is word1, record a start index
    i) If the end index has already been found, update the minimum distance (if smaller)
  b) Otherwise if the word is word2, record a stop index
    i) If the start index has already been foudn, update the minimum distance (if smaller)
3) If the minimum distance was at some point updated, return it
4) Otherwise, return -1
"""

def min_distance(words, word1, word2):
    index1, index2 = -1, -1
    min_dist = len(words)  # Use the length of the list as the maximum possible distance
    for i, word in enumerate(words):
        if word == word1:
            index1 = i
            if index2 != -1:
                min_dist = min(min_dist, index1 - index2)
        elif word == word2:
            index2 = i
            if index1 != -1:
                min_dist = min(min_dist, index2 - index1)
    return min_dist if min_dist != len(words) else -1

# Time complexity: o(n), where n is the number of elements in the words list.
# Space complexity: o(1), because the function uses only a few additional variables: index1, index2, and min_dist, and these variables are of constant space and do not depend on the size of the input list. No additional data structures that scale with the input size are used.
    
#Example Usage:

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)
#Example Output:
# 3
# 1
# 2
