## First program

Traditionally, the first program you write in any programming language is _``Hello World!``_. Introduce yourself to the world by printing this simple message


```
print("Hello, world! My name is Stefanos")
```

## Comments

 Comments in Python start with the hash character **(#)** and a single space and they extend to the end of the physical line. 

 - **Multi-Line Comments:** Python does not really have syntax for multiline comments. You can use the hash character though in concurrent lines
 - **Inline Comments**: Inline is considered a comment on the same line as a statement. Don't overdo it with inline comments. It is adviced to add at least two spaces in-between the inline comment and the statement 

 

_**NOTE:** It is always crucial to add (and update) comments to keep track of the changes and understand what is going on with the code. As the code grows larger are more and more important_


```

# This is the a simple comment
print("Hello World!")  # This inline comment for this line
	
print("# this is not a comment")
# This is a multiline comment
# This is a new multiline comment

```


## Variables

Variables store values that can be referenced later on the code. To assign a variable in python use the equals symbol **(=)**. It is also possible to assign a value into multiple variables by using the same symbol.



```

# Here is an example where the value "test" is assigned on var1 and var2 variables
var1 = var2 = "test"

# Print both variables
print("var1 = " + var1)
print("var2 = " + var2)

var1 = "Let's change"  # Assign new value to var1
print("New var1 = " + var1)

```

### Naming Conventions

- Variable names can contain (latin) letters, numbers and/or underscore character
- Variable names cannot start with a digit
- The so called _Reserved words or keywords_ cannot be used as variable name. Ex if, or, and etc

In case any of those requirements is not met then an error message will pop up

### Variable types


In many programming languages, variables are statically typed. That means a variable is initially declared to have a specific data type, and any value assigned to it during its lifetime must always have that type.

Variables in Python are not subject to this restriction. In Python, a variable may be assigned a value of one type and then later re-assigned a value of a different type:

The type of a variable determines the operations that it supports (e.g., “does it have a length?”) and defines the possible values for objects of that type. The **type()** function returns the type of the variable. 

```
number = 12
print(type(number))   # Print type of variable "number"

flaf = True
print(type(flag))

```
## TODO MAYBE ADD DATATYPES
In Python, there are two main types of numbers: integers and floats. The most important difference between them is that a float is a number that has a decimal point, and an int is a number without a decimal point.

### Type Casting

Python supports several built-in functions to let you convert one data type into another. These functions return a new object represented the converted value. `int(x)` converts x variable into an integer, `float(x)` converts x into a floating point number and so on. 

_NOTE: Be careful, casting is not always possible. Ex. Cannot convert a integer to a list_ 

```
float_number = 9.0
print(float_number)
print(type(float_number))

float_number = str(float_number)  # Cast to string and see the difference
print(float_number)
print(type(float_number))

```

# Arithmetic operators

Python include multiple operators that are used to conduct calculations

- (+) is the addtion operator
- (-) is the substraction operator
- (\*) is the multiplication operator
- (/) is the division operator
- (%) the modulo operator is the remainder of the division of the first argument by the second
- (//) is the floor of the division result between two numbers

As in math, different operators have different priority. You can read more regarding operator [here](https://docs.python.org/3/reference/expressions.html#binary-arithmetic-operations). As a rule of thumb, it is better to use parenthessis to have better control over the priority.

### Augmented Assignment

An augmented assignment is a single statement combining a binary operation and an assignment statement such as `+=, -=` etc. 

An augmented assignment like `x += 12` can be also written as `x = x + 12`

```
division = 4
print("Before Division ", str(division))

division /= 2
print("After Division with 2:", str(division))
```

### Boolean and comparison operators

Python has multiple types of comparison operators including:

- `<` less than
- `>` greater than
- `==` equal
- `!=` not equal
- `>=` greater or equal
- `<=` less or equal

All the above operators compare the values of two objects and can either return **True** or **False**


# Strings

## Concatenate Strings

In order to concatenate two strings the mathematical symbol `+` is used
```
var1 = "This is an"
var2 = "example"

var3 = var1 + " " + var2
print(var3)
```

## String multiplication

Python supports string-by number multiplication(but not the other way around). In the following example the word _"Example"_ will be repeated 3 times


```
example = "Example"
result = example * 3
print(result)   # Result -> ExampleExampleExample
```
 

## String Indexing

Strings can be interpreted as arrays and it is possible to access single characters by position. For example `str[index]` will yield the character at position index in the string str. Indices start from 0 and can also be negative numbers if required to start counting from the end of the string. In case the required index does not exist a `ValueError` pops up 

```
python = "Python"
print("First letter ", python[0])
print("Last letter ", python[-1])
```

## String Slicing

Slicing is used to extract substrings from a string. It works on a similar fashion as indexing but now instead of one index there are two indices colon seperated `str[ind1:ind2]`. 

```
str[start:end]  # items start through end - 1
str[start:]     # items start through the rest of the array
str[:end]       # items from the beginning through end-1
str[:]          # a copy of the whole array
```

## In operator

Checks whether a string contains a specific letter or a substring. Returns Boolean expression

```
test = "I like Python"
exists = "Python" in test

print(exists)
```

## String length

The `len()` method is used to count how many characters a string contains

**Exercise: Get the first half of a string**

## Escape Character

Backslash `(\)` is used to escape special symbols like single or double quotes. In order to literally use the backslash character use double backslash

Special symbols `'\n'` and `'\t'` are used to add a line break to a string and tabulation respectively

Quotes have special meanings and they can be escaped with a backslash too. If there is a need to print quotes inside a string, use different kind of quotes: single quotation marks may be used in a double-quoted string without escaping and vice versa. Also, it would be a good idea to pick youw favourite kind of quotes and use respectively

```
print("That's the sample we are \"looking for\"\n")
print("Escape the escape \\ character\t for now")
```

## Basic String Methods

Two very useful string methods are the lower() and upper(). The first one is responsible to convert all characters in a string to lowercase whereas the second converts all character to capitals

```
example = "My name is Stefanos"
print("To lowercase ", example.lower())
print("To uppercase ", example.upper())
```


## String formatting

The `%` operator after strings combines the string with variables. For example, the `%s` will be replaced with a string that comes after it. `%d` is a symbol used for integer values, and `%f` for floating point values

```
name="Stefanos"
age=24

print("My name is %s and I am %d years old" %  (name,age))
print("I am %d years old" % age)
```

## Formatted String literals

A formatted string literal (f-string) is a string literal taht is prefixed with `'f'` or `'F'`. These are expressions delimited by curly braces `{}`

The parts of the string outside curly braces are treated literally. Escape sequences are decoded like in ordinary string literals. Each expression is evaluated in the context where the formatted string literal appears, in order from left to right

```
name="Stefanos"
age=24

print(f"My name is {name} and I am {age} years old")
```

_NOTE: This format was introduced since Python 3.6 version_

# Data Structures

## List introduction

Python has a number of different data types used to group data together. The most verstile is the list, that can be written as a series of comma seperated values enclosed in square brackets

Operations like concatenation and slice are supported here

```

list = [1,3,4,5,2]
print(list)     # Print the desired list
list += [99,77]
print(list)     # Print the concatenated list

```

## List Operations

Lists are **mutable**(it is possible to change their content) using `lst[index] = diff_itme`. It is also possible to add extra items at the end of the list by using the append method or list concatenation

```

list = [1,2,3,4,5]
print("Initial list ",list)

list[0] = 99
print("Replaced the first element ", list)

list.append(-1)
print("Added extra element ", list)

```

## Tuples

Tuples represent another standard sequence data type. They are almost identical to lists. The only significant difference is that tuples are **immutable**(cannot add, replace or delete elements) in a tuple. Tuples are formatted by comma seperated elements enclosed in parentheses `Ex. (var, var2, var3)`

Special cases:
-  Create an empty tuple with just an empty pair of parenthessis `()`
- Create a tuple with one item by defining the value followed by a comma `Ex. tuple = ('val',)`

## Join() method
The method `.join()` is a string method and is used to create a string from iterable objects. It joins each element of an iterable (such as list, string or tuple) by a string seperator and returns a concatenated string. A `TypeError` will be raised if there are any non string values in the iterable.

The syntax of the `join()` method looks as follows:

string.join(iterable_string)

```
string_sample = 'abcde'
tuple_sample = ('this', 'is', 'an', 'example')
list_sample = ['Nice', 'friend']

print(' + '.join(string_sample))    # Join with the + sign
print(' + '.join(tuple_sample))    # Join with the = sign
print(' try my '.join(list_sample))
```

## Dictionaries

Dictonaries are similar to lists except that in order to access their values, keys are used instead of indices. A key can be any immutable type. Strings and numbers can always be keys; tuples can be used as keys if they contain only immutable objects. Lists cannot be used as keys.

Dictionaries are sets of `key: value` pairs, with the requirement that the keys are unique within one dictionary. Dictionaries are enclosed withing curly brackets `dct = {'key1':'value1', 'key2':'value2'}`. Dictionaries can also be created with the dict constructor ex. `a = dict('one':1, 'two':2)`  

```
phone_book = {'John':123, 'Jane':456, 'Jarvis':654}
print(phone_book)

phone_book['Phil'] = 2310   # Add a new item to the dict
print(phone_book)

del phone_book["John"]      # Delete a specific key-value pair
print(phone_book)

```

## Dictionaries Keys() and values()

There are many useful methods in dictionaries such as `keys()`,`values()`, and `items()`

- `keys()` -> returns a view object that a list of all the keys in the dictonary in order of insertion.
- `values()` -> returns a new view of the dictionary's values
- `items()` -> returns dictionary items as tuples in a list (in (key,value pairs))

The objects returned by dict.keys(), dict.values() and dict.items() provide a dynamic view on the dictionary's entries, which means that when changes apply to the dictionary the view reflects thoses changes 

```
phone_book = {'John':123, 'Jane':456, 'Jarvis':654}
print(phone_book)

print("Keys ",phone_book.keys())
print("Values ",phone_book.values())

```

## In keyword

The in keyword is used to check if a list or a dictionary contains a specific item (the same way it worked with strings)

```
random_list = ['Ofi', 'Olympiakos', 'Panathinaikos']
print("Ofi" in random_list)

random_dict = {'Ofi':13, 'Aris':2}
print("Aris" in random_dict)
```


# Boolean operators

Boolean operators compare statement and return results in boolean values. The boolean operator `and` returns `True` when the expression on both sides of `and` are `True`. The boolean operator `or` returns `True` when at least one expression on either side of `or` is `True`. The boolean operator `not` inverts the boolean expression it precedes

```
name = "Stefanos"
age = 24

print(name == "Nikos" or age == 24)  
print(name == "Stefanos" and age == 24)
```

Boolean operators are not evaluated from left to right. There's an order of operations for boolean operators: `not` is evaluated first, `and` is evaluated next and `or` is evaluated last. In general, it is much better though to use parenthesis to define the order operatrion much clearer 

```
name = "Stefanos"
age = 24

print(name == "Nikos" or not age == 24)  

# Check if name is Antonis or it's not true 
# that name equals Stefanos and he is 24 years old at the same time 

print(name == "Antonis" or not name == "Stefanos" and age == 24)

# Or what is better in my opinion
print((name == "Antonis") or (not name == "Stefanos" and age == 24))
```


## If statement

Compound statements in Python contain (groups of) other statements; they affect or control the execution of those statements in some way. 

Perhaps the most well known statement is the `if` statement. The `if` keyword is used to form a conditional statement that executes some specified code after checking if its expression is True. Python uses indentation to define code blocks

```

if value > 10:
    print("Value above 10")             # Indented block
    print("Another value above 10")     # Indented block

print("Outside the block!")

```

A code block starts with indentation and ends with the first unindented line. The amount of indentation must be consistent throughout the block. Generally, four whitespaces or single tabs are used for indentation. Incorrect indentation will result in IndentationError.

If you have only one statement to execute, you can put it on the same line as the if statement.

```
if value > 10: print("Value above 10")
```

## Else and elif statements

The `elif` and `else` statements complement the if statement. There can be zero or more elif parts, and the else part is optional. The keyword elif is short for ‘else if’, and is useful to avoid excessive indentation.

In conditional execution, only one of the suites is selected by evaluating the expressions one by one until one is found to be `True`. Then that suite is executed and no other part of the if statement is evaluated. If all expressions are false, the suite of the else clause, if present, is executed.

```
a = 2
b = 33
if b > a:
  print("b is greater than a")  # That's the result
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

```


## for loop

The `for` statement is used to iterate over the elements of a sequence (such as a string, tuple, or list) or another iterable object. The sequence is evaluated once. On each iteration, the variable defined in the for loop will be assigned to the next value in the list. The code following the line with the for statement is executed once for each item. When the items are exhausted, the loop terminates.

You can read more about the for statement [on this page](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement
) of Python Documentation.

```
for i in range(3):      # Prints numbers from 0-4
    print(i)

primes = [2, 3, 5, 7]

for prime in range(len(primes)):
    print(prime)

```

**Exercise: Use a loop to count how many characters a string contains**

## While loop

A while loop is somewhat similar to an if statement: it executes some code if some condition is True. The key difference is that it will continue to execute indented code for as long as the condition is True. If the expression is False, the loop terminates.

```

i = 0
while i<4:      # Prints numbers from 0-4
    print(i)
    i+=1

primes = [2, 3, 5, 7]

curr = 0
while curr < len(primes):
    print(primes[curr])
    curr+=1

```

## Break keyword

The `break` keyword is used to escape from a loop

```

# This loop will print until i reaches 5 and exits
for i in range(10):
    print(i)
    if i == 5:
        break

```

## Continue keyword

The continue keyword is used to skip the rest of the code inside the loop for the current iteration only and proceed right to the next one. The loop continues to the next iteration

```

# This loop will print every value from 0 to 10 except 3
for i in range(10):
    if i == 3:
        continue
    print(i)
```

Exercise: Print only the odd numbers from 1 to 100

_Sources: PyCharm Edu, Stanford Course: Introduction to Python_