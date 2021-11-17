def tower_builder(n_floors):
    floors = []
    num = n_floors
    for i in range(n_floors):
        num -= 1
        floors.append(' ' * num + '*' * (i * 2 + 1) + ' ' * num)
    return floors


print(tower_builder(3))