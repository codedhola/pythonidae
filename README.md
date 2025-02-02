# pythonidae

A simple python practicing space

# DATATYPES

## Basic Python Datatypes

### _int_

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

### _float_

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

### _bool_

This is a truthy datatype that has either 'True' or 'False'

```py
 True
 False
```

### _str_

The str is a a strings datatype, mostly used with the double or single quote ("", ''),

```py
  name = "samuel"

  '''
  This is a multi-line
  string type
  ''' #multi-line string

  f'Hello {name} this is a formated string, i hope you know that '


  len('turtle') # 6

  # Basic Methods
  '  I am alone '.strip()               # 'I am alone' --> Strips all whitespace characters from both ends.
  'On an island'.strip('d')             # 'On an islan' --> # Strips all passed characters from both ends.
  'but life is good!'.split()           # ['but', 'life', 'is', 'good!']
  'Help me'.replace('me', 'you')        # 'Help you' --> Replaces first with second param
  'Need to make fire'.startswith('Need')# True
  'and cook rice'.endswith('rice')      # True
  'still there?'.upper()                # STILL THERE?
  'HELLO?!'.lower()                     # hello?!
  'ok, I am done.'.capitalize()         # 'Ok, I am done.'
  'oh hi there'.count('e')              # 2
  'bye bye'.index('e')                  # 2
  'oh hi there'.find('i')               # 4 --> returns the starting index position of the first occurrence
  'oh hi there'.find('a')               # -1
  'oh hi there'.index('a')              # Raises ValueError

  'I\'m thirsty'
  "I'm thirsty"
  "\n" # new line
  "\t" # adds a tab

  'Hey you!'[4] # y
  name = 'Coded Hola'
  name[4]     # d
  name[:]     # Coded Hola
  name[:1]    # C
  name[-1]    # a
  name[::1]   # Coded Hola
  name[::-1]  # aloh dedoc
  # : is called slicing and has the format [ start : end : step ]

  'Hi there ' + 'Timmy' # 'Hi there Timmy' --> This is called string concatenation
  '*'*10 # **********


```

### _list_

This datatype is used to hold a list of datatypes in sequence, and this starts count from 0

```py
  software_stacks = ["javascript", "python", "c++"]
```

# _tuple_

