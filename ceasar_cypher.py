# Caesar Cipher (caesar.py)

# A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter found by moving n places down the alphabet. For example, assume the input plain text is the following:

# abcd xyz
# If the shift value, n, is 4, then the encrypted text would be the following:

# efgh bcd
# You are to write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher. The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.

# Note: You can assume the plain text is all lowercase ASCII except for whitespace and punctuation.

# Method using translate

import string

def caesar(letters, num):
    a = string.ascii_lowercase
    mask = a[num:] + a[:num]
    trantab = str.maketrans(a, mask)
    return letters.translate(trantab)    

print(caesar("abcd xyz", 4))


# Method without using translate

import string

def shift_n(letter, amount):
    if letter not in string.ascii_lowercase:
        return letter
    new_letter = ord(letter) + amount
    while new_letter > ord("z"):
        new_letter -= 26
    while new_letter < ord("a"):
        new_letter += 26
    return chr(new_letter)


def caesar1(message, amount):
    enc_list = [shift_n(letter, amount) for letter in message]
    return "".join(enc_list)

print(caesar1("abcd xyz", 4))