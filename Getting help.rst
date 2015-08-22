Getting help
============

Save Our Sanity
---------------

Python is a very helpful programming language, when we need to find out more information.  And it is all built-in so we do not even need to go elsewhere to find it.

On a general level, you can use the interactive shell to enter the help utility like so::

    >>> help()
    
So if you remember what we taught in chapter 3, this means that ``help`` is a function, and it is being called by placing brackets ``()`` after its name.

When we are in the help utility, the prompt changes from ``>>>`` to ``help>``, to avoid confusing the two.  The first thing to learn is how to exit the help system:

.. code:: python
    :pythontest: nooutput

    help> quit
    >>>
    
In actual fact, just pressing the Enter key without any text will do the same!

Now, if you re-enter the help utility, you can type any command or function to get further information on that item.  For example:

.. code:: python
    :pythontest: nooutput

    >>> help()
    help> print

This will display some information on the print function.  If the help utility does not recognise what you have typed, it will say so.

You need not enter the help utility to get further information, though.  You can do it from the interactive prompt as well::

    >>> help(print)
    
This will display the same information as before, but it takes less effort to get to it!

You can also get help on values or types of data::

    >>> help(10)
    >>> help(12.8)
    
These will display information on integers and floating point numbers, respectively.  Do not worry about what is displayed at this point - much of it will not make much sense yet!

Using the proper names of the types of data will display the same information::

    >>> help(int)
    >>> help(float)

To get a list of what is built into Python, you can call the *directory* function in this way:

.. code:: python
    :pythontest: nooutput

    >>> dir(__builtins__)
    ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
     '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
     '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__',
     '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
     '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
     '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items',
     'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
    
This will list a number of error codes, followed by a number of built-in functions.  These functions can be used just by referring to their name, followed by parentheses (round brackets) to call them.  For example, one of the built-in functions is ``round``, so we can simply call it as follows::

    >>> round(10.75)
    11
     
which returns a value of 11, as you would expect.

You can get more help on these functions by using the help function again.  For example::

    >>> help(round)
    
will give more information on the round function, such as what it accepts (a number, and optionally the number of digits to round the number to), and what it returns back (another number, the rounded result).

In the previous chapter, we introduced the notion of bring in a separate program (often called a *module*) into our own using the *import* command.  But how do we know what available programs there are to import?  To find this out, we can type the following::

    >>> help('modules')
    
This takes a few seconds for Python to work out, but it will list every available module that can be imported by your program, including the ``math`` or ``turtle`` module we used in the previous chapter.

To delve deeper, we can find out more information on functions inside these other modules by using the dot notation as introduced last time.  So, for example, if we want to find out more information on the square root function inside the math module, we could do the following:

    >>> import math
    >>> help(math.sqrt)
    
.. note:: You must import the module before you can get help on its contents.  Otherwise Python does not know what is inside it.

For further information and a guide on the language, please refer to *The Python Tutorial*, which includes many more examples and covers more language features than we will be doing in this guide!

Things to remember
------------------

1. To get help, use the ``help()`` function in the interactive shell with the item on which your require further information, and the ``dir()`` function to get a directory listing on the ``__builtins__`` (double underscore at each end) or a particular module.
