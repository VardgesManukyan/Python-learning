# 1.
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return instead of the empty string. 
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Skzbi 2 tarery + Verji 2 tarery
s="barev"
a=s[:2]
v=s[-2:]
print(a+v)

# 2.
# Write a Python program to get a string from a given string where all occurrences 
# of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

s="restart"
s=a+s[1:].replace("r","$")
print(s)

# 3.
# Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'
# Trvatse 2hat string, tal ppoxelov erku rajin tarery orinak("1234", "7890"="7834", "1290")

s="qyal"
g="mard"
a=s[:2]+g[-2:]
b=g[:2]+s[-2:]
print(a+  " "  +b)

# 4.
# Write a Python program to add 'ing' at the end of a given 
# string (length should be at least 3). If the given string already 
# ends with 'ing' then add 'ly' instead. If the string length of the 
# given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly
# Stringi verjic avelacnel "ing", ete trvatsy verjanu "ing"-ov apa avelacnel "ly"
s="wrestl"   
if s[-3:]=="ing":
	s=s+"ly"
else:
	s=s+"ing"

print(s)	
