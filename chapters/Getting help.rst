Getting help
============

.. quote::
    :author: Mosher's Law of Software Engineering

    Don't worry if it doesn't work right. If everything did, you'd be out of a job.

Save Our Sanity
---------------

Python is a very helpful programming language when we need to find out more information.  And it is all built-in so we do not even need to go elsewhere to find it.

On a general level, you can use the interactive interpreter to enter the help utility like so::

    >>> help()

So if you remember what we taught in :ref:`chapter 2`, this means that ``help`` is a function, and it is being called by placing parentheses ``()`` (round brackets) after its name.

When we are in the help utility, the prompt changes from ``>>>`` to ``help>``, to avoid confusing the two.  The first thing to learn is how to exit the help system:

.. code-block:: py3con
    :pythontest: nooutput

    help> quit
    >>>

In actual fact, just pressing the :button:`Enter` key without any text will do the same!

Now, if you re-enter the help utility, you can type any command or function to get further information on that item.  For example:

.. code::
    :pythontest: nooutput

    >>> help()
    help> round

This will display some information on the ``round`` function.  If the help utility does not recognise what you have typed, it will say so.

You need not enter the help utility to get further information, though.  You can do it from the interactive prompt as well::

    >>> help(round)

This will display the same information as before, but it takes less effort to get to it!

You can also get help on values or types of data::

    >>> help(10)
    >>> help(12.8)

These will display information on integers and floating point numbers, respectively.  Do not worry about what is displayed at this point - much of it will not make much sense yet!

Using the proper names of the types of data will display the same information::

    >>> help(int)
    >>> help(float)

To get a list of what is built into Python, you can call the :term:`directory function` in this way:

.. code:: py3con
    :pythontest: nooutput

    >>> dir(__builtins__)
    ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__',
     '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
     '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__',
     '__len__', '__lt__', '__ne__', '__new__', '__reduce__',
     '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
     '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy',
     'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault',
     'update', 'values']

This will list a number of error codes, followed by a number of built-in functions.  These functions can be used just by referring to their name, followed by parentheses to call them.  For example, one of the built-in functions is ``round``, so we can simply call it as follows::

    >>> round(10.75)
    11

which returns a value of 11, as you would expect.

You can get more help on these functions by using the help function again.  For example::

    >>> help(round)

will give more information on the round function, such as what it accepts (a number, and optionally the number of digits to round the number to), and what it returns back (another number, the rounded result).

In the previous chapter, we introduced the notion of bringing in a separate program (often called a :term:`module`) into our own using the ``import`` command.  But how do we know what available modules there are to import?  To find this out, we can type the following::

    >>> help('modules')

This takes a few seconds for Python to work out, but it will list every available module that can be imported by your program, including the ``math`` or ``turtle`` modules we used previously.

To see what is inside a module, once you have imported it, you can perform a ``dir`` on the module name, for example:

.. code-block:: py3con
    :pythontest: nooutput

    >>> import turtle
    >>> dir(turtle)

To delve deeper, we can find out more information on functions inside these other modules by using the dot notation as introduced last time.  So, for example, if we want to find out more information on the square root function inside the ``math`` module, we could do the following::

    >>> import math
    >>> help(math.sqrt)

.. note:: You must import the module before you can get help on its contents.  Otherwise Python does not know what is inside it.

For further information and a guide on the language, please refer to *The Python Tutorial* at :file:`Computing/Python 3.4.2 docs/tutorial/index.html`, which includes many more examples and covers more language features than we will be doing in this guide!

Things to remember
------------------

#. To get help, use the ``help()`` function in the interactive interpreter with the item on which your require further information, and the ``dir()`` function to get a directory listing on the ``__builtins__`` (double underscore at each end) or a particular module.
