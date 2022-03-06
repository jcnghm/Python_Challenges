# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

def reverse_vowels(s):
    vowels=[]
    for letter in s:
        if letter.lower() in 'aeiou':
            vowels.append(letter)
    vowels= vowels[::-1]
    answer=''
    count=0
    for letter in s:
        if letter.lower() in 'aeiou':
            answer+=vowels[count]
            count+=1
        else:
            answer+=letter
    return answer

print(reverse_vowels('hello'))
print(reverse_vowels('leetcode'))
print(reverse_vowels('hihowareyou'))
print(reverse_vowels('testing'))