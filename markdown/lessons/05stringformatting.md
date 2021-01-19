---
title: ""
draft: false
weight:
lesson: true
descriptor: ""
---

# String Formatting
---

String formatting is controlling the output of a given string especially when using the ```print()``` function. For some reason, this is a topic that is debated quite often as there are _multiple ways to do string formatting_.

Consider reading __[Google's Style Guide for Strings](https://google.github.io/styleguide/pyguide.html#s3.10-strings)__ when you are using strings.

### Escape Characters

Certain characters are not allowed to be inserted into a string so we must use __Escape Characters__ to insert them. Escape Characters are started with a backslash ```\``` then some characters.

``` 
Escape Characters:
\` = Single Quote
\\ = Backslash	
\n = New Line	
\r = Carriage Return	
\t = Tab	
\b = Backspace	
\f = Form Feed	
\ooo = Octal value	
\xhh = Hex value
```

__Example:__


```python
# Escape Characters

print('\'Hello\nWorld!\'')
```

    'Hello
    World!'


### Raw String

Whenever you want the strings to ignore any special symbol's behaviour, we can use __raw strings__.

If you want to convert a string to a raw string, it requires the symbol ```r``` in front of the string. This will help you ignore formatting operators and [escape characters](https://www.w3schools.com/python/gloss_python_escape_characters.asp).

__Example:__


```python
# Raw String 

message1 = '\'Hello\nWorld!\''
message2 = r'\'Hello\nWorld!\''

print('message1:', message1)
print('message2:', message2)
```

    message1: 'Hello
    World!'
    message2: \'Hello\nWorld!\'


### Option 1: Using the Formatting Operator

```%``` operator is used to help format a string.

__Important Formatting Symbols:__
```
%c : character
%s : string (same as str())
%d : decimal; often used for integers
%f : floating point
%g : for all digits
```

When a string has these symbols within the string, it will look for values in order to place them into the string.

__Example:__


```python
# Using % operator for string formatting

name = 'Mr. Park'
age = 10000

message = 'My name is %s and I am %d years old.' % (name, age)
print(message)
print('-'*64)

# Working with Decimals:
pi = 3.14159
print('Examine the following outputs for decimal values.')
print(r"-- print('%.2f' % pi) >>", '%.2f' % pi) #outputs 3.14
print(r"-- print('%g' % pi) >>", '%g' % pi) #outputs 3.14159 (Supports up to 6 decimal, will round the last decimal)
print(r"-- print('%.3f' % pi) >>", '%.3f' % pi) #outputs 3.142
print(r"-- print('%.3g' % pi) >>", '%.3g' % pi) #outputs 3.14
```

    My name is Mr. Park and I am 10000 years old.
    ----------------------------------------------------------------
    Examine the following outputs for decimal values.
    -- print('%.2f' % pi) >> 3.14
    -- print('%g' % pi) >> 3.14159
    -- print('%.3f' % pi) >> 3.142
    -- print('%.3g' % pi) >> 3.14


### Option 2: Using the ```.format()``` method

Similar to ```%``` operator, there is a _method_ that helps with formatting as well.

__Example:__


```python
# Using .format()

print('This is the {}th lesson for strings.'.format(5))

example = "I am: {}."
print(example.format('Mr. Park'))
```

    This is the 5th lesson for strings.
    I am: Mr. Park.


There are two very important statements: ```{}``` and ```.format()```
- ```{}``` is a formatter that act as a placeholder for data
- ```.format()``` will target the formatter and supply the data for the placeholder

For more information and usage of ```.format()``` please check out the tutorial at __[Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)__
