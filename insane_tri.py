def triangle(row):
    results = [3**i+1 for i in range(10) if 3**i<=100000][::-1]
    print(results)
    for length in results:
        while len(row) >= length:
            row = [row[i] 
            if row[i] == row[i+length-1] 
            else ({"R","G","B"} - {row[i],row[i+length-1]}).pop() 
            for i in range(len(row) - length+1)]
    return row[0]

print(triangle('GB'))