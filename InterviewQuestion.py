# Interview Question
def SeatingStudents(arr):
    counter = 0
    class_size = arr[0]
    row_size = int(class_size/2)
    occupied = arr[1:]
    desks = []
    a = 0
    for i in range(row_size):
        desks.append([])
        for j in range(2):
            if(a+1) in occupied:
                taken = True
            else:
                taken = False
            desks[i].append(str(taken))
            a += 1
    
    for i in range(row_size-1):
        if desks[i][0] == str(False) and desks[i][1] == str(False):
            counter += 1
        elif desks[i][0] == str(False) and desks[i+1][0] == str(False):
            counter += 1
        elif desks[i][1] == str(False) and desks[i+1][1] == str(False):
            counter += 1
    if desks[row_size-1][0] == str(False) and desks[row_size-1][1] == str(False):
        counter += 1

    return counter
    



# keep this function call here 
# print(SeatingStudents(input()))

list = [6, 4]

print(SeatingStudents(list))