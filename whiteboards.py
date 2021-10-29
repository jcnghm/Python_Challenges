# You get an array of numbers, return the sum of all of the positives ones.


# Example 1
# ---------
# Input: [1,-4,7,12] 
# Output: 20
# Explanation: 1 + 7 + 12 = 20

# Example 2
# ---------
# Input: [-1,-3,-7,15] 
# Output: 20
# Explanation: 15 = 15

# Example 3
# ---------
# Input: [] 
# Output: 0

# Note: if there is nothing to sum, the sum is default to 0.

list1 = [1,-4,7,12] 

def sumPos(nums):
    new_list = []
    for i in nums:
        if i > 0:
            new_list.append(i)
    return sum(new_list)

sumPos(list1)


# You are given a list of unique integers (arr), and two integers (a and b). Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value (True if a and b are consecutive, False otherwise).

# It is guaranteed that a and b are both present in arr.

# Example Input: isConsecutive([1, 6, 9, -3, 4, -78, 0], -3, 4)
# Output: True

# Example Input: isConsecutive([3,1,0,19], 19, 0)
# Output: True

arr1=[3,1,0,19]
a = 19
b = 1

def isConsecutive(arr,a,b):
    indexA = arr.index(a)
    indexB = arr.index(b)
    if indexA == (indexB + 1) or indexA == (indexB - 1):
        return True

    else:
        return False



isConsecutive(arr1,a,b)

num = 15

def descending_order(num):
    number = str(num)
    number = ''.join(sorted(number))
    number = number[::-1]
    number = int(number)

    return number

descending_order(15)
str = "hey fellow warriors"

def spin_words(sentence):
    sen = sentence.split(" ")
    new_str = []
    for i in sen:
        if len(i) >=5:
            new_str.append(i[::-1])
        else:
            new_str.append(i)
    return new_str
spin_words(str)

