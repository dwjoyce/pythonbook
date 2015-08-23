Catching errors
===============

It's broke
----------

.. pythontest:: off

In Python, we encounter many errors, also known in Python as *exceptions*. We have arithmetic errors::

    >>> 200 / 0
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

Syntax errors::

    >>> if broken = True:
    File "<stdin>", line 1
        if broken = True:
                ^
    SyntaxError: invalid syntax

Errors with functions::

    >>> input("I'm", "not working")
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: input expected at most 1 arguments, got 2

And all sorts of other errors::

    >>> 1 + "two"
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> error += 1
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    NameError: name 'error' is not defined
    >>> lst = ["more", "bad", "bugs"]
    >>> lst[5]
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    IndexError: list index out of range

Some common Python exceptions:

======================= ============================================================
Name                    Common reason
======================= ============================================================
``ZeroDivisionError``   You divided something by zero
``IOError``             You tried to open a non-existant file
``ImportError``         You tried to import a module that does not exist
``NameError``           You have forgotten to define a variable
``SyntaxError``         Your syntax is wrong
``TypeError``           You tried to add a string and an integer
``ValueError``          You tried to convert a non-number string into an integer
======================= ============================================================

Exceptions are good. They tell us that something is broken, which we should fix. However, it is also nice to be able say "if there is an error, do this". In python, this is called a ``try``-``except`` block.


``try`` not to crash
--------------------

.. pythontest:: all

Say we have some code that could produce an error::

    your_age = int(input("Your age: "))

.. pythontest:: off

If the user types a number, it works fine. But if the user types something else, we gen an exception::

    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'something else'

.. pythontest:: nooutput

We could test the string to see if it is a number (``str.isdigit()``), but instead we will try catching the exception. To do that we type ``try:``, followed by our code, which should be indented, just like an ``if`` statement. Then we type ``except:``, followed by the code we want run when these is an error::

    try:
        your_age = int(input("Your age: "))
    except:
        print("Err... No.")

If the user behaves, all is well::

    >>> try:
            your_age = int(input("Your age: "))
        except:
            print("Err... No.")
        
    Your age: 99
    >>> your_age
    99

If the user does not behave, they get told off::

    >>> try:
            your_age = int(input("Your age: "))
        except:
            print("Err... No.")
        
    Your age: something else
    Err... No.

.. pythontest:: all

This works with any code::

    >>> try:
            a = 2 / 0
        except:
            print("Maths says no!")
        
    Maths says no!


Let's be specific about the problem
-----------------------------------

Using the ``try``-``except`` block as above work fine, but what if we only want to catch one type of exception? For instance the below code contains an invalid variable, but we will never know, because the ``except`` is catching every exception, including the exception due to the invalid variable::

    >>> i_do_exist = "123"
    >>> try:
            a = int(i_do_not_exist)
        except:
            print("That was not a number!")
        
    That was not a number!

The exception that we want to catch is a ``ValueError``:

.. code:: python
    :pythontest: norun

    >>> int("abc")
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'abc'

So, instead of typing ``except:``, we can type ``except ValueError``. This will catch errors due to converting non-numbers, but not other errors:

.. code:: python
    :pythontest: norun

    >>> i_do_exist = "123"
    >>> try:
            a = int(i_do_not_exist)
        except ValueError:
            print("That was not a number!")
        
    Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
    NameError: name 'i_do_not_exist' is not defined

In general, you should try to name a type of exception to catch, as you will not hide other errors, which may be causing your program to malfunction.

Exercises
---------

1. Add ``try``-``except`` blocks to your programs from chapter 8, printing out "That was not a number" when the user types in a non-number.
2. Write a program that takes two numbers, and divides one by the other. Print out a message when they try to divide by zero using a ``try``-``except`` (the exception type is ``ZeroDivisionError``).

Things to remember
------------------

1. Use ``try``-``except`` blocks to catch exceptions.
2. The code inside a ``try``-``except`` block is indented, like for an ``if`` block.
3. It is best to name an exception type, to avoid surprises.
