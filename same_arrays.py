def delete_nth(order,max_e):
    print(order)
    # order = order[::-1]
    for num in order:
        print(num)
        if order.count(num) > max_e:
            order.remove(num)
    return order

print(delete_nth([20,37,20,21], 1))