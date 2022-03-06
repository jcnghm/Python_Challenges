# Given a string s, find the first non-repeating character in it 
# and return its index. If it does not exist, return -1.
# Example 1:
# Input: s = "codingtemple"
# Output: 0
# Example 2:
# Input: s = "codingcodingalumni"
# Output: 12
# Example 3:
# Input: s = "ctct"
# Output: -1

def first_unique(string):
    for i in range(len(string)):
        if string.count(string[i]) == 1:
            return i
    return -1



print(first_unique("codingcodingalumni"))
print(first_unique("ctct"))

