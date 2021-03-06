Functions and Maths
===================

.. quote::
    :author: Michael Palin
    :source: The Argument Sketch - Monty Python's Flying Circus

    Ah. I'd like to have an argument, please.

Basic functions
---------------

In Maths, you learn about :term:`functions`. An example of a simple function is:

.. math:: f(x) = x + 1

This function takes in a number, :math:`x`, and adds one to it. So if :math:`x = 1`, then :math:`f(x) = 2`. In Python-speak, :math:`x` is an :term:`argument`, and the result, :math:`f(x)` is the :term:`return value`. Every function gives back a value, its return value.

Python also has :term:`functions`. You can make your own functions, but in this chapter, we will focus on using functions that Python already has, called :term:`built-in functions`. The first function we'll use is called ``abs``, which stands for absolute value::

    >>> abs
    <built-in function abs>

What this function does is, given any number, positive or negative, it returns a positive number with a magnitude equal to the number you give it. This means that if you give it ``6``, it will return ``6``, but if you give it ``-9``, it will return ``9``. The way you use this function is you write the function name, ``abs``, then a opening parenthesis, ``(``, then the number you want, let's say ``-42``, and finally a closing parenthesis, ``)``, to tell Python that we are finished::

    >>> abs(-42)
    42

It works just as you would expect.  We can do this with other numbers, including numbers with decimal places::

    >>> abs(2)
    2
    >>> abs(-123.45)
    123.45
    >>> abs(0)
    0

We can say that ``abs`` is a function that takes one argument, a number, and :term:`returns` the positive version of that number. In the above example, we can say that we :term:`called` ``abs`` with ``-123.45`` as an :term:`argument`.

More arguments
--------------

But not all functions take one argument. An example of a function that takes two arguments is ``round``. It takes a number to be rounded, usually a fractional number, and a whole number of decimal places to round the first number to. So rounding ``123.12`` to ``1`` decimal place should give ``123.1``. How do we call a function with more than one argument? We separate the arguments with commas. To call round as we described, we write ``round``, then ``(``, our first argument, ``123.12``, then a comma, ``,``. We then write our second argument, ``1`` and a closing parenthesis, ``)``::

    >>> round(123.12, 1)
    123.1

``round`` can round to any number of decimal places to round to::

    >>> round(98765.4321, 3)
    98765.432
    >>> round(0.123456789, 7)
    0.1234568
    >>> round(0.123456789, 0)
    0.0
    >>> round(0.123456789, 20)
    0.123456789

When the number of decimal places to round to is greater then the precision of the number to round, ``round`` does nothing. ``round`` can also take a negative number of decimal places, like scientific notation (or standard form)::

    >>> round(12345.6, -1)
    12350.0
    >>> round(12345.6, -3)
    12000.0

If you call ``round`` with ``-2``, it makes the last two non-fractional digits zeros. Another two-argument function is ``pow`` (power). ``pow(x, y)`` is equivalent to ``x ** y``::

    >>> pow(3, 4)
    81
    >>> pow(-2, 5)
    -32
    >>> pow(64, 0.5)
    8.0

How many arguments can one function have?
-----------------------------------------

That depends!  Some functions take any number of arguments. ``min`` is a function that takes two or more arguments, and returns the smallest one::

    >>> min(1, 8)
    1
    >>> min(4, 1, 9)
    1
    >>> min(-2, 5, -256, 7, 2, -5, -10, 100)
    -256
    >>> min(0.5, 0.125)
    0.125

If you don't give ``min`` enough arguments, Python gives an error:

.. code-block:: py3con
    :pythontest: compile

    >>> min()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: min expected 1 arguments, got 0

Other functions also give errors if you don't give the right number of arguments:

.. code-block:: py3con
    :pythontest: compile

    >>> abs()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: abs() takes exactly one argument (0 given)
    >>> abs(1, 2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: abs() takes exactly one argument (2 given)
    >>> round(5, 9, 1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: round() takes at most 2 arguments (3 given)

``max`` is a similar function to ``min``, except that it returns the largest argument::

    >>> max(1, 8)
    8
    >>> max(4, 1, 9)
    9
    >>> max(-2, 5, -256, 7, 2, -5, -10, 100)
    100
    >>> max(0.5, 0.125)
    0.5

Functions functioning
---------------------

You can use the return value of a function as an argument to another function, assign the return value to a variable and use variables as arguments::

    >>> max(-10, abs(-20))
    20
    >>> the_biggest_num = max(4, 9, 23, 56, 12, 5)
    >>> the_biggest_num
    56
    >>> a = 3
    >>> b = -4
    >>> c = 5
    >>> min(a, b, c)
    -4

Functions are also variables, so you can assign functions to new variables::

    >>> func = abs
    >>> func(-8)
    8
    >>> func
    <built-in function abs>
    >>> abs
    <built-in function abs>

Exercises
---------

#. Use ``abs`` to find the absolute value of ``-35.5``.

#. Use ``round`` to round ``-22.8364926`` to ``4`` decimal places.

#. Use both ``round`` and ``abs`` to find the absolute value of ``-7495.184758`` to ``2`` decimal places.

#. Use ``max`` and ``min`` to find the smallest and largest number from ``7``, ``-8``, ``4``, ``-12`` and ``1``.

Things to remember
------------------

#. :term:`Functions` are called with :term:`arguments` to give a :term:`return value`.

#. To call a function ``func`` with no arguments do ``func()``.

#. To call a function ``func`` with an argument ``arg`` do ``func(arg)``.

#. To call a function ``func`` with more than one argument, separate the arguments by commas: ``func(arg1, arg2, arg3, etc)``.

#. Functions return values that can be assigned to variables, e.g. ``num = abs(-10)``, and variables and return values can be used as arguments, e.g. ``abs(num)`` and ``abs(round(-10.75))``.
