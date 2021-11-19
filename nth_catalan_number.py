# What is a Catalan number?
# In combinatorial mathematics, the Catalan numbers form a sequence of natural numbers that occur 
# in various counting problems, often involving recursively-defined objects. They are named after the 
# Belgian mathematician Eugène Charles Catalan (1814–1894).

# Using zero-based numbering, the nth Catalan number is given directly in terms of binomial coefficients by:


# You can read more on Catalan numbers Here.

# Task:
# Implement a function which calculates the Nth Catalan number.

# 0  =>  1
# 3  =>  5
# 7  =>  429
# 9  =>  4862


def nth_catalan_number(n):
    
    if n == 0 or n == 1:
        return 1

    catalan = [0 for i in range(n + 1)]

    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

    return catalan[n]

print(nth_catalan_number(9))