

if __name__ == '__main__':

    birthdays = {
        'Zach': '05/08/1989',
        'Mom': '05/20/1961',
        'Dad': '04/05/1958',
        'Ezra': '01/27/2021',
        'Felicia': '07/06/1986'}

    print('Welcome to the birthday dictionary. We know the birthdays of:')
    for name in birthdays:
        print(name)

    print('Who\'s birthday do you want to look up?')
    name = input()
    if name in birthdays:
        print('{}\'s birthday is {}.'.format(name, birthdays[name]))
    else:
        print('Sadly, we don\'t have {}\'s birthday.'.format(name))