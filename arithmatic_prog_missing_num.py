# An Arithmetic Progression is defined as one in which there is a constant 
# difference between the consecutive terms of a given series of numbers. 
# You are provided with consecutive elements of an Arithmetic Progression. 
# There is however one hitch: exactly one term from the original series is 
# missing from the set of numbers which have been given to you. The rest of 
# the given series is the same as the original AP. Find the missing term.

# You have to write a function that receives a list, list size will always 
# be at least 3 numbers. The missing term will never be the first or last one.

# input = find_missing([1, 3, 5, 9, 11])
# output = 7

def find_missing(sequence):
    counts = []
    counter = len(sequence)
    while counter > 0:
        for i in sequence:
            counts.append(sequence[counter-1] - sequence[counter-2])
            counter -= 1
        counts.pop()
    counts = counts[::-1]
    for i in range(len(counts)):
        if counts.count(counts[i]) == 1:
            sequence.insert(i + 1, (sequence[i] + counts[-1]))
            result = sequence[i] + counts[-1]
    print(sequence)
    return result

    
    
            
    







print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))