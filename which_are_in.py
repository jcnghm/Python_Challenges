# Return the words in a1 if they are in the words in a2

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

def in_array(array1, array2):
    words = []
    for word in array2:
        for sec in array1:
            if sec in word:
                words.append(sec)
    words = list(set((words)))
    return sorted(words)

print(in_array(a1, a2))