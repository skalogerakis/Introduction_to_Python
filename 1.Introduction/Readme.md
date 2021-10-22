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

# Functions

## Definition

Functions are a way to divide your code into useful blocks, make it more readable and reuse it. Keyword `def` introduces a function definition. It must be followed by the function name and the parenthesized list of formal parameters (which can be empty). The statements that form the body of the function start at the next line and must be indented.

Functions only run when they are called. To call a function, use its name followed by parentheses

```
def hello_world_fun():  # function definition
    print("This is a function that prints Hello World")


hello_world_fun()   # how to call the function
```

## Parameters and call arguments

Function parameters are defined inside the parentheses `()` following the function name. A parameter acts as a variable name for an argument passed to the function.

The terms parameter and argument refer to the same thing: information that is passed into a function. However, a parameter is the variable listed inside the parentheses in the function definition, while an argument is the value that is sent to the function when it is called.

By default, a function must be called with the correct number of arguments. If your function expects 2 arguments, you have to call it with 2 arguments:

```
def my_name(name, surname):   # function definition
    print(name+" "+surname)

my_name("Stefanos", "Kalogerakis")  # calling the function
```

## Return value

Functions may return a value to the caller, using the keyword `return` . You can use the returned value to assign it to a variable or just print it out. In fact, even functions without a return statement do return a value. This value is called `None` (it’s a built-in name). Writing the value `None` is normally suppressed by the interpreter, but if you really want to see it, you can use `print(name_func())`.

```
def sum_numbers(x,y):
    return x + y

sum_numbers(3,12)   # Function that returns the sum of two numbers
```

**Exercise: Write a function that returns a list of numbers of the Fibonacci sequence up to N**

## Default parameters

It is also possible to define functions with a variable number of arguments. There are three forms, which can be combined. The most useful form is to specify a default value for one or more arguments. This creates a function that can be called with fewer arguments than it is defined with. For example, the function above can be called in several ways

```
def multiply_by(a, b=2, c=1):
    return a * b + c
```

- giving only the mandatory argument a: multiply_by(3)

- giving one of the optional arguments: multiply_by(3, 47), or multiply_by(3, c=47)

- or even giving all arguments: multiply_by(3, 47, 0)

You can specify which argument you are providing in the function call, just like we did in the third case with c=47. If you do not specify that, values will be assigned according to their order. Do not put spaces around the = symbol in function calls and definitions.

## Keyword Arguments

We already hinted that functions can also be called using keyword arguments of the form kwarg=value. For instance, the function testShowOff(), which we defined for you, it can be called in any of the following ways

```
def testShowOff(var1,var2='init'):
    print(var1 + " "+ var2)


# Alternative ways to call the function
testShowOff('Var1')             # 1 positional argument
testShowOff(var1='Var1_1')        # 1 keyword argument
testShowOff(var1='Var1_2',var2='Var2_1')    # 2 keyword argument (This is how I prefer to do it)
testShowOff(var2='Var2_2',var1='Var1_3')
testShowOff('Var1_4', var2='Var2_3')             # 1 positional, 1 keyword argument
```


## Recursion

The word recursion comes from the Latin word recurrere, meaning to return, revert, or recur. In programming, recursion refers to a coding technique in which a function calls itself.

In most cases, recursion isn't necessary, but in some situations, self-referential definition is warranted. Walking through tree-like data structures would be a good example. Such structures are nested, and they readily fit a recursive definition. A non-recursive algorithm for the same task would be quite cumbersome.

Here's a simple example of a recursive function. It takes a number as an argument and prints the numbers from the specified argument down to zero. In the recursive call, the argument is one less than the current value of n, so each recursion moves closer to the base case (which is zero).

```
def countdown(n):
    print(n, end=' ')
    if n == 0:
        return             # Terminates recursion
    else:
        countdown(n - 1)   # Recursive call

countdown(4)

```

**Exercise: Create a function that calculates the factorial of a positive integer. (Factorial: For every number it calculates the product of this number n and the factorial of the previous number. Factorial of 0 and 1 is 1)**

# Classes and Objects

## Definition
Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Classes are essentially templates for creating your objects. Each class instance (object) can have attributes attached to it for maintaining its state. Functions of objects are called methods, and they can modify their state. Methods are defined by the object's class.

The generalized form of class definition looks like this:

```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```


Class definitions, like function definitions (`def` statements) must be executed before they have any effect.

The statements inside a class definition will usually be function definitions, but other statements are sometimes useful. The function definitions inside a class normally have a peculiar form of argument list — this is explained later.

Class objects support two kinds of operations: attribute references and instantiation. Attribute references will be discussed in the following sections. Class instantiation uses function notation. Just imagine that the class object is a parameterless function that returns a new instance of the class. For example:

```
class SomeClass:
    """A simple example class"""
    i = 12345

x = SomeClass()
```

`x = SomeClass()` creates a new instance of the class and assigns this object to the local variable x.

You can find out more about class definition syntax by reading this section of Python Documentation.


## Variable Access


You can use attribute references to access variables inside an object. Attribute references use the standard syntax for all attribute references in Python: `obj.name`. Valid attribute names are all the names that were in the class’s namespace when the class object was created. So, if the class definition looked like this:

```
class MyClass:
    year = 2021

    def say_hello(self):
        return 'hello world'


class_var = MyClass()   # MyClass new instance
    
class_var.year = 2030   # Change the variable value inside an object
```


then `MyClass.year` and `MyClass.say_hello` are valid attribute references returning an integer and a function object, respectively. Class attributes can be assigned to, so you can change the value of `MyClass.year` by assignment.

## The self parameter

It's time to explain the `self` parameter we saw in previous tasks. The first argument passed to a class method is `self`. This is nothing more than a convention: the name self has no special meaning to Python. It is advised to follow the convention, otherwise your code may be less readable to other Python programmers.

Python will use the self parameter to refer to the object that is created or modified.
Methods may call other methods by using method attributes of the self argument:

```
class Bag:
    def __init__(self):     # Init is explained later on
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)  # Calling the method `add` from another method
        self.add(x)

```

## Special __init__ method

The instantiation operation (“calling” a class object) creates an empty object, but it is useful to create objects with instances customized to a specific initial state. Therefore, a class may define a special method named `__init__()`, like this:

```
class MyClass:
    def __init__(self):
        self.data = []

```

`__init__` is one of the reserved methods in Python. If defined, the `__init__()` method is invoked automatically when an instance of the class is created, and it initializes the object and its attributes. It always takes at least one argument, self. So in our example, a new, initialized instance can be obtained by:

x = MyClass()
The __init__() method may receive arguments for greater flexibility. In that case, arguments given to the class instantiation operator are passed on to __init__(). For example:

```
class Complex:
    def __init__(self, real_part, imag_part):
        self.r = real_part
        self.i = imag_part
        self.num = complex(self.r, self.i)

x = Complex(3.0, -4.5)  # Instantiating a complex number
x.num   # Result(3-4.5j)
```

## __str__ vs __repr__ methods

Both `str()` and `repr()` methods in Python are used for string representation of an object, but there are some differences. For example:

```
s = 'Hello World'
print (str(s))  # Output: Hello World
print(repr(s))  # Output: 'Hello World'

```

You can see that if we print a string using the `repr()` function, then it prints with a pair of quotes. `str()` is used for creating output for the user, while `repr()` is normally used for debugging and development. `repr()` needs to be unambiguous, and `str()` — to be readable.

Much like `__init__`, the methods `__repr__` and `__str__` are reserved in Python. The `print()` statement and the `str()` built-in function use the `__str__` method defined in the object's class to display its string representation. The repr() built-in function uses the __repr__ method defined in the object's class.

Our own defined class should therefore have a `__repr__` if we need detailed information for debugging. Also, if we think it would be useful to have a string representation for users, we should create a `__str__` function. Check out another implementation of the class Complex in the code editor. Run the code to see what each of the two print statements prints.

```
class Complex:
    def __init__(self, real_part, imag_part):
        self.real = real_part
        self.img = imag_part

    def __repr__(self):
        return f'Complex(10, 20)'

    def __str__(self):
        return f'{self.real} + i{self.img}'


x = Complex(2, 5)
print(str(x))
print(repr(x))

```

## Class and Instance Variables

In general, instance variables are for data unique to each instance, and class variables are for attributes and methods shared by all instances of the class:

```
class Cat:

    species = "Felis catus"  
    
    def __init__(self, breed, name):
        self.breed = breed  
        self.name = name

cleo = Cat('mix', 'Cleo')
furry = Cat('bengal', 'Furry')

print(cleo.name)    # Output: Cleo
print(cleo.species) # Output: Felis catus
print(furry.name)   # Output: Furry
print(furry.species) # Output: Felis catus
```

You can see that `species` is a class variable shared by all instances, while `name` and `breed` are instance variable unique to each instance.

Shared data can have possibly surprising effects when involving mutable objects, such as lists and dictionaries. If a class variable is a list and you modify it for one object, it will be changed for all objects of the class (check out the example in the code editor. If you intend using a list to keep track of features unique to each instance, you need to make it an instance attribute.


# Modules and packages

## Import module
As your program gets longer, you may want to split it into several files for easier maintenance. You may also want to use a handy function that you’ve written in several programs without copying its definition into each of them.

Modules in Python are simply Python files with the `.py` extension containing Python definitions and statements. Modules are imported from other modules using the `import` keyword and the file name without the extension `.py`.

Let's say you wrote a script called my_funcs.py with a bunch of functions (func1, func2, etc.). Now, if you want to use those in another script that is placed in the same directory, you can do import my_funcs. This does not import the names of the functions defined in my_funcs directly, but using the module name, you can now access the functions, for example:

```
my_funcs.func1()
```

Modules can import other modules. It is customary but not required to place all import statements at the beginning of a module.

## from import

One form of the import statement imports names `from` a module directly. This way, you can use the imported name without the module_name prefix. For example:

```
from calculator import Add

calc = Add()    # name `Calculator` used directly without prefix `calculator`
```

This does not introduce the name of the module from which the imports are taken in the local symbol table (so in our example, `calculator` is not defined).

There is even an option to import all names that a module defines:

```
from calculator import *
calc = Multiply()

```
This imports all names except those beginning with an underscore `_`. In most cases, Python programmers do not use this, since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

If the module name is followed by `as`, then the name following as is bound directly to the imported module:

```
import my_module as mm
mm.hello_world()
```

This is effectively importing the module in the same way that `import my_module` will do, with the only difference of it being available as `mm`.


# File input and output

## Open file

Python has a number of built-in functions to read and write information to a file on your computer.

`open()` returns a file object, and is most commonly used with two arguments: `open(filename, mode)`:

```
f = open('somefile.txt', 'w')
```

The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. It can be `'r'` if the file will only be read, `'w'` – for writing only (an already existing file with the same name will be erased), and `'a'` opens the file for appending – any data written to the file is added to its end. `'r+'` opens the file for both reading and writing. The mode argument is optional; `'r'` will be assumed if it’s omitted.

It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the file is properly closed after the code suite finishes.

```
with open('somefile.txt') as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed

```

**Important:** If you’re not using the `with` keyword, then you should call `f.close()` to close the file and free up any system resources used by it. You cannot use the file object after it is closed, whether by a `with` statement or by calling `f.close()`.


```
with open('input1.txt', 'r') as file:
    print(file.read())


outfile = open('outfile.txt', 'w') # opening the file in write mode (using `w` argument)
outfile.write('Hello World')  # writing to the file, the write() method is explained later.
outfile.close()


```


# Read file

To read a file’s contents, you can call `f.read(size)`, which reads some quantity of data and returns it as a string. When size is omitted or negative, the entire contents of the file will be read and returned.

```
with open('somefile.txt') as f:
    print(f.read())

Here's everything that's in the file.\n         # Output supposing that the file has one line as context

```

**Note:** there will be a problem if the file is twice as large as your machine’s memory.

`f.readline()` reads a single line from the file; a newline character (`\n`) is left at the end of the string and is only omitted on the last line of the file if the file doesn’t end in a newline. If `f.readline()` returns an empty string, the end of the file has been reached, while a blank line is represented by \n, a string containing only a single newline.

```
f.readline()
'This is the first line of the file.\n'
f.readline()
'Second line of the file\n'
f.readline()
''
```

For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and makes the code simple:

```
for line in f:
    print(line)
This is the first line of the file.
Second line of the file
```

If you want to read all the lines of a file in a list, you can also use `list(f)` or `f.readlines()`.

## Write to file

As we already mentioned, if you use `'w'` as the second argument in `open()`, the file opens for writing only. A new empty file will be created. If another file with the same name already exists, it will be erased. If you want to add some content to an existing file, you should use the `'a'` (append) modifier.

Another file object method, `f.write(string)`, writes the contents of a string to the file, returning the number of characters written.

```
f.write('This is a test\n')
15
```

Other types of objects in text mode need to be converted into a string first:

```
value = ('the answer', 42)
s = str(value)  # convert the tuple into string
f.write(s)
18
```
Where the specified text will be inserted in the file depends on the file mode (`'a'` vs `'w'`).

`'a'`: the text will be inserted at the end of the file.

`'w'`: the file will be emptied before the text will be inserted at the beginning.

If you want to include a symbol such as a line break, into your string (to start from a new line), add it with a +:

```
f.write('\n' + 'string,' + ' ' + 'another string')
```

This will add a new line and write 'string, another string'.

_Sources: PyCharm Edu, Stanford Course: Introduction to Python_