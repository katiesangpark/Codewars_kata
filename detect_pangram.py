## a Function to determine Pangram
## Input: any sentence
## Output: True/False
import string
def is_pangram(s):
    
    ## convert the input sentence to lowercase.
    sentence = s.lower()
    
    ## expected 26 letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    # Get each letter from alphabet
    for char in alphabet:
        #Check if the letter is in the sentence or not
        if char not in sentence:
                return False
    return True
