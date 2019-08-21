URL:    
[python-regular-expression-tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)

#### Basic Patterns: Ordinary Characters
1.  script: basic_pattern.py
2.  detail: Matching themselves exactly and do not have a special meaning in their regular expression syntax

#### Wild Card Characters: Special Characters
1.  script: special_characters.py
2.  Cheat sheet
    
    |Characters|Function|
    |:---|:---|
    |.|A period. Matches any single character except newline character|
    |\w|Matches any single letter, digit or underscore|
    |\W|Matches any character not part of \w (lowercase w)|
    |\s|Matches a single whitespace character like: space, newline, tab, return|
    |\S|Matches any character not part of \s|
    |\t|Matches tab|
    |\n|Matches newline|
    |\r|Matches return|
    |\d|Matches decimal digit 0-9|
    |^|Matches a pattern at the start of the string|
    |$|Matches a pattern at the end of string|
    |[abc]|Matches a or b or c|
    |[a-zA-Z0-9]|Matches any letter from (a to z) or (A to Z) or (0 to 9). Characters that are not within a range can be matched by complementing the set. If the first character of the set is ^, all the characters that are not in the set will be matched.|
    |\A|Matches only at the start of the string. Works across multiple lines as well|
    |\b|Matches only the beginning or end of the word|
    |\\|If the character following the backslash is a recognized escape character, then the special meaning of the term is taken. For example, \n is considered as newline. However, if the character following the \ is not a recognized escape character, then the \ is treated like any other character and passed through.|

#### Repetitions
1.  script: repetitions.py
2.  Cheat sheet

    |Characters|Function|
    |:---|:---|
    |+|Checks for one or more characters to its left|
    |*|Checks for zero or more characters to its left|
    |?|Checks for exactly zero or one character to its left|
    |{x}|Repeat exactly x number of times|
    |{x,}|Repeat at least x times or more|
    |{x, y}|Repeat at least x times but no more than y times|