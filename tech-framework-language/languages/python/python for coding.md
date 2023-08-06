# Python for coding

## utils

### [len(s)](https://docs.python.org/3/library/functions.html#len)

Return the length (the number of items) of an object. The argument may be a sequence (such as a string, bytes, tuple, list, or range) or a collection (such as a dictionary, set, or frozen set).


## [strings](https://docs.python.org/3/tutorial/introduction.html#strings)

```python
# `\` can be used to escape quotes  
a = 'doesn\'t'

# If you don’t want characters prefaced by `\` to be interpreted as special characters, you can use raw strings by adding an `r` before the first quote  
a = r'\n'

# Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated. This feature is particularly useful when you want to break long strings:
text = ('Put several strings within parentheses '
        'to have them joined together.')

# If you want to concatenate variables or a variable and a literal, use `+`:
text + 'something'

# substring and accessing character

# 1. Strings can be indexed (subscripted), with the first character having index 0. There is no separate character type; a character is simply a string of size one:
word = 'Python'
word[0]

# 2. Indices may also be negative numbers, to start counting from the right:
word[-1]

# In addition to indexing, slicing is also supported. While indexing is used to obtain individual characters, slicing allows you to obtain substring:
word[0:2] # characters from position 0 (included) to 2 (excluded)
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end

# Note how the start is always included, and the end always excluded. 
# s[:i] + s[i:] is always equal to s:

# One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1



```
