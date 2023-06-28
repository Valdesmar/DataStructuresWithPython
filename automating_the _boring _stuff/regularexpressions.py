# Regular expressions section

##########################
# Regular expressions module
import re

'''
 Regular expressions are mini-language for specifying text
patterns. Writing code to do pattern matching without 
regular expressions is a huge pain.
 Regex strings often use \ backslash (like \d), so they are
often raw strings:r"\d".
 Import the re module first.
 Call the re.compile() function to create a regex object.
 Call the regex objects's search() method to create a 
match object.
 Call the regex object's group() method to get matched 
string.
 \d is the regex for a numeric digit character.
'''


# message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# Using parenthesis while searching, groups elements together.
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
#                               (group1) (group2) (group3)
# mo = phoneNumRegex.search(message)
# print(mo.group())

# To find all matchs of the message

# mo2 = phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 415-555-9999')
# print(mo2)

# Pipe character

# Enables multiples choices for the search
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo1 = batRegex.search('Batmobile lost a wheel')
# print(mo1.group())


# Repetition in gerex patterns and greedy/nongreedy

# batRegex = re.compile(r'Bat(wo)?man') # same use as the pipe charac
# mo2 = batRegex.search('The adventures of Batman')
# print(mo2.group())
# mo2 = batRegex.search('The adventures of Batwoman')
# print(mo2.group())

# batRegex = re.compile(r'Bat(wo)*man') # it will match even with multiple wo
# mo = batRegex.search('The adventures of Batwowowowowoman')
# print(mo.group())

# Recap
# ? means 0 or 1 
# * means 0 or more
# + means 1 or more

# batRegex = re.compile(r'(Ha){3}')
# mo = batRegex.search('He said HaHaHa')
# print(mo.group())

# phoneNumRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
# ((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3} 
# (\d\d\d)? this part can be on match or not
# (,)? this means the phone numbes can be separated by coma or not
# {3} this means there should be 3 matches
# mo1 = phoneNumRegex.search('My numbers are 415-555-1245,555-4242,212-555-0000')
# print(mo1.group())

# {3} can also get a range ,like: {3, 5}

# digitRegex = re.compile(r'(\d){3,5}')
# mo3 = digitRegex.search('12345678') # Greedy match, matches the longest string
# print(mo3.group())

# digitRegex = re.compile(r'(\d){3,5}?')
# mo3 = digitRegex.search('12345678') # Non-Greedy match
# print(mo3.group())


# Regex character classes and the findall method

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# findall allows to find all matches in a text
# returns the matches as list of tuples


# Regex object
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping,\
      9 ladies dancing, 8 maids a milking, 7 swans a swimming, \
        6 geese a laying, 5 gold rings, 4 calling birds, 3 french hens,\
              2 turtle doves, and 1 partridge in a pear tree.'

# xmasRegex = re.compile(r'\d+\s\w+')
# lyrcisMatch = xmasRegex.findall(lyrics)
# print(lyrcisMatch)

vowelRegex = re.compile(r'[aeiouAEIOU]') # match for every vowel in str
vowelMatch = vowelRegex.findall('Robocop eats baby food.')
print(vowelMatch) 

vowelRegex = re.compile(r'[aeiouAEIOU]{2}') 
# match for every 2 vowels in string

consonantRegex = re.compile(r'[^aeiouAEIOU]') 
# Ignores the vowels, ^ ignores what is stated



########################
# Regular expressions End






























