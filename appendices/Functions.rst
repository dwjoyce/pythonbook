:orphan:

Functions in Python
===================

Functions are named sections of code.  They are useful in terms of keeping common code together in one place that can be called from any number of other locations.  They can accept data in from the calling code, and can also return data back.  Functions are called by using their name, and by typing parentheses after their name.  Any data being passed in - *arguments* - are placed inside the appropriate parentheses.

Built-in functions
------------------

Python 3 has a number of built-in functions:

abs, all, any, ascii, bin, bool, bytearray, bytes, callable, chr, classmethod, compile, complex, copyright, credits, delattr, dict, dir, divmod, enumerate, eval, exec, exit, filter, float, format, frozenset, getattr, globals, hasattr, hash, help, hex, id, input, int, isinstance, issubclass, iter, len, license, list, locals, map, max, memoryview, min, next, object, oct, open, ord, pow, print, property, quit, range, repr, reversed, round, set, setattr, slice, sorted, staticmethod, str, sum, super, tuple, type, vars, zip

You can get this list by typing dir(__builtins__) in IDLE, but the full list will include other built-in items as well (e.g. exception types).

These can be called by any Python program without having to import anything else – they are built-in to the language itself.

.. pythontest:: nooutput

For example::
    
    >>> abs(-123)
    >>> range(10)
    >>> min([10,20,5,15])
    >>> print('Hello there')

Local functions
---------------

You can define your own functions in your Python module by using the ``def`` keyword.  This can then be called within your own program by simply using the name of the function itself, similar to a built-in function.

For example, here are four functions that we have written ourselves::

    def say_hello():
        print 'hello'

    def say_hello_times(times):
        print 'hello' * times

    def square_number(number):
        return number * number

    def lowest_highest(numbers):  # accepts a list of numbers
        lowest = min(numbers)
        highest = max(numbers)
        return lowest, highest  # returns two values

Which can then be called as follows::

    say_hello()
    say_hello_times(10)
    print(square_number(5))  # prints 25
    low, high = lowest_highest([5,10,35,15,50,20])

Imported functions
------------------

You can use functions in other modules by importing them first.

For example, to use functions inside the Math module, you can do the following::

    import math
    print math.sqrt(100)

You need to write module name followed by a period '.' before the name of the function when calling it.

You can print out a listing of what a module contains by performing a 'dir' on its name, for example::

    >>> dir(math)

Functions belonging to a type ('class methods')
-----------------------------------------------

A particular class of values is called a type (integers, floating point numbers, strings, files), and these contain functions on the data that the type contains.

For example, to change a sentence to uppercase you can do the following::

    >>> message = 'mary had a little lamb'
    >>> print message.upper()  # prints 'MARY HAD A LITTLE LAMB'

You need write variable name followed by a period '.' before the name of the function when calling it.

You can list the functions that a type contains by performing a 'dir' on its name, for example::

    >>> dir(int)
    >>> dir(float)
    >>> dir(string)

This will show that some types have functions that are not relevant to other types.  For example, a the type float has a function called is_integer() which returns True if it is a whole number, False if not.  Strings have functions such as lower(), split(), title(), upper(), which are relevant to strings of characters, but not numbers and files.
