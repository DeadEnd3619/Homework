sample_data = '''Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are'''
print(sample_data)



input_data = input("Enter a sequence of comma-separated numbers: ")
numbers = input_data.split(", ")
number_list = [num.strip() for num in numbers]  # Remove extra spaces
number_tuple = tuple(number_list)
print("List:", number_list)
print("Tuple:", number_tuple)

a = input('put some wacky spaces between your numbers: ').split()
b = input('put some wacky spaces between your numbers: ').split()
common_elements = list(set(a) & set(b))
print(common_elements)



letter = input("Enter a letter: ").lower()
if letter in 'aeiou':
    print("True")
else:
    print("False")


numbers = [
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527
]

even_numbers = []

for number in numbers:
    if number == 237:
        break
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)