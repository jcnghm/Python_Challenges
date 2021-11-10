# Prework in class notes

# Question 1 Examples
def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")

user_name = input("enter username:")
hello_name(user_name)

# Question 2 Examples

# def odd_numbers():
#     for n in range(1, 101, 2):
#          print(n)
# odd_numbers()

def odd_nums():
    return [n for n in range(1,101) if n % 2 != 0]
print(odd_nums())

#Question 3 Examples

def max_num_in_list(a_list):
    return max(a_list)
print(max_num_in_list([1, 2, 3, 4]))

# Question 4 Examples

def is_leap_year2(a_year):
    leap_year = False
    if a_year % 400 == 0:
        leap_year = True
    elif a_year % 100 == 0:
        leap_year = False
    elif a_year % 4 == 0:
       leap_year = True
    if leap_year == True:
        print(str(a_year) + " is a leap year!")
    else:
        print(str(a_year) + " is not a leap year.")

prompt = "\n Is this a leap year?"
prompt += "\n Please enter a year: "
test_year = int(input(prompt))

is_leap_year2(test_year)

# Question 5 examples


def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           print(a_list[i] + 1)
           print(a_list[i+1])
           i += 1
       else:
           status = False
           break
    return status
print(is_consecutive([1, 2, 3, 4, 5, 6]))

