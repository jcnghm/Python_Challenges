# Write a function, add_it_up(), that takes a single integer as input and returns the sum of the integers from zero to the input parameter.

# The function should return 0 if a non-integer is passed in.

def add_it_up(num):
    list = []
    if type(num) != int:
        return 0
    else:
        for i in range(0,num + 1):
            list.append(i)
    return sum(list)

print(add_it_up(10))

def add_it(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

print(add_it(10))

def even_better(num):
    return sum(range(num + 1))

print(even_better(10))