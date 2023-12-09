word = input("please enter a word: ")

for letter in word:
    print(letter)



user_input = input("Enter multiple words separated by commas: ")

words = [word.strip() for word in user_input.split(',')]

if words:
    max_word = max(words, key=len)
    max_letters = len(max_word)
    
    print(f"The word with the most letters is: {max_word}")
    print(f"It has {max_letters} letters.")
else:
    print("No words entered.")




sentence = input("Enter a sentence: ")

if sentence:

    first_letter = sentence[0]
    last_letter = sentence[-1]

    swapped_sentence = last_letter + sentence[1:-1] + first_letter

    print("Original sentence:", sentence)
    print("Swapped sentence:", swapped_sentence)
else:
    print("No input sentence provided.")




word_to_insert = input("Enter a word to insert: ")

word_to_wrap = input("Enter a word to wrap in HTML tags: ")

html_string = f"<{word_to_wrap}>{word_to_insert}</{word_to_wrap}>"

print("HTML Result:", html_string)