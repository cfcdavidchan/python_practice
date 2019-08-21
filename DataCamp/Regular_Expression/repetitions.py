import re

# + - Checks for one or more characters to its left.
pattern = r'Co+'
sequence = "Cooookie"
print (re.search(pattern, sequence).group())

# * - Checks for zero or more characters to its left
pattern = r'Ca*'
sequence = "Ceke"
print (re.search(pattern, sequence).group())

# ? - Checks for exactly zero or one character to its left
pattern = r'Colou?r'
sequence = "Colour"
print (re.search(pattern, sequence).group())

# {x} - Repeat exactly x number of times.
# {x,} - Repeat at least x times or more.
# {x, y} - Repeat at least x times but no more than y times.
pattern = r'\d{0,2}'
sequence = '0987654321'
print (re.search(pattern, sequence).group())