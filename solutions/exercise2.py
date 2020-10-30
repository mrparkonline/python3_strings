# Exercise 2
# q1) Ask the user’s first and last name , and print it all UPPERCASED.

first_name = input('Enter your first name: ').upper()
last_name = input('Enter your last name: ').upper()

print(first_name, last_name)

# q2a) Create a program that outputs a string containing all the duplicate characters in a string.

# q2b) Determine the most used letter in a string.

word = input('Enter a word: ')

duplicate_letters = ''
most_occurring = ''
counter = 0

for character in word:
    if (word.count(character) > 1) and (character not in duplicate_letters):
        duplicate_letters += character

    if word.count(character) > counter and character != most_occurring:
        most_occurring = character
        counter = word.count(character)

print('These are the duplicate character in', word, ':', duplicate_letters)
print('The most occurring character is:', most_occurring)

# q3) Create a program such that it outputs the number of uppercase characters and lowercase characters

user_input = input('Enter a word: ')

upper_count = 0
lower_count = 0

for c in user_input:
    if c.islower():
        lower_count += 1
    elif c.isupper():
        upper_count += 1

print('There are', lower_count, 'lowercased letters.')
print('There are', upper_count, 'uppercased letters.')

# q4) Examine the following string pattern:
# *
# **
# ***
# ****
# if input was 4

# method 1: using concatenation
user_input = int(input('Enter value for N: '))
string_pattern = '*'

for i in range(user_input):
    print(string_pattern)
    string_pattern += '*'

# method 2: repeating
string_pattern = '*'
for i in range(1, user_input+1):
    print(string_pattern * i)

# method 3: slicing!
string_pattern = '*' * user_input
for i in range(1, user_input+1):
    print(string_pattern[:i])

# Q5) Create a program that cleans up the user's input.
# whitespace removal

temp_word = '   h e  l l o  wo r l d !   '
print('lstrip():', temp_word.lstrip())
print('rstrip():', temp_word.rstrip())
print('strip():', temp_word.strip())
print('replace(\' \',\'\'):', temp_word.replace(' ', ''))

# q6) Removing Character one by one
'''
user_input = input('Enter a word: ')

# Removing the front most characters
for i in range(0, len(user_input)):
    print(user_input[i:])

# Removing the back most characters
for i in range(len(user_input), 0, -1):
    print(user_input[:i])
'''

# q7) Numeric Pattern with Strings
'''
user_input = int(input('Enter a value N: '))

for num in range(1, user_input+1):
    print(str(num) * num)
'''

# q8) Star Pattern
'''
user_input = int(input('Enter value N: '))

for num in range(1, user_input+1):
    print('*' * num)

for num in range(user_input-1, 0, -1):
    print('*' * num)
'''

# q9) 101010 Pattern
'''
user_input = int(input('Enter value N: '))

pattern = '' # empty string initialized
for num in range(1, user_input+1):
    if num % 2 == 0:
        # num is even
        pattern += '0'
    else:
        # num is odd
        pattern += '1'

    print(pattern)
    #input()
# end of for loop

pattern = '10' * user_input
print('currently pattern is:', pattern)

for i in range(1, user_input+1):
    print(pattern[:i])
'''

# q10) Sorting a string alphabetically
user_input = input('Enter a word to sort alphabetically: ')

sorted_input = '' # this is the variable that will contain the sorted string

while user_input:
    # This means, we are looping until user_input becomes empty

    # Look for the smallest value
    smallest_value = min(user_input)
    # Count how many times it occurs
    occurence = user_input.count(smallest_value)

    # Add the smallest values to the sorted input
    sorted_input += smallest_value * occurence

    # Remove the smallest values from the input
    user_input = user_input.replace(smallest_value, '')

    #print('sorted_input:', sorted_input)
    #print('user_input:', user_input)
    #input()

# end of while loop
print('Sorted string:', sorted_input)

# q11: Sort a string where the vowels are placed first then the consonants
'''
user_input = input('Enter a word: ')

sorted_word = '' # empty string initialized
vowels = ''
consonants = ''

for character in user_input:
    if character.lower() in 'aeiou':
        vowels += character
    else:
        consonants += character

sorted_word = vowels + consonants
print('Result:', sorted_word)
'''

#q12: Take two strings, and then sort them into a single string in REVERSE Alphabetical Order
'''
word1 = input('Enter word 1: ')
word2 = input('Enter word 2: ')

alpha = 'abcdefghijklmnopqrstuvwxyz'
upper_alpha = alpha.upper()

reverse_order = alpha[::-1] + upper_alpha[::-1]
#print(reverse_order)

sorted_word = ''

for character in reverse_order:
    w1_count = word1.count(character)
    w2_count = word2.count(character)

    if w1_count >= 1:
        sorted_word += character * w1_count
        word1.replace(character, '')

    if w2_count >= 1:
        sorted_word += character * w2_count
        word2.replace(character, '')

print('Both words in reverse order sorted:', sorted_word)
'''

# q13: Anagram -- Check if two strings are anagrams of each other

# a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

word1 = input('Enter word1: ')
word2 = input('Enter word2: ')

cleaned_word1 = ''
# Remove impurities from each string
for character in word1:
    if character.isalpha():
        cleaned_word1 += character.lower()

cleaned_word2 = ''
# Remove impurities from each string
for character in word2:
    if character.isalpha():
        cleaned_word2 += character.lower()

#print(cleaned_word1, cleaned_word2)

if len(cleaned_word1) != len(cleaned_word2):
    print(word1, 'and', word2, 'are not anagrams.')
else:

    anagram = True # we have a variable that assumes that the two words are anagrams.

    for character in cleaned_word1:
        if cleaned_word1.count(character) != cleaned_word2.count(character):
            anagram = False

    if anagram:
        print(word1, 'and', word2, 'are anagrams!')
    else:
        print(word1, 'and', word2, 'are not anagrams.')
