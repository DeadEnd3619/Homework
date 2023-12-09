




# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump <= mpg * fuel_left:
#         return True
#     else:
#         return False

# def area_or_perimeter(l , w):
#     if l == w:
#         return l * w
#     else:
#         return l * 2 + w * 2

# def double_char(s):
#     result = ""
#     for char in s:
#         result += char * 2
#     return result

# def remove_exclamation_marks(s):
#     result = ''
#     for x in s:
#         if x != '!':
#             result += x
#     return result

'''Here you can just use .replace to change the "!" to "" aka blank '''

# def is_pangram(s):
#     uni = set()
#     for x in s:
#         if x.isalpha():
#             uni.add(x.lower())
#     if len(uni) == 26:
#         return True
#     else:
#         return False

# def to_jaden_case(string):
#     words = string.split(' ')
#     capitalized_words = [letter.capitalize() for letter in words]
#     jaden_case_string = ' '.join(capitalized_words)
#     return jaden_case_string

'''using split makes a miltipule lists and "[word.capitalize() for word in words]" takes the first letter and capitalizes it through a for loop. .join takes these lists and combines them with a space between them.'''
'''.split would allow inputs to be randomized through .random choice of the follow split.'''

# def expanded_form(num):
#     constant = 0
#     result = ""
#     Num_list = []
#     Num_str = str(num)[::-1]
#     for x in Num_str:
#         if x != '0':
#             Num_list.append(str(int(x) * 10 ** constant))
#         constant += 1
#     result = ' + '.join(Num_list[::-1])
#     return result

# def camel_case(s):
#     words = s.split(' ')
#     capitalized_words = [letter.capitalize() for letter in words]
#     jaden_case_string = ''.join(capitalized_words)
#     return jaden_case_string

'''heres a lesson in coding, reduce, reuse, recycle.'''

# def get_count(sentence):
#     vowels = 0
#     for x in sentence:
#         if x.lower() in ('a', 'e', 'i', 'o', 'u'):
#             vowels += 1
#     return vowels

# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# def likes(names):
#     Likes = len(names)
#     if Likes == 0:
#         print('no one likes this')
#     elif Likes == 1:
#         print(f'{names[0]} likes this')
#     elif Likes == 2:
#         print(f'{names[0]} and {names[1]} like this')
#     elif Likes == 3:
#         print(f'{names[0]}, {names[1]} and {names[2]} like this')
#     elif Likes >= 4:
#         print(f'{names[0]}, {names[1]} and {Likes - 2} others like this')
#     else:
#         print('invalid input')

# bad_names = input('')
# names = bad_names.split(' ')
# likes(names)

# def max_sequence(arr):
#     max_sum = float('-inf')
#     current_sum = 0
#     all_negative = True
#     for num in arr:
#         if num >= 0:
#             all_negative = False
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum if not all_negative else 0

# def generate_hashtag(s):
#     words = s.split(' ')
#     capitalized_words = [letter.capitalize() for letter in words]
#     jaden_case_string = ''.join(capitalized_words)
#     if jaden_case_string == '':
#         return False
#     elif len(jaden_case_string) >= 140:
#         return False
#     else:
#         return '#' + jaden_case_string

'''
original_string = "world"
character_to_add = "h"
new_string = "{}{}".format(character_to_add, original_string)

print(new_string)
'''

# def xo(s):
#     x_counter = 0
#     o_counter = 0
#     for x in s:
#         if x == 'x' or x == 'X':
#             x_counter += 1
#         elif x == 'o' or x == 'O':
#             o_counter += 1
#         else:
#             pass
#     if x_counter == o_counter:
#         return True
#     else:
#         return False

# def Descending_Order(num):
#     s = str(num)
#     s = list(s)
#     s = sorted(s)
#     s = reversed(s)
#     s = ''.join(s)
#     return int(s)







# def are_you_playing_banjo(name):
#     constant = 0
#     for x in name:
#         if constant == 0:
#             if x == ('R', 'r'):
#                 return name + ' plays banjo'
#             constant += 1
#     return name + " does not play banjo"





# from itertools import permutations
# def print_string_variations(input_string):
#     string_permutations = permutations(input_string)
#     for permutation in string_permutations:
#         print(''.join(permutation))
# user_input = input("Enter a string: ")
# print_string_variations(user_input)




# def rgb(r, g, b):
#     r = max(0, min(255, round(r)))
#     g = max(0, min(255, round(g)))
#     b = max(0, min(255, round(b)))
#     hex_value = "{:02X}{:02X}{:02X}".format(r, g, b)
#     return hex_value






# def format_duration(seconds):
#     if seconds < 0:
#         return "Invalid input. Please provide a non-negative number of seconds."
#     elif seconds == 0:
#         return "now"
#     years, seconds = divmod(seconds, 31536000)
#     days, seconds = divmod(seconds, 86400)
#     hours, seconds = divmod(seconds, 3600)
#     minutes, seconds = divmod(seconds, 60)
#     formatted_units = []
#     if years > 0:
#         formatted_units.append("{} year{}".format(years, 's' if years != 1 else ''))
#     if days > 0:
#         formatted_units.append("{} day{}".format(days, 's' if days != 1 else ''))
#     if hours > 0:
#         formatted_units.append("{} hour{}".format(hours, 's' if hours != 1 else ''))
#     if minutes > 0:
#         formatted_units.append("{} minute{}".format(minutes, 's' if minutes != 1 else ''))
#     if seconds > 0:
#         formatted_units.append("{} second{}".format(seconds, 's' if seconds != 1 else ''))
#     if len(formatted_units) == 1:
#         return formatted_units[0]
#     formatted_time = ", ".join(formatted_units[:-1]) + " and " + formatted_units[-1]
#     return formatted_time


'''The "divmod" function devides the 1st value by the second value and gives the ammount of times it can be divded and the remainder. '''


