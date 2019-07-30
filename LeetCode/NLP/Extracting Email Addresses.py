"""
https://www.geeksforgeeks.org/extracting-email-addresses-using-regular-expressions-python/
"""

"""
Let suppose a situation in which you have to read some specific data like phone numbers, email addresses, dates, a collection of words etc.
How can you do this in a very efficient manner?The Best way to do this by Regular Expression.

Let take an example in which we have to find out only email from the given input by Regular Expression.

Input  : Hello shubhamg199630@gmail.com Rohit neeraj@gmail.com
Output : shubhamg199630@gmail.com neeraj@gmail.com
Here we have only selected email from the given input string.

Input : My 2 favourite numbers are 7 and 10
Output :2 7 10
Here we have selected only digits.

$	            Matches the end of the line
\s	            Matches whitespace
\S	            Matches any non-whitespace character
*	            Repeats a character zero or more times
\S	            Matches any non-whitespace character
*?	            Repeats a character zero or more times (non-greedy)
+	            Repeats a character one or more times
+?	            Repeats a character one or more times (non-greedy)
[aeiou]	        Matches a single character in the listed set
[^XYZ]	        Matches a single character not in the listed set
[a-z0-9]	    The set of characters can include a range
(	            Indicates where string extraction is to start
)	            Indicates where string extraction is to end
"""

import re

## Example 1: Extract numeric digit
s = 'My 2 favourite numbers are 7 and 10'
lst = re.findall('[0-9]+', s)
print(lst)

## Example 2: Extract emails
s = 'Hello from shubhamg199630@gmail.com to priya@yahoo.com, about the meeting @2PM'

# \S matches any non-whitespace character
# @ for as in the Email
# + for Repeats a character one or more times
lst = re.findall('\S+@[0-9A-Za-z.]+', s)
print(lst)