Tuple Like lists, but they are used for immutable thing (that don't change)
To declare a tuple we => `my_tuple = ('apple','grapes','mango', 'grapes')`

# _set_

Set is an unordered collection of unique objects. sets are created like object but only values are required
=> `my_set = { 1, 2, 3, 4, 5 }`

Note => They are no duplicates in set

dict

This is a tyoe of datatype that stores values in "key":"value" pairs

```py
  user_details = {
    "name": "coded hola",
    "stacks": ["python", "typescript"],
    "isDev": True
  }
```

### Classes --> Custom types

These are data types that we create

### Specialized data types

These are special package or modules that we can bring to python

## None

This datatype means nothing in python i.e absence of value

# BUILT-IN FUNCTIONS

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

# '_list_' methods

```py


  # Add to List
  my_list * 2                # [1, 2, '3', True, 1, 2, '3', True]
  my_list + [100]            # [1, 2, '3', True, 100] --> doesn't mutate original list, creates new one
  my_list.append(100)        # None --> Mutates original list to [1, 2, '3', True, 100]          # Or: <list> += [<el>]
  my_list.extend([100, 200]) # None --> Mutates original list to [1, 2, '3', True, 100, 200]
  my_list.insert(2, '!!!')   # None -->  [1, 2, '!!!', '3', True] - Inserts item at index and moves the rest to the right.

  ' '.join(['Hello','There'])# 'Hello There' --> Joins elements using string as separator.

```

```py
  # Copy a List
  basket = ['apples', 'pears', 'oranges']
  new_basket = basket.copy()
  new_basket2 = basket[:]

  # Remove from List
  [1,2,3].pop()    # 3 --> mutates original list, default index in the pop method is -1 (the last item)
  [1,2,3].pop(1)   # 2 --> mutates original list
  [1,2,3].remove(2)# None --> [1,3] Removes first occurrence of item or raises ValueError.
  [1,2,3].clear()  # None --> mutates original list and removes all items: []
  del [1,2,3][0]   # None --> removes item on index 0 or raises IndexError



```

```py
  [1,2,'b',4,5,6].index('b') # return ==> b which is the index
  ['a','b','c','d','e'].index('b', 0, 4) # return ==> b because b is present in the index between 0 to 4
  [1,2,'b',4,5,6].index('a') # return ==> An Error => Advisable to use a different method is not sure index is present

  # The 'in' method is considered safe in this context because it returns 'True' or 'false'
  'x' in ['a', 'b', 'c', 'd'] # returns False



  [1,2,5,3].sort()         # None --> Mutates list to [1, 2, 3, 5]
  [1,2,5,3].sort(reverse=True) # None --> Mutates list to [5, 3, 2, 1]
  [1,2,5,3].reverse()      # None --> Mutates list to [3, 5, 2, 1]
  sorted([1,2,5,3])        # [1, 2, 3, 5] --> new list created
  my_list = [(4,1),(2,4),(2,5),(1,6),(8,9)]
  sorted(my_list,key=lambda x: int(x[0])) # [(1, 6), (2, 4), (2, 5), (4, 1), (8, 9)] --> sort the list by 1st (0th index) value of the tuple
  list(reversed([1,2,5,3]))# [3, 5, 2, 1] --> reversed() returns an iterator

  my_list[::-1] # This reverse a list and also make a new copy(doesn't modify the old list)

  stacks = ['python', 'javscript', 'c++', 'go']
  " ".join(stacks)




```

# 'dict' methods

```py
  my_dict = {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False}
  my_dict['name']                      # Andrei Neagoie
  len(my_dict)                         # 3
  list(my_dict.keys())                 # ['name', 'age', 'magic_power']
  list(my_dict.values())               # ['Andrei Neagoie', 30, False]
  list(my_dict.items())                # [('name', 'Andrei Neagoie'), ('age', 30), ('magic_power', False)]
  my_dict['favourite_snack'] = 'Grapes'# {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes'}
  my_dict.get('age')                   # 30 --> Returns None if key does not exist.
  my_dict.get('ages', 0 )              # 0 --> Returns default (2nd param) if key is not found

  #Remove key
  del my_dict['name']
  my_dict.pop('name', None)

```

```py
  my_dict.update({'cool': True})  # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
  {**my_dict, **{'cool': True} }                                         # {'name': 'Andrei Neagoie', 'age': 30, 'magic_power': False, 'favourite_snack': 'Grapes', 'cool': True}
  new_dict = dict([['name','Andrei'],['age',32],['magic_power',False]])  # Creates a dict from collection of key-value pairs.
  new_dict = dict(zip(['name','age','magic_power'],['Andrei',32, False]))# Creates a dict from two collections.
  new_dict = my_dict.pop('favourite_snack')  # Removes item from dictionary.

  # Dictionary Comprehension
  {key: value for key, value in new_dict.items() if key == 'age' or key == 'name'} # {'name': 'Andrei', 'age': 32} --> Filter dict by keys
```

# 'tuples' methods

```py
  len(my_tuple)                          # 4
  my_tuple[2]                            # mango
  my_tuple[-1]                           # 'grapes'

  # Immutability
  my_tuple[1] = 'donuts'  # TypeError
  my_tuple.append('candy')# AttributeError

  # Methods
  my_tuple.index('grapes') # 1
  my_tuple.count('grapes') # 2


```

# 'sets' methods

```py
  new_set = {1, 2, 3, 4, 5, 6}

  my_set.remove(100)      # {1} --> Raises KeyError if element not found
  my_set.discard(100)     # {1} --> Doesn't raise an error if element not found
  my_set.clear()          # {}
  new_set = {1,2,3}.copy()# {1,2,3}

  # set method
  set1 = {1,2,3}
  set2 = {3,4,5}
  set3 = set1.union(set2)               # {1,2,3,4,5}
  set4 = set1.intersection(set2)        # {3}
  set5 = set1.difference(set2)          # {1, 2}
  set6 = set1.symmetric_difference(set2)# {1, 2, 4, 5}
  set1.issubset(set2)                   # False
  set1.issuperset(set2)                 # False
  set1.isdisjoint(set2)                 # False --> return True if two sets have a null intersection.

```

# Conditionals

Comparison Operators and Logical Operators

```py

==                   # equal values
!=                   # not equal
>                    # left operand is greater than right operand
<                    # left operand is less than right operand
>=                   # left operand is greater than or equal to right operand
<=                   # left operand is less than or equal to right operand
<element> is <element> # check if two operands refer to same object in memory
Logical Operators
1 < 2 and 4 > 1 # True
1 > 3 or 4 > 1  # True
1 is not 4      # True
not True        # False
1 not in [2,3,4]# True


if <condition that evaluates to boolean>:
  # perform action1
elif <condition that evaluates to boolean>:
  # perform action2
else:
  # perform action3

## TERNARY OPERATOR IN PYTHON
is_friend = True
can_message = "Message Allowed" if is_friend else "not allowed"

```

# Control flow

```py
  my_list = [1,2,3]
  my_tuple = (1,2,3)
  my_list2 = [(1,2), (3,4), (5,6)]
  my_dict = {'a': 1, 'b': 2. 'c': 3}

  for num in my_list:
      print(num) # 1, 2, 3

  for num in my_tuple:
      print(num) # 1, 2, 3

  for num in my_list2:
      print(num) # (1,2), (3,4), (5,6)

  for num in '123':
      print(num) # 1, 2, 3

  for idx,value in enumerate(my_list):
      print(idx) # get the index of the item
      print(value) # get the value

  for k,v in my_dict.items(): # Dictionary Unpacking
      print(k) # 'a', 'b', 'c'
      print(v) # 1, 2, 3

  while <condition that evaluates to boolean>:
    # action
    if <condition that evaluates to boolean>:
      break # break out of while loop
    if <condition that evaluates to boolean>:
      continue # continue to the next line in the block

    # WHILE LOOPS IS GREAT WHEN YOU DON'T KNOW WHEN THE TASK IS END
    # EXAMPLE
    # waiting until user quits
  msg = ''
  while msg != 'quit':
      msg = input("What should I do?")
      print(msg)


```

_Range_

```py
  for _ in range(0, 5):
    print(_)

  for _ in range(0, 10, 2):
    print(_)

  for _ in range(10, 1, -1):
    print(_)

```

_Enumerate_

This method returns both the index and the value counter of the item that is being looped through

```py
  for i, el in enumerate('helloo'):
  print(f'{i}, {el}')
  # 0, h
  # 1, e
  # 2, l
  # 3, l
  # 4, o
  # 5, o

```

# Functions

A function in python is defined using the '_def_' key word then naming the function.

```py
  def add(msg):
    return msg

  print(add("Hello functions")) # Hello functions

```
