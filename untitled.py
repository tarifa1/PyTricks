
# Why Python Is Great:
# In-place value swapping

# Let's say we want to swap
# the values of a and b...
a = 23
b = 42

# The "classic" way to do it
# with a temporary variable:
tmp = a
a = b
b = tmp

# Python also lets us
# use this short-hand:
a, b = b, a


# Python Riddle: 👻 it is a mystery
# What will this expression evaluate to?

>>> {True: 'yes', 1: 'no', 1.0: 'maybe'}

# "is" vs "=="

>>> a = [1, 2, 3]
>>> b = a

>>> a is b
True
>>> a == b
True

>>> c = list(a)

>>> a == c
True
>>> a is c
False

# • "is" expressions evaluate to True if two 
#   variables point to the same object

# • "==" evaluates to True if the objects 
#   referred to by the variables are equal

# Because Python has first-class functions they can
# be used to emulate switch/case statements

def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


>>> dispatch_if('mul', 2, 8)
16

>>> dispatch_dict('mul', 2, 8)
16

>>> dispatch_if('unknown', 2, 8)
None

>>> dispatch_dict('unknown', 2, 8)
None


# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
>>> from collections import namedtuple
>>> Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
>>> my_car = Car('red', 3812.4)
>>> my_car.color
'red'
>>> my_car.mileage
3812.4

# We get a nice string repr for free:
>>> my_car
Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
>>> my_car.color = 'blue'
AttributeError: "can't set attribute"


# The standard string repr for dicts is hard to read:
>>> my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
>>> my_mapping
{'b': 42, 'c': 12648430. 'a': 23}  # 😞

# The "json" module can do a much better job:
>>> import json
>>> print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
>>> json.dumps({all: 'yup'})
TypeError: keys must be a string

