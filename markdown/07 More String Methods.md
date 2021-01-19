# More String Methods
---

The string data type has a lot of useful built-in methods that can help us solve more complex problems.

### Removing Leading and/or Trailing Spaces

These methods do not remove spaces within the text.

__```string_data.strip()```__
- Returns a string that loses all leading and trailing white spaces

__```string_data.lstrip()```__
- Returns a string that loses all leading white spaces

__```string_data.rstrip()```__
- Returns a string that loses all trailing white spaces


```python
# Strip() Examples

word1 = '   h ello   '
# 3 spaces then h ello then 3 spaces
print('word1.lstrip():', word1.lstrip(), 'world.') 
print('word1.rstrip():', word1.rstrip(), 'world.')
print('word1.strip():', word1.strip(), 'world.')
```

    word1.lstrip(): h ello    world.
    word1.rstrip():    h ello world.
    word1.strip(): h ello world.


### Using ```replace()```

__```replace()```__ is a powerful function helps us modify a string by targeting a pattern.

__```string_data.replace(old_str, new_str, limit)```__
- Returns a new string that replaces all instances of the ```old_str``` with the ```new_str```
- Limit (optional argument) doesn’t have to be set, if it is set, it will only apply the replace method based on the limit
- Therefore, this method can either use either 2 or 3 arguments


```python
# Using replace() examples

word = 'Hello World'
test1 = word.replace('l', 'L')
print('test1:', test1)

test2 = word.replace('l', 'o', 2)
print('test2:', test2)

test3 = word.replace('Hello','Goodbye')
print('test3:', test3)

test4 = word.replace(' ', '')
print('test4:', test4)
```

    test1: HeLLo WorLd
    test2: Heooo World
    test3: Goodbye World
    test4: HelloWorld


### Using ```startswith()``` and ```endswith()```

String methods that can check the start or the end of a string.

__```string_data.startswith('pattern', start_index, end_index)```__
__```string_data.endswith('pattern', start_index, end_index)```__
- Both of these methods return either True/False
- It looks for the string __pattern__ argument either at the start or the end.
- The indexes of start and/or end are both optional
    - they are integer based arguments



```python
# startswith() & endswith() examples

word = 'Hello World'

print("word.startswith('Hell'):", word.startswith('Hell')) # True
print("word.endswith('rld'):", word.endswith('rld')) # True

print("word.endswith('!'):", word.endswith('!')) # False
print("word.startswith('h'):", word.startswith('h')) # False

print("word.startswith(' ',5):", word.startswith(' ',5)) # True
print("word.endswith('or', 2, 9):", word.endswith('or', 2, 9)) # True because word[2:9] → ‘llo wor’
```

    word.startswith('Hell'): True
    word.endswith('rld'): True
    word.endswith('!'): False
    word.startswith('h'): False
    word.startswith(' ',5): True
    word.endswith('or', 2, 9): True


### Items in a Sequence to String

__```str_data.join(iterable_data)```__
- the ```join()``` method returns a new string that combines all items in the ```sequence/iterable_data``` separated by the ```str_data``` provided
- Each item in the sequence/iterable data must be a string type


```python
# .join() example

new_str = ', '.join(['1', '2', '3']) # new_str is: “1, 2, 3”
new_str2 = ' '.join('helloworld') # new_str2: “h e l l o w o r l d”

print(new_str)
print(new_str2)
```

    1, 2, 3
    h e l l o w o r l d


### String to a List

There are many ways to convert a string data into a list.

```list()``` function
- This function allows to convert a string to a list
- Each individual characters will be separated as a single item in the list

```sorted()``` function
- This function will sort the given string in ASCII order
- The function will return a __list__
- Each individual character in the string will be an item in the list

__Controlled Way to convert a string to a list: ```split()```__

__```str_data.split('pattern', numberOfTime)```__

- The ```split()``` method separates a string into a list
- Both arguments are optional, and when they are not specified: they will separate by spaces
    - ```pattern``` : this looks for a pattern to separate each items by
    - ```numberOfTime``` : this integer sets how many times to separate the string


```python
# String to a List examples

phrase1 = 'Hello World!'
print(list(phrase1))

phrase2 = 'Mr. Park'
print(sorted(phrase2))
print('-'*64)

# Using .split()
result1 = 'hello world'.split()
print('result1:', result1)

result2 = 'a,b,c,d,e'.split(',')
print('result2:', result2)

result3 = '1$2$3$4$5'.split('$',2)
print('result3:', result3)
```

    ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']
    [' ', '.', 'M', 'P', 'a', 'k', 'r', 'r']
    ----------------------------------------------------------------
    result1: ['hello', 'world']
    result2: ['a', 'b', 'c', 'd', 'e']
    result3: ['1', '2', '3$4$5']

