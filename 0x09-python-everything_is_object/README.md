				#0x09-python-everything_is_object README File



Last Updated: 31/01/2024;
Contributor(s): MyAtlas0;



TASKS:

0. Who am I?

#mandatory
What function would you use to get the type of an object?

Write the name of the function in the file, without ().

# Filename: 0-answer.txt



1. Where are you?

#mandatory
How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

# Filename: 1-answer.txt



2. Right count

#mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 100

# Filename: 2-answer.txt



3. Right count =

#mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = 89

# Filename: 3-answer.txt




4. Right count =

#mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a

# Filename: 4-answer.txt



5. Right count =+

#mandatory
In the following code, do a and b point to the same object? Answer with Yes or No.

>>> a = 89
>>> b = a + 1

# Filename: 5-answer.txt



6. Is equal

#mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)

# Filename: 6-answer.txt



7. Is the same

#mandatory
What do these 3 lines print?

>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)

# Filename: 7-answer.txt



8. Is really equal

#mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)

# Filename: 8-answer.txt



9. Is really the same

#mandatory
What do these 3 lines print?

>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)

# Filename: 9-answer.txt



10. And with a list, is it equal

#mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)

# Filename: 10-answer.txt



11. And with a list, is it the same

#mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)

# Filename: 11-answer.txt



12. And with a list, is it really equal

#mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)

# Filename: 12-answer.txt



13. And with a list, is it really the same

#mandatory
What do these 3 lines print?

>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)

# Filename: 13-answer.txt



14. List append

#mandatory
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)

# Filename: 14-answer.txt



15. List add

#mandatory
What does this script print?

l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)

# Filename: 15-answer.txt



16. Integer incrementation

#mandatory
What does this script print?

def increment(n):
    n += 1

a = 1
increment(a)
print(a)

# Filename: 16-answer.txt



17. List incrementation

#mandatory
What does this script print?

def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)

# Filename: 17-answer.txt



18. List assignation

#mandatory
What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)

# Filename: 18-answer.txt



19. Copy a list object

#mandatory
Write a function def copy_list(l): that returns a copy of a list.

The input list can contain any type of objects
Your file should be maximum 3-line long (no documentation needed)
You are not allowed to import any module

# Filename: 19-copy_list.py



20. Tuple or not?

#mandatory
a = ()
Is a a tuple? Answer with Yes or No.

# Filename: 20-answer.txt



21. Tuple or not?

#mandatory
a = (1, 2)
Is a a tuple? Answer with Yes or No.

# Filename: 21-answer.txt



22. Tuple or not?

#mandatory
a = (1)
Is a a tuple? Answer with Yes or No.

# Filename: 22-answer.txt



23. Tuple or not?

#mandatory
a = (1, )
Is a a tuple? Answer with Yes or No.

# Filename: 23-answer.txt



24. Who I am?

#mandatory
What does this script print?

a = (1)
b = (1)
a is b

# Filename: 24-answer.txt



25. Tuple or not

#mandatory
What does this script print?

a = (1, 2)
b = (1, 2)
a is b

# Filename: 25-answer.txt



26. Empty is not empty

#mandatory
What does this script print?

a = ()
b = ()
a is b

# Filename: 26-answer.txt



27. Still the same?
mandatory
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

# Filename: 27-answer.txt



28. Same or not?

#mandatory
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
Will the last line of this script print 139926795932424? Answer with Yes or No.

# Filename: 28-answer.txt



29. #pythonic

#advanced
Write a function magic_string() that returns a string “BestSchool” n times the number of the iteration (see code):

Format: see example
Your file should be maximum 4-line long (no documentation needed)
You are not allowed to import any module

# Filename: 100-magic_string.py



30. Low memory cost

#advanced
Write a class LockedClass with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called first_name.

You are not allowed to import any module

# Filename: 101-locked_class.py



31. int 1/3

#advanced
julien@ubuntu:/python3$ cat int.py 
a = 1
b = 1
julien@ubuntu:/python3$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many int objects are created by the execution of the first line of the script? (103-line1.txt)
How many int objects are created by the execution of the second line of the script (103-line2.txt)

# Filename: 103-line1.txt, 103-line2.txt



32. int 2/3

#advanced
julien@ubuntu:/python3$ cat int.py 
a = 1024
b = 1024
del a
del b
c = 1024
julien@ubuntu:/python3$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration:

How many int objects are created by the execution of the first line of the script? (104-line1.txt)
How many int objects are created by the execution of the second line of the script (104-line2.txt)
After the execution of line 3, is the int object pointed by a deleted? Answer with Yes or No (104-line3.txt)
After the execution of line 4, is the int object pointed by b deleted? Answer with Yes or No (104-line4.txt)
How many int objects are created by the execution of the last line of the script (104-line5.txt)

# Filename: 104-line1.txt, 104-line2.txt, 104-line3.txt, 104-line4.txt, 104-line5.txt



33. int 3/3

#advanced
julien@twix:/tmp/so$ cat int.py 
print("I")
print("Love")
print("Python")
julien@ubuntu:/tmp/so$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration:

Before the execution of line 2 (print("Love")), how many int objects have been created and are still in memory? (105-line1.txt)
Why? (optional blog post :))

Hint: NSMALLPOSINTS, NSMALLNEGINTS

# Filename: 105-line1.txt




34. Clear strings

#advanced
guillaume@ubuntu:/python3$ cat string.py 
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
guillaume@ubuntu:/python3$ 
Assuming we are using a CPython implementation of Python3 with default options/configuration (For answers with numbers use integers, don’t spell out the word):

How many string objects are created by the execution of the first line of the script? (106-line1.txt)
How many string objects are created by the execution of the second line of the script (106-line2.txt)
After the execution of line 3, is the string object pointed by a deleted? Answer with Yes or No (106-line3.txt)
After the execution of line 4, is the string object pointed by b deleted? Answer with Yes or No (106-line4.txt)
How many string objects are created by the execution of the last line of the script (106-line5.txt)

# Filename: 106-line1.txt, 106-line2.txt, 106-line3.txt, 106-line4.txt, 106-line5.txt
