
list_1 = [1,11,14,5,8,9]

def func(list):
    return [i for i in list if i < 10]

print(func(list_1))



l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def combine(l1, l2):
    # result = sorted(l1+l2)
    # return result
    return [i for i in sorted(l1+l2)]

print(combine(l_1,l_2))


