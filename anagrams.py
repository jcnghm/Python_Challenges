def anagrams(word, words):
    anagram = sorted(word)
    print(anagram)
    return [i for i in words if anagram == sorted(i)]

# Test Cases
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))

print(anagrams('laser', ['lazing', 'lazy',  'lacer']))