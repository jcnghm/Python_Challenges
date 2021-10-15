# Return True if string is an Isogram

def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True