def alphabet_position(text):
    text = text.lower()
    print(text)
    res = ""
    index = 0
    while index < len(text):
        item = text[index]
        if ord(item) > ord("z") or ord(item) < ord("a"):
            index +=1
            continue
        res += str(ord(item) - ord("a")+1) + " "
        index += 1
    return res[:-1]

alphabet_position("The sunset sets at twelve o' clock.")