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

