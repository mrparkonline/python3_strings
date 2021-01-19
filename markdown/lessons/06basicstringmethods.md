---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# Basic String Methods
---

In this lesson, we will be looking a string methods that deal with searching, checking the status, and editing strings.

This is __not an exhaustive list__ of all methods with strings. You check out the list of methods [here](https://docs.python.org/3/library/stdtypes.html#string-methods).

__Methods:__ set of code belonging to a certain data/object
- String and List data types have special methods only for them
- Usually, we need a period before the method name to use them

```
Example:

print('Hello {}!'.format('World'))

.format() is a string method!
```

__Return:__ certain methods and functions have the ability to return a value/result after its operations
- This is useful when we __assign the result to a variable__
- Built-in functions like: ```len(), max(), min(), int(), float()``` all return a new value so that we can assign the result to a variable or update an existing variable

### Search Related Methods

_Recall:_ Index starts at 0

__```string_data.count(_str_arg_)```__
- Returns how many time the string argument occurs in the given variable

__```string_data.find(_str_arg_)```__
- Returns the location of where the string argument  was found. If not found, returns -1

__```string_data.index(_str_arg_)```__
- Same as find(), but raises an [exception](https://www.tutorialspoint.com/python3/python_exceptions.htm#:~:text=In%20general%2C%20when%20a%20Python,otherwise%20it%20terminates%20and%20quits.) if str not found.



```python
# Search Related Methods Examples

example = 'hello world!'
result_1 = example.count('e') # is 1
result_2 = example.count('l') # (single lowercase L) is 3
result_3 = example.count('ll') # (double lowercase L) is 1
print('result_1:', result_1)
print('result_2:', result_2)
print('result_3:', result_3)
print('-'*64)

result_4 = example.find('d') # is 10 … found at index 10
result_5 = example.find('z') # is -1 … not found
result_6 = example.find('or') # is 7 … ‘or’ begins at index 7
print('result_4:', result_4)
print('result_5:', result_5)
print('result_6:', result_6)
print('-'*64)

result_7 = example.index('d') # is 10 … found at index 10
print('result_7:', result_7)
result_8 = example.index('or') # is 7 … ‘or’ begins at index 7
print('result_8:', result_8)
result_9 = example.index('z') # is an error
print('result_9:', result_9)
print('-'*64)

```

    result_1: 1
    result_2: 3
    result_3: 1
    ----------------------------------------------------------------
    result_4: 10
    result_5: -1
    result_6: 7
    ----------------------------------------------------------------
    result_7: 10
    result_8: 7



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-11-3bf5d49914e1> in <module>
         22 result_8 = example.index('or') # is 7 … ‘or’ begins at index 7
         23 print('result_8:', result_8)
    ---> 24 result_9 = example.index('z') # is an error
         25 print('result_9:', result_9)
         26 print('-'*64)


    ValueError: substring not found


### String Status Methods

These methods will all either return ```True``` or ```False```.

__```string_data.isalnum()```__
- Checks iff alpha+numeric, no spaces or no special characters

__```string_data.isalpha()```__
- Checks iff alpha, no spaces, no numbers or no special characters

__```string_data.islower()```__
- Checks iff all characters are lowercased, doesn’t check whitespaces

__```string_data.isupper()```__
- Check iff all characters are uppercased, doesn’t check whitespaces

__```string_data.isdigit()```__
- Checks iff numeric, no spaces or no special characters, ignores unicode majority of the time, this is preferred over ```.isnumeric()``` and ```.isdecimal()```


```python
# String Status Methods Example

example1 = 'abc123'
example2 = '123'
example3 = 'HELLO'

print('example1.isalnum():', example1.isalnum()) # outputs True
print('example1.isalpha():', example1.isalpha()) # outputs False

print('example3.islower():', example3.islower()) # outputs False
print('example3.isupper():', example3.isupper()) # outputs True

print('example2.isdigit():', example2.isdigit()) # outputs True
print('example1.isdigit():', example1.isdigit()) # outputs False
```

    example1.isalnum(): True
    example1.isalpha(): False
    example3.islower(): False
    example3.isupper(): True
    example2.isdigit(): True
    example1.isdigit(): False


### String Editing Methods

These methods will return a new string

__```string_data.capitalize()```__
- Capitalizes the first letter of a string

__```string_data.lower()```__
- Returns with all characters in the string lowercased

__```string_data.upper()```__
- Returns with all characters in the string uppercased


```python
# Editing Strings Example
# string variables must be updated with new values if you want to modify it

example = 'hello, world!'
example = example.capitalize() # example : ‘Hello, world!’
print('example:', example)

example = example.upper() # example : ‘HELLO, WORLD!’
print('example:', example)

example = example.lower() # example : ‘hello, world!’
print('example:', example)
```

    example: Hello, world!
    example: HELLO, WORLD!
    example: hello, world!

