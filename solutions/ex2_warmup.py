# Warm Up questions
# Warm up Questions

# Q1) Given a string input from the user, only output first-half of the string.

user_input = input('Enter a word: ')

halfway = len(user_input) // 2
first_half = user_input[:halfway]

print('First half of', user_input, 'is', first_half)

# Q2) Given a string, flip the string where the second half of the word is moved to the front.

second_half = user_input[halfway:]
flipped_word = second_half + first_half
print('This is the result when we flip our word:', flipped_word)

# Q3) Create a program to checks upon two strings. If one of the strings is found at the end of the word, output/return True … otherwise output/return False. The program is not case sensitive.

user_input2 = input('Enter another word: ')

# check if both inputs are the same
if user_input.lower() == user_input2.lower():
    print(user_input, 'ends with', user_input2)
else:
    # the two inputs are not equal to each other
    if user_input.lower().endswith(user_input2.lower()):
        print(user_input, 'ends with', user_input2)
    elif user_input2.lower().endswith(user_input.lower()):
        print(user_input2, 'ends with', user_input)
    else:
        print('The words do not end with each other.')
