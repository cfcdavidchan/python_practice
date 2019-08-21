import re

# . - A period. Matches any single character except newline character
pattern = r'.{0,}k'
sequence = "Cookie"

print (re.search(pattern, sequence).group())

#\w - Lowercase w. Matches any single letter, digit or underscore.
pattern = r'\wo\w'
sequence = "Cookie"
print (re.search(pattern, sequence).group())

#\W - Uppercase w. Matches any character not part of \w (lowercase w).
pattern = r'\Wook'
sequence = "@ookie"
print (re.search(pattern, sequence).group())

#\s - Lowercase s. Matches a single whitespace character like: space, newline, tab, return.
pattern = r'Eat\scake'
sequence = 'Eat cake'
print (re.search(pattern, sequence).group())

#\S - Uppercase s. Matches any character not part of \s (lowercase s).
pattern = r'Cook\Se'
sequence = 'Cookie'
print (re.search(pattern, sequence).group())

#\t - Lowercase t. Matches tab.
pattern = r'Eat\tcake'
sequence = 'Eat\tcake'
print (re.search(pattern, sequence).group())

#\n - Lowercase n. Matches newline.
# \r - Lowercase r. Matches return.
# \d - Lowercase d. Matches decimal digit 0-9.
pattern = r'c\d\dkie'
sequence = 'c00kie'
print (re.search(pattern, sequence).group())

#^ - Caret. Matches a pattern at the start of the string.
pattern = r'^Eat Cak'
sequence = 'Eat Cake'
print (re.search(pattern, sequence).group())

# $ - Matches a pattern at the end of string.
pattern = r't cake$'
sequence = 'Eat cake'
print (re.search(pattern, sequence).group())

#[0-6] - Matches 0-6
pattern = r'Number: [0-6]'
sequence = 'Number: 5'
print (re.search(pattern, sequence).group())

# Matches any character except 5
pattern = r'Number: [^5]'
sequence = 'Number: 0'
print (re.search(pattern, sequence).group())

# \A - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
pattern = r'\A[A-E]ookie'
sequence = 'Cookie'
print (re.search(pattern, sequence).group())

# \b - Lowercase b. Matches only the beginning or end of the word.
pattern = r'\b[A-Da-d]ookie\\'
sequence = 'Cookie\\'
print (re.search(pattern, sequence).group())