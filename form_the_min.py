def min_value(digits):
    nums = sorted(list(set(digits)))
    results = [str(num) for num in nums]
    return int(''.join(results))


print(min_value([1,3,1]))