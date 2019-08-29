import re

def is_pangram(sentence):
    matchReference = re.match(r'.[A-Za-z]', sentence) # flag L to locale
    if matchReference:
    	return True
    else:
    	return False  # not complete

#from string import ascii_lowercase

#ALPHABET = set(ascii_lowercase)

#def is_pangram(string):
    #return ALPHABET.issubset(string.lower())	