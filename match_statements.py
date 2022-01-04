def arithmetic(a, b, operator):
    math = operator
    match math:
        case 'add':
            return a + b
        case 'subtract':
            return a - b
        case 'multiply':
            return a * b
        case 'divide':
            return a / b

print(arithmetic(5,2,"add"))