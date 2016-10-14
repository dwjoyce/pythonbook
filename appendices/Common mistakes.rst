:orphan:

Common mistakes
===============

.. quote::
    :author: Paul R. Ehrlich

    To err is human, but to really foul things up you need a computer.

Forgetting to open / close quotation marks
------------------------------------------

Do not forget to close your quoted strings with a quotation mark at both the beginning and end.  Moreover, you must be consistent, so if you start with a single or double quotation mark, then you must finish with the same type of quotation mark.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print("Hello, World!)              |     print("Hello, World!")             |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print(Hello!')                     |     print('Hello!')                    |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print('Your name is, name)         |     print('Your name is', name)        |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print('Name', name, 'age, age)     |     print('Name', name, 'age', age)    |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Using quotation marks insides quotes
------------------------------------

If you include a quotation mark inside a string, then you must use the escape sequence ``\'`` or ``\"``, otherwise Python will assume you have closed off the string, thus leaving the remaining text outside the quotation marks.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print('St. Michael's School')      |     print('St. Michael\'s School')     |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print("His name was "fred"")       |     print("His name was \"fred\"")     |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Not using commas between items
------------------------------

You must use a ``,`` comma between each item, whether you are printing, defining a list or defining more than one variable from a sequence of values.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print('Hello your name is' name)   |     print('Hello your name is', name)  |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print(10 20 30 40)                 |     print(10, 20, 30, 40)              |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     months = ['jan' 'feb' 'mar']       |     months = ['jan', 'feb', 'mar']     |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     num1 num2 = 10 20                  |     num1, num2 = 10, 20                |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     num1 num2 = num2 num1              |     num1, num2 = num2, num1            |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Spelling or capitalisation mistakes
-----------------------------------

You must be consistent in using the names that have been defined, including the way the names are spelt and capitalised.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     pront(10 + 20)                     |      print(10 + 20)                    |
|     Print(10 + 20)                     |      print(10 + 20)                    |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     number = 10                        |      number = 10                       |
|     print(numbre)                      |      print(number)                     |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     turtle.pencolour("red")            |      turtle.pencolor("red")            |
|     turtle.beginfill()                 |      turtle.begin_fill()               |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     s = 'good morning'                 |      s = 'good morning'                |
|     print(s.titel())                   |      print(s.title())                  |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Using variables before defining them
------------------------------------

Before making use of a variable, you must define it to some value.  Use the value ``None`` if you do no know what this value is going to be in advance (or ``''`` for an empty string, or ``[]`` for an empty list).

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     num1 = 10                          |     num1, num2 = 10, 20                |
|     print(num1, num2)                  |     print(num1, num2)                  |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     while count < 10:                  |     count = 0                          |
|         print(count)                   |     while count < 10:                  |
|         count = count + 1              |         print(count)                   |
|                                        |         count = count + 1              |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Using invalid variable names
----------------------------

Variable names must begin with either an upper or lowercase letter, or an underscore ``_`` character.  Do not include symbols in your names.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     100_num = 100                      |     num_100 = 100                      |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     a$ = 10                            |     a = 10                             |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     first number = 123                 |     first_number = 123                 |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Setting variables
-----------------

Variables are defined by placing the variable name on the left, with an assignment operator in the middle, followed by the expression to store on the right.  If you are defining two variables at the same time (in the second example below), then you must use the assignment operator between each of them so that they are assigned to the same value.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     101 = number                       |     number = 101                       |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     num1, num2 = 5                     |     num1 = num2 = 5                    |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Using modules before importing them
-----------------------------------

Before you can use anything defined inside another module, you must import it first.  This includes even listing its contents by using the ``dir`` function.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     num = random.randint(1, 100)       |     import random                      |
|                                        |     num = random.randint(1, 100)       |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Another common mistake is to save your program with the same name as a module you are importing, so it will import your own program instead.  For example, if you are using the ``random`` module, then do not call your program ``random.py``, or if you are using the ``turtle`` module then do not call your program ``turtle.py``.

Not converting to integers when performing arithmetic
-----------------------------------------------------

Strings must be converted into numbers, whether integers or floats, before they are used in arithmetic calculations.  Use the ``int``, ``float`` and ``str`` functions to convert between these types of data.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     age = input('Age? ')               |     age = input('Age? ')               |
|     print(age + 10)                    |     print(int(age) + 10)               |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Forgetting the colon ``:`` at the end of compound statements
------------------------------------------------------------

Any compound statement, whether an ``if``, ``while``, ``for``, ``def`` or ``try``, must have a colon ``:`` symbol at the end of the line to indicate that the code block that follows belongs to it.  For example, if an ``if`` statement is used, then the code block is only executed if the condition following the ``if`` keyword evaluates to ``True``.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     if num > 10                        |     if num > 10:                       |
|         print(num)                     |         print(num)                     |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     for num in range(10)               |     for num in range(10):              |
|         print(num)                     |         print(num)                     |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     while num < 10                     |     while num < 10:                    |
|         print(num)                     |         print(num)                     |
|         num = num + 1                  |         num = num + 1                  |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     def say_hello()                    |     def say_hello():                   |
|         print("Hello!")                |         print("Hello!")                |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Using the assignment operator instead of comparison operator
------------------------------------------------------------

When comparing values, you must use one of the :term:`comparison operators`.  The :term:`assignment operator` ``=`` is used to define variables.  The equals operator ``==`` is used to compare an expression on the left with an expression on the right, resulting in a boolean ``True`` or ``False`` result.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     if num = 10:                       |     if num == 10:                      |
|         print(num)                     |         print(num)                     |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Not forming expressions properly
--------------------------------

The expressions below on the left (taking the first example) were intended to compare the variable ``ch`` against either ``'A'`` or ``'B'``, and execute the subsequent code block if this is the case.  Unfortunately, it only compares ``ch`` against ``'A'``, and then checks whether the letter ``'B'`` is not empty (which it isn't).  It is equivalent to ``(ch == 'A') or ('B')``, with each side of the expression being evaluated separately, and then combined together with the ``or`` operator.  This means that the code block will always execute, as this expression is always ``True``.  To compare a variable against two separate values, you need to do both comparisons individually, such as on the right of the table.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |     :pythontest: off                   |
|                                        |                                        |
|     if ch == 'A' or 'B':               |     if ch == 'A' or ch == 'B':         |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |     :pythontest: off                   |
|                                        |                                        |
|     if a and b > 10:                   |     if (a > 10) and (b > 10):          |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Unnecessarily testing expressions against ``0``, ``True``, ``False``, ``None`` or ``""``
----------------------------------------------------------------------------------------

The examples below on the left will work perfectly well, but contain code that is unnecessary.  If you wish to compare whether a value is non-zero, is not empty, or is ``True``, you simply need to test the variable name alone.  You would not type in the expression ``a > 0 == True``, but ``a > 0`` instead.  Therefore, do not type in an expression such as ``a == True``, but simply test against ``a`` instead.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |     :pythontest: off                   |
|                                        |                                        |
|     if a != 0 and b != 0:              |     if a and b:                        |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |     :pythontest: off                   |
|                                        |                                        |
|     if a == 0 and str == '':           |     if not a and not s:                |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |     :pythontest: off                   |
|                                        |                                        |
|     if a == True:                      |     if a:                              |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |     :pythontest: off                   |
|                                        |                                        |
|     if a == False:                     |     if not a:                          |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Getting the number of brackets wrong in an expression
-----------------------------------------------------

Always ensure that the same number of left brackets ``[`` or ``(`` matches the number of right brackets ``]`` or  ``)``, respectively.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print(2 + (4 * (8 / (10 / 5))      |     print(2 + (4 * (8 / (10 / 5))))    |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print(((10 + 20) ** 2)             |     print(((10 + 20) ** 2))            |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print((10 + 20) / 8 / 4))          |     print((10 + 20) / (8 / 4))         |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     nums = [10, 20, [40, 50]           |     nums = [10, 20, [40, 50]]          |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Indexing past the end of lists
------------------------------

Do not index past the end of a sequence, which ranges from 0 up until the length of the list but one (i.e. 0 to 2, inclusive, in the example below).

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     names = ['fred', 'bob', 'tom']     |     names = ['fred', 'bob', 'tom']     |
|     print(names[3])                    |     if 3 < len(names):                 |
|                                        |         print(names[3])                |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Forgetting the brackets when calling a function
-----------------------------------------------

Always include parentheses when invoking (:term:`calling`) a function.  Simply typing the name of the function will provide you with its memory location - it will not actually run it!

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     int                                |     int()                              |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     turtle.begin_fill                  |     turtle.begin_fill()                |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print(math.sqrt 144)               |     print(math.sqrt(144))              |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print(int '1010101', 2)            |     print(int('10101010', 2))          |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Using variable names reserved by Python
---------------------------------------

Do not use reserved keywords as names in your code.  To see Python's full list of keywords, then import the ``keyword`` module and type ``keyword.kwlist`` in the interactive interpreter.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     for = 10                           |     for_num = 10                       |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     if = 100                           |     if_num = 100                       |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     while = 'fred'                     |     while_str = 'fred'                 |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Getting the indentation wrong
-----------------------------

Python uses :term:`indentation` (the practice of "pushing in" your code from the left-hand side) to define blocks of code.  Ensure that each block of code is exactly indented in the same manner (i.e. they start in the same column as other lines at the same level or indentation).  It is recommended practice to use an indentation of 4 spaces for each code block.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     print('Hello there')               |     print('Hello there')               |
|         print('How are you?')          |     print('How are you?')              |
|                                        |                                        |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     for num in range(10):              |      for num in range(10):             |
|     print(num)                         |          print(num)                    |
|                                        |                                        |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     if a == 10:                        |     if a == 10:                        |
|         print('a is 10')               |         print('a is 10')               |
|       print('where is b?')             |         print('where is b?')           |
|                                        |                                        |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     if a == 10:                        |     if a == 10:                        |
|         print('a is 10')               |         print('a is 10')               |
|     print('where is b?')               |         print('where is b?')           |
|     else:                              |     else:                              |
|         print('and what might c be?')  |         print('and what might c be?')  |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Using an ``elif`` or ``else`` without an ``if``
-----------------------------------------------

A selection statement must always include an ``if`` statement, with the ``elif`` and ``else`` statements being optional (i.e. you do not have to include them).

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     a = 10                             |     a = 10                             |
|     elif a > 10:                       |     if a == 10:                        |
|         print('larger than ten')       |         print('a is ten')              |
|     else:                              |     elif a > 10:                       |
|         print('something else')        |         print('larger than ten')       |
|                                        |     else:                              |
|                                        |         print('something else')        |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Placing a condition after an ``else``
-------------------------------------

The ``else`` line within an ``if`` statement can be read as *otherwise do this* - or if all of the tests above are ``False`` then do this instead.  It is not meant to include a test of its own.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     a, b = 10, 20                      |     a, b = 10, 20                      |
|     if a > b:                          |     if a > b:                          |
|         print('a is larger')           |         print('a is larger')           |
|     elif a < b:                        |     elif a < b:                        |
|         print('b is larger')           |         print('b is larger')           |
|     else a == b:                       |     else:                              |
|         print('a and b are the same')  |         print('a and b are the same')  |
|                                        |                                        |
+----------------------------------------+----------------------------------------+

Getting stuck in a loop
-----------------------

Your loops should always include a way out, whether via the condition at the top eventually changing from ``True`` to ``False``, or having a ``break`` statement which is performed selectively.

+----------------------------------------+----------------------------------------+
| Bad                                    | Good                                   |
+========================================+========================================+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |                                        |
|                                        |                                        |
|     num = 0                            |     num = 0                            |
|     while num < 10:                    |     while num < 10:                    |
|         print(num)                     |         print(num)                     |
|                                        |         num = num + 1                  |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
| .. code-block:: py3con                 | .. code-block:: py3con                 |
|     :pythontest: off                   |     :pythontest: compile               |
|                                        |                                        |
|     while True:                        |     while True:                        |
|         name = input('Name? ')         |         name = input('Name? ')         |
|         print(name)                    |         if name == 'quit':             |
|                                        |             break                      |
|                                        |         print(name)                    |
|                                        |                                        |
+----------------------------------------+----------------------------------------+
