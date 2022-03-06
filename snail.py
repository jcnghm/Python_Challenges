def snail(array):
    results = []
    while len(array) > 0:
        results += array[0]
        del array[0]

        if len(array) > 0:
            for i in array:
                results += [i[-1]]
                del i[-1]

            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results


data = [[1, 2, 3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10, 9, 8, 7]]

data2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
expected2 = [1, 2, 3, 6, 9, 8, 7, 4, 5]

print(snail(data2))