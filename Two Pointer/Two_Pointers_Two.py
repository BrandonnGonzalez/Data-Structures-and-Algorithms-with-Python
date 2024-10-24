# SET 1
# QUESTION 1

"""
Problem 1: Long Pressed
Write a function is_long_pressed() that takes in a string name and a string typed as parameters. Imagine your friend is typing their name into a keyboard and when typing a character, the key might get long pressed and the character will be typed 1 or more times.

The function should examine the typed characters and return True if it is possible that it was your friends name with some characters being long pressed and False otherwise.

Use the two-pointer approach to solve the problem, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. A common variation of this technique is to point one variable at the beginning of one string and a second pointer at the beginning of a second string, then increment each pointer conditionally to solve a problem.

def is_long_pressed(name, typed):
    pass

"""



"""
1) Start with two pointers, i and j, at the beginning of `name` and `typed` respectively.
2) Loop through both strings while both pointers are within the bounds of their respective strings.
  a) If characters at both pointers match, move both pointers.
  b) If they don't match but current `typed` character is the same as the previous one, move `typed` pointer.
  c) Otherwise, return False because of a mismatch.
3) After the loop, ensure all characters in `name` are accounted for.
4) Also ensure any extra characters in `typed` match the last character in `name`.
5) If both conditions are satisfied, return True, otherwise False.

"""

def is_long_pressed(name, typed):
    i = 0 # will iterate through the name string
    j = 0 # will iterate through the typed string 

    while i < len(name) and j < len(typed): # while i < len(name) and j < len(typed) (as long as there are characters to iterate through):
        if name[i] == typed[j]: # if the current character in name is equal to the current character in typed:
            i += 1 # increment the name pointer to the next character
            j += 1 # increment the typed pointer to the next character
        elif j > 0 and typed[j] == typed[j-1]: # else if j > 0 and current char in typed is equal to the previous character, that means it is
            # - a long pressed character and we can continue checking through the rest of the characters, increment by one 
            j += 1
        else: # else, return False because the program detects a mismatch, meaning typed doesnt match name.
            return False
    if i < len(name): # checks to see if there are still any characters to go through in the name string. if i < len(name), that means
        # it means not all characters from name were matched with typed.
        return False
    while j < len(typed): # while j < len(typed) (so as long as there are still characters to check through),
        if typed[j] != name[-1]: # if current char in typed is not matched with the last char in name, return False 
            return False
        j += 1 # otherwise, it checks for remaining characters
    return True # returns True once all conditions are met

    # Time Complexity: O(max(len(name), len(typed))), because: 
    """
    Main while loop:

    This loop runs while both i < len(name) and j < len(typed) hold true. In the worst case, it iterates through both strings fully.
    In each iteration of the loop, either i or j (or both) are incremented.
    The loop effectively runs O(max(len(name), len(typed))) times because the loop terminates as soon as one of the pointers reaches the end of its respective string.
    Second while loop:

    This loop runs if there are remaining characters in typed after the first loop. It checks if the remaining characters in typed are the same as the last character of name.
    In the worst case, this loop iterates through the remaining characters in typed, so it runs O(len(typed) - j), which is at most O(len(typed)).
    """

    # Space Complexity: O(1), because no extra arrays, lists, or complex data structures are used, nothing scales with the input.



# Example usage
name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))
# True

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))
# False
name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))
# True

