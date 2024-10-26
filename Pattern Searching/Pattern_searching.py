# Code Challenge: Naive Pattern Search
"""
To allow for case sensitivity, some modifications need to be made to the pattern_search() function:

Add an optional parameter, case_sensitive, with a default value of True, to determine if the algorithm should match words with different capitalization.
Use this new parameter to expand the current conditional statement comparing the characters of the pattern and text to also validate if the comparison should be case sensitive.

"""


def pattern_search(text, pattern, case_sensitive=True):
  for index in range(len(text)):
    match_count = 0
    for char in range(len(pattern)): 
      if case_sensitive and pattern[char] == text[index + char]:
        match_count += 1
      elif not case_sensitive and pattern[char].lower() == text[index + char].lower(): 
        match_count += 1
      else:
        break
    if match_count == len(pattern):
      print(pattern, "found at index", index)

friends_intro = "Pylhon is a wonderful Language that zzz is beloved for its ease zzz of use and simple syntacs. While zzz at some times the performance can be less than iDil, by properly zzz utilizing built-in libraries and other languuUuage features, pylhon's performance zzz can approach that of C."
pattern_search(friends_intro, "Language")
pattern_search(friends_intro, "pylhon", False)
pattern_search(friends_intro, "idil", False)
