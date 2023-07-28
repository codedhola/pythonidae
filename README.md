# pythonidae

A simple python practising space

# DATATYPES

### Basic Python Datatypes

#### _int_

The basic datatype used in performing basic operation, =>

```py
# Arithmetic
  2 + 4 # the '+' used to perfom operation
  2 - 1
  10 + 3  # 13
  10 - 3  # 7
  10 * 3  # 30
  10 ** 3 # 1000
```

#### _float_

This is a number type also but with the decimal number

```py
  # Arithmetic
  20.34 + 2
  10 + 3  # 13
  10 - 3  # 7
  10 * 3  # 30
  10 ** 3 # 1000
  10 / 3  # 3.3333333333333335
  10 // 3 # 3 --> floor division - no decimals and returns an int
  10 % 3  # 1 --
```

bool

This is a truthy datatype that has either 'True' or 'False'

```py
 True
 False
```

str

The str is a a strings datatype, mostly used with the double or single quote ("", ''),

```py
  name = "samuel"

  '''
  This is a multi-line
  string type
  ''' #multi-line string

  f'Hello {name} this is a formated string, i hope you know that '
```

list

This datatype is used to hold a list of datatypes in sequence, and this starts count from 0

```py
  software_stacks = ["javascript", "python", "c++"]
```

tuple

set

dict

This is a tyoe of datatype that stores values in "key":"value" pairs

```py
  user_details = {
    "name": "coded hola",
    "stacks": ["python", "typescript"]
  }
```

### Classes --> Custom types

These are data types that we create

### Specialized data types

These are special package or modules that we can bring to python

## none

This datatype means nothing in python i.e absence of value

# FUNCTION

### Basic python function

They are ome basic python function utility that needs to be known

_type_

```py
  type(4)                  # int
  type(2.10)               # float
  type('Coded hola')       # str
  type(True)               # bool
  type([1, 3, "sam"])      # list
  type({"name": "john"})   # dict

```

_print_

```py
 print("Hello") # prints hello to the console
```

# VARIABLES

This is a way of storing information, we declare a variable and assign a datatype to it to hold the datatype for use in a later time (binding)
some important things to consider in naming a variable are

- start with lowercase or \_ (underscore)
- can be snake case i.e (\_)underscore in the middle)
- They are case sensitive
- Don't override python or module keywords
- store constants in UPPERCASE
- Don't create a variable with double \_\_(underscore). They are reserved words for that
-

```py
user_name = 'coded hola'
developer = True
NAME = 'samuel'

```
