

def unique_in_order(iterable):
        if iterable == None:
            return None
        elif iterable == []:
            return []
        elif iterable == '':
            return []
        result = []
        i = 0
        while i < len(iterable)-1:
            if iterable[i] == iterable[i+1]:
                i += 1
                continue
            result.append(iterable[i])
            i += 1
        result.append(iterable[i])
        return result


print(unique_in_order('AAAABBBCCDAABBB'))