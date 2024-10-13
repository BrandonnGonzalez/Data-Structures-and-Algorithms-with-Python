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



# SET 2
# QUESTION 1


"""
Write a function remove_char() that takes in a string s and an integer n as parameters, The function returns a new string with the nth character removed where 0 < n < len(s).

def remove_char(s, n):
    pass
Example Usage:

s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)
Example Output: typo
"""

# PLANNING
"""
Will slice the input string into two components and then combine them at the end.
1) Slice the string from the beginning up to the index n
2) Slice the string from the index after n to the end
3) Return these two components added together in the order: first, last

"""

def remove_char(s, n):
    # Create a new string 'first_part' that includes all characters from the beginning of 's' up to the character at index 'n' (not inclusive).
    first_part = s[:n]
    # Create a new string 'last_part' that includes all characters from the character at index 'n+1' to the end of 's'.
    last_part = s[n+1:]
    # Return the result by concatenating 'first_part' and 'last_part', effectively removing the character at index 'n'.
    return first_part + last_part
    
    
    # Time Complexity: O(n), where n is the length of the input string "s". slicing creates a new string that copies up to n characters.
    # Space Complexity: O(n), where n is the length of the input string s.
    # - Two new strings first_part and last_part are created, each of size less than or equal to the length of s, so the additional space required is proportional to the length of s.

# Example usage:
s = "typpo"
fixed_s = remove_char(s, 2)
print(fixed_s)
# prints "typo"




# QUESTION 3
"""
Write a function vowel_count() that takes in a string s as a parameter and returns the number of vowels in the given string.

def vowel_count(s):
    pass
Example Usage:
my_str = "hello world"
my_str2 = "aAaAaAaAAA"
my_str3 = "ths strng s mssng vwls"

count1 = vowel_count(my_str)
print(count1)
count2 = vowel_count(my_str2)
print(count2)
Example Output:
3
10
0
"""

"""
PLANNING:
1. Need to create a list a string that contains all vowels.
2. Should definitely make the string a lowercase string so it does not miscount uppercased/lowercase vowels for example.
3. for all of the letters in the string, if those letters are also in the vowels string, increment a counter
4. return the counter for the given string input 
"""

def vowel_count(s):
    vowels = "aAeEiIoOuU"
    vowel_counter = 0
    for letters in s:
        if letters in vowels:
            vowel_counter += 1
            
    return vowel_counter

# Time Complexity: O(n), where n is the length of the input string s. Worst case runtime is o(n) because we are using a for loop to iterate through the entire "s" string to look for vowels.
# Space Complexity: O(1), because we are not using any additional data structures and our space does not neccesarily grow with our input string, "s".
# Completion: 6 minutes

# Example Usage:
my_str = "hello world"
count1 = vowel_count(my_str)
print(count1) # output: 3

my_str2 = "aAaAaAaAAA"
count2 = vowel_count(my_str2)
print(count2) # outputs 10



# QUESTION 4

"""
Write a function reverse_sentence() that takes in a string sentence as a parameter and returns the string with the sentence but with the order of the words reversed. The sentence will only contain alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function returns the original string.

def reverse_sentence(sentence):
    pass
Example Input: sentence = "I solemnly swear I am up to no good"
Example Output: "good no to up am I swear solemnly I"
"""
"""
PLANNING:
Reverse a list of the input words and return the joined sentence
1) First, split the sentence into a list of words
2) Slice the entire list with a negated step parameter
3) Join the list of words back into a sentence
4) Return the reversed sentence
"""
def reverse_sentence(sentence):
    words = sentence.split(' ') # splits the string into a list of words
    reversed_words = words[::-1] # slices the words string with a negated step parameter
    reversed_sentence = ' '.join(reversed_words) # joins back the sliced list of words, reversed but into a full sentence
    return reversed_sentence # returns that string
    
# Time Complexity: O(n), where n is the length of the input string, "sentence". This is due to:
# Splitting the Sentence: The sentence.split(' ') operation goes through the entire string to separate it into words, which takes O(n) time, where n is the length of the sentence.
# Reversing the List: The slicing operation words[::-1] also takes O(m) time, where m is the number of words in the list.
# Joining the Words: The ' '.join(reversed_words) operation goes through the list of reversed words and combines them back into a single string, which takes O(n) time again.

# Space Complexity: O(n)
# 1. List of Words: The split method creates a new list of words, which takes O(m) space, where m is the number of words.
# 2. Reversed List: The slicing operation also creates a new list of the same size, requiring O(m) space.
# 3. Joined String: The final string created by ' '.join(reversed_words) will also take O(n) space since it combines all characters into a single string.

# Completion: 20 minutes (looked at solution)



# SESSION 2
# SET 1
# QUESTION 1

"""
Write a function sum_of_number_strings() that takes in a list of strings nums. Each string is a representations of integers. The function should return the sum of these strings as an integer.

# PLANNING
1. need a var that will hold  the int value of the sum
2. for all of the numbers in the string...
3. convert those numbers into an int and add them to the var we made
4. return that var
"""

def sum_of_number_strings(nums):
    sum_holder = 0
    for numbers in nums:
        sum_holder += int(numbers)
    return sum_holder

# Time Complexity: O(n), where n is the total number of characters in the input string nums. This is due to the for loop iterating through the entire input string and adding it into
# the counter variable that sums up all of the numbers.
# Space Complexity: O(1), because we do not require any extra space; no additional dsa needed and we only use one variable.
# Completion: 5 minutes

nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
# Example Output: 60




# QUESTION 2

"""
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. 
The function returns the modified list.

def remove_duplicates(nums):
    pass
Example Input: nums = [1,1,1,2,3,4,4,5,6,6]
Example Output: no_dups = [1,2,3,4,5,6]
"""

# PLANNING
"""
1.  create a new list that will contain the non-duplicate values
2. For all of the numbers in the nums list...
3. if those numbers are NOT in the non-duplicates list... add them
4. Add the end of the for loop return the new, non-duplicates list
"""

def remove_duplicates(nums):
    non_duplicates = []
    for numbers in nums:
        if numbers not in non_duplicates:
            non_duplicates.append(numbers)
    return non_duplicates

# Time Complexity: O(n^2), where n is the size of the input nums list. This is also due to the for loop having to iterate through the entire nums list, as well
# as the in operator checking if the numbers are not in the non_duplicates list, running in o(n)  time, making the worst case runtime, O(n^2).
# Worst case, it has to add multiple duplicate numbers into the non_duplicates list.
# Space Complexity: O(n), due to the program returning a new list which contains the non_duplicates.
# Completion: 5 minutes
# A better solution would be using a Set which is faster for membership checks, o(1).

# Example input
nums = [2, 2, 3, 4, 4, 4, 5, 5, 6, 7]
print(remove_duplicates(nums))
# Example output: non_duplicates = [2, 3, 4, 5, 6, 7]



# QUESTION 3


"""
Write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the 
new string. Non-letter characters should remain in their original positions.

Example Usage:

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
Example Output: j-Ih-gfE-dCba
"""

# PLANNING
"""
Make a list of all letters in the string, then build a new string that reverses only the letters.
1) Create an empty list for the letters
2) Loop through the string, and add any letters to the list
3) Make an index variable, set to end of letters list
4) Create an empty results string
5) Loop through each character in the original string
  a) If the char was a letter:
     i) add the value at letters[index] to results
    ii) reduce index by 1
  b) Otherwise, add the char itself to results
6) Return results

"""

def reverse_only_letters(s):
    letters = []
    for c in s:
        if c.isalpha():
            letters.append(c)
    
    letters_index = len(letters) - 1 # Start from the end of the letters list
    results = " "

    for c in s:
        if c.isalpha():# if the character is alpahabetic 
            results += letters[letters_index] # adds the current letter in the letters list, to the results string
            letters_index -= 1 # decrements the current letters_index to continue reversing through the list
        else: # if not other character is alphabetic and could be like a dash or number, add that to the results string.
            results += c
    return results

# Time Complexity: O(n), where n is the length of the string. The for loop iterates for all of the characters in the string, which is o(n) time. The second 
# loop also does the same which is o(n) time.
# Space Complexity: O(n), due to using a list to store all of the letters in the string, which in the worst case can hold all n characters 
# (if all characters are letters).  Additionally, am building the result string, which will also require o(n) time.
# Completion: 15 minutes 

#Example Usage:
s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
#Example Output: j-Ih-gfE-dCba




# QUESTION 4

"""
Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. 
A uniform substring consists of a single repeated character.

"""

# PLANNING
"""
1) If the input string is empty, return 0
2) Set a variable to track the largest uniform substring and the current uniform substring
3) Loop through the length of the input string
  a) If the current and previous characters are equal, increase the current uniform substring counter and update the largest uniform 
     substring counter
  b) Otherwise, reset the current uniform substring counter to 1
4) Return the largest uniform substring counter
"""

def longest_uniform_substring(s):
    if not s:
        return 0 
    max_substring = 1
    current_substring = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]: # O(1) time operation. The current letter gets compared to the previous letter in the iteration 
            current_substring += 1
            max_substring = max(max_substring, current_substring) # constant time operation O(1)
        else:
            current_substring = 1
    return max_substring

    """
    Time Complexity: O(n), where n is the length of the input string "s". This is due to the for loop we are using to iterate through the entire string,
    which compares the current letter to it's previous letter.

    Space Complexity: O(1), due to a fixed amount of space being used and due to their not being any additional data structures that grow with the size of the 
    input, or hold values or run through the code.
    max_substring and current_substring only hold integers so there is no additional space required.
    Completion: 15 minutes
    """

# Example input
s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)
# Example output
# 4 
# 1


