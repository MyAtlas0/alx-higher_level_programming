				# 0x0A-python-inheritance README File



Last Updated: 06/02/2024;
Contributor(s): MyAtlas0;



TASKS:

0. Lookup

#mandatory
Write a function that returns the list of available attributes and methods of an object:

Prototype: def lookup(obj):
Returns a list object
You are not allowed to import any module

# Filename: 0-lookup.py



1. My list

#mandatory
Write a class MyList that inherits from list:

Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module

# Filename: 1-my_list.py, tests/1-my_list.txt



2. Exact same object

#mandatory
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module

# Filename: 2-is_same_class.py



3. Same class or inherit from

#mandatory
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

Prototype: def is_kind_of_class(obj, a_class):
You are not allowed to import any module

# Filename: 3-is_kind_of_class.py



4. Only sub class of

#mandatory
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

Prototype: def inherits_from(obj, a_class):
You are not allowed to import any module

# Filename: 4-inherits_from.py



5. Geometry module

#mandatory
Write an empty class BaseGeometry.

You are not allowed to import any module

# Filename: 5-base_geometry.py



6. Improve Geometry

#mandatory
Write a class BaseGeometry (based on 5-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module

# Filename: 6-base_geometry.py



7. Integer validator

#mandatory
Write a class BaseGeometry (based on 6-base_geometry.py).

Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module

# Filename: 7-base_geometry.py, tests/7-base_geometry.txt



8. Rectangle

#mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

Instantiation with width and height: def __init__(self, width, height):
width and height must be private. No getter or setter
width and height must be positive integers, validated by integer_validator

# Filename: 8-rectangle.py



9. Full rectangle

#mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>

# Filename: 9-rectangle.py



10. Square #1

#mandatory
Write a class Square that inherits from Rectangle (9-rectangle.py):

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented

# Filename: 10-square.py



11. Square #2

#mandatory
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

Instantiation with size: def __init__(self, size)::
size must be private. No getter or setter
size must be a positive integer, validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the square description: [Square] <width>/<height>

# Filename: 11-square.py



12. My integer

#advanced
Write a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module

# Filename: 100-my_int.py



13. Can I?

#advanced
Write a function that adds a new attribute to an object if it’s possible:

Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
You are not allowed to use try/except
You are not allowed to import any module

# Filename: 101-add_attribute.py
