# String Exercise 1
'''
# q3) Create a program that outputs the inputted string backwards.

user_input = input('Enter a word: ')

print(user_input[::-1]) # [::-1] slicing helps us to reverse a string

# Create a program such that it determines if there are more vowels than consonants in the given inputted string. Assume that te input is all lowercased
'''

user_input = input('Enter a word: ')
vowel_counter = 0
consonant_counter = 0

for character in user_input:
    if character in 'aeiou':
        vowel_counter += 1
    else:
        consonant_counter +=1

if vowel_counter> consonant_counter:
    print('There are more vowels than consonants in', user_input)
elif vowel_counter == consonant_counter:
    print('There equal amounts of vowels and consonants in', user_input)
else:
    print('There are more consonants than vowels in', user_input)

    # q5) Create a program that counts the number of characters from the inputted string such that are not found in the set of lowercase alphabets.

'''
user_input = input('Enter a string: ')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
counter = 0

for character in user_input:
    if character not in alphabet:
        counter += 1

print('There are', counter, 'characters that are not part of the lowercased alphabets.')
'''

# q6) Create a program that determines if the two inputted words are palindromes

word1 = input('Enter word 1: ')
word2 = input('Enter word 2: ')

word1_reversed = word1[::-1]
word2_reversed = word2[::-1]

if word1_reversed == word1:
    print(word1, 'is a palindrome.')
else:
    print(word1, 'is not a palindrome.')

if word2_reversed == word2:
    print(word2, 'is a palindrome.')
else:
    print(word2, 'is not a palindrome.')
