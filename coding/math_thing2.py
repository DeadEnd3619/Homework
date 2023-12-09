import cmath

a = float(input('input a number'))
b = float(input('input a number'))
c = float(input('input a number'))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))



def find_arithmetic_mean(numbers):
    if len(numbers) == 0:
        return None

    total = sum(numbers)
    mean = total / len(numbers)
    return mean



numbers = input('Enter numbers separated by spaces: ').split()
numbers = [int(num) for num in numbers]  

num_of_numbers = len(numbers)

if num_of_numbers == 0:
    print("The list is empty, so there is no mean.")
else:
    sum_of_numbers = sum(numbers)
    arithmetic_mean = sum_of_numbers / num_of_numbers

    whole_divisions, remainder = divmod(sum_of_numbers, num_of_numbers)

    print("Arithmetic Mean:", arithmetic_mean)
    print("Number of Whole Divisions:", whole_divisions)
    print("Remainder:", remainder)