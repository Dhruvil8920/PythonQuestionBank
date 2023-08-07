"""
Write a Python program to extract email addresses from a given text string.
The program should find all occurrences of valid email addresses in the text and print them as output.

Implement a function extract_email_addresses(text) that takes the input text as a string and returns a list of all valid email addresses found in the text.

A valid email address should satisfy the following conditions:

It should contain one '@' symbol.
The part before '@' can consist of one or more alphanumeric characters, dots (.), underscores (_), percentage signs (%), plus signs (+), or hyphens (-).
The part after '@' can consist of one or more alphanumeric characters, dots (.), or hyphens (-).
The email address should end with a valid top-level domain consisting of two or more uppercase or lowercase letters.

INPUT:
text = "Hello, my email is john@example.com. Please contact me there or at john.doe@example.co.uk."

Output:
['john@example.com', 'john.doe@example.co.uk']
Note:

The input text may contain other symbols, special characters, or random text alongside email addresses.
The program should only extract valid email addresses and ignore other patterns.
Consider using regular expressions to match email addresses.

"""

import re
def extract_email_addresses(text):
    pass



