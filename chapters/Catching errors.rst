Catching errors
===============

.. quote::
    :author: Unknown

    At the source of every error which is blamed on the computer you will find at least two human errors, including the error of blaming it on the computer.

It's broke
----------

.. pythontest:: off

Computer users generally get annoyed when the programs they are using break easily.  These programs are fragile, or brittle, and basically fall over or "crash" when something out of the ordinary happens.  However, mistakes are made, unexpected things occur, programs are even used for purposes they were not intended.  These things happen in real life, and computer programs should be resilient enough to keep on going, and not stop dead in their tracks.  If the user has typed in the 13th month by accident, the program should tell the user so rather than falling apart.  If the user has asked for a file to be opened that no longer exists, the program should inform the user instead of disappearing down a hole.  If the user has asked for a number to be divided by zero, then the program should report the error rather than losing all the user's data up to that point.  Unhappy users will stop using your program and switch to another that is not so delicate.

So the idea is for your program not to fail, but to handle errors gracefully and inform the user politely what has happened.  This is a much more pleasant experience for the user of your program.

In Python, we encounter many errors, also known in Python as :term:`exceptions`. We have arithmetic errors, where we cannot divide a number by zero::

    >>> 200 / 0
    Traceback (most recent call last):
      File "<stdin>`"`, line 1, in <module>
    ZeroDivisionError: division by zero

:term:`Syntax errors`, where the program is breaking the rules of the language::

    >>> if broken = True:
      File "<stdin>", line 1
        if broken = True:
                  ^
    SyntaxError: invalid syntax

Errors with functions, such as passing in two arguments where only one is expected::

    >>> input('I\'m', 'not working')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: input expected at most 1 arguments, got 2

And all sorts of other errors::

    >>> 1 + 'two'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>> error += 1
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'error' is not defined
    >>> lst = ['more', 'bad', 'bugs']
    >>> lst[5]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

.. pythontest:: all

Some common Python exceptions:

======================= ============================================================
Name                    Common reason
======================= ============================================================
``ZeroDivisionError``   You divided something by zero
``FileNotFoundError``   You tried to open a non-existent file
``ImportError``         You tried to import a module that does not exist
``NameError``           You have forgotten to define a variable
``SyntaxError``         Your syntax is wrong
``TypeError``           You tried to add a string and an integer
``ValueError``          You tried to convert a non-number string into an integer
======================= ============================================================

Exceptions are helpful - they give the program information on what has happened so that it can do something about it.  They tell us that something is broken, which we should fix.  However, it is also nice to be able say "if there is an error, do this".  In Python, this is called a ``try``-``except`` block.

``try`` not to crash
--------------------

Say we have some code that could produce an error::

    your_age = int(input('Your age: '))

.. pythontest:: off

If the user types an integer number, it works fine.  But if the user types something else - even a floating point number - we get an exception::

    >>> your_age = int(input('Your age: '))
    Your age: blah blah
    Traceback (most recent call last):
      File "<pyshell#4>", line 1, in <module>
        your_age = int(input('Your age: '))
    ValueError: invalid literal for int() with base 10: 'blah blah'

.. pythontest:: nooutput

We could test the string to see if it is a number (``str.isdigit``), but instead we will try to handle the problem when it is occurs.  This means that our code will be shorter and neater - otherwise every time you use a value that is unknown, it will need to be checked to see whether its contents are correct.  This approach often results in a program where the error checking code takes up more space than the code that actually does the work!  It also allows another part of your program to handle the errors instead of having to deal with them immediately - for example, a worker may not know what to do when a problem occurs, but his boss will!  This last point is more obvious in larger programs rather than the small ones we will be writing here.

To handle an error when it occurs, we type ``try:``, followed by our code, which should be indented, just like an ``if`` statement. Then we type ``except:``, followed by the code we want run when there is an error::

    try:
        your_age = int(input('Your age: '))
    except:
        print('Err... No.')

Think of this as if the code will *try* to run a block of code - the call to ``int`` and ``input`` in this example - *except* if an error occurs then jump straight into this extra block of code.  The extra block of code can be run at any time when an error occurs.  This means if the initial block may or may not finish.

If the user types in a number as expected, all is well::

    >>> try:
            your_age = int(input('Your age: '))
        except:
            print('Err... No.')
        
    Your age: 99
    >>> your_age
    99

If the user types in something that is not expected, a message will be displayed instead::

    >>> try:
            your_age = int(input('Your age: '))
        except:
            print('Err... No.')
        
    Your age: blah blah blah
    Err... No.

.. pythontest:: all

This works with any code::

    >>> try:
            a = 2 / 0
        except:
            print('Maths says no!')
        
    Maths says no!

Let's be specific about the problem
-----------------------------------

Using the ``try``-``except`` block as above works fine, but what if we only want to catch one type of exception? For instance, the following code contains an invalid variable, but we will never know, because the ``except`` is catching every exception, including the exception due to the invalid variable::

    >>> i_do_exist = '123'
    >>> try:
            a = int(i_do_not_exist)
        except:
            print('That was not a number!')
        
    That was not a number!

The exception that we want to catch is a ``ValueError``:

.. code-block:: py3con
    :pythontest: norun

    >>> int('abc')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: 'abc'

So, instead of typing ``except:``, we can type ``except ValueError:``. This will catch errors due to converting non-numbers, but not other errors:

.. code-block:: py3con
    :pythontest: norun

    >>> i_do_exist = '123'
    >>> try:
            a = int(i_do_not_exist)
        except ValueError:
            print('That was not a number!')
        
    Traceback (most recent call last):
      File "<stdin>", line 2, in <module>
    NameError: name 'i_do_not_exist' is not defined

In general, you should name the type of exception you wish to handle.  If you do not name the exception in order to catch all possible errors, then you may miss problems you should be handling differently.  It is simply a case of best practice.

.. pythontest:: nooutput

To find a full list of error types, you can type the :term:`directory function` ``dir`` in the interactive interpreter::

    >>> dir(__builtins__)

.. pythontest:: all

The errors that you can use to filter your errors are listed at the start - generally they have the word error at the end: ``ArithmeticError``, ``AssertionError``, ``AttributeError``, ``BaseException``, all the to ``ZeroDivisionError`` at the end.

Exercises
---------

#. Add ``try``-``except`` blocks to your programs from :ref:`chapter 8`, printing out "That was not a number" when the user types in a non-number.

#. Write a program that takes two numbers, and divides one by the other. Print out a message when it tries to divide by zero using a ``try``-``except`` (the exception type is ``ZeroDivisionError``).

#. Write a program called :file:`openfile.py` which asks the user for a filename, opens the file and prints out its contents, just like in :ref:`chapter 20` on reading files. However, this time, if the file does not exist you should print out a suitable message such as "Sorry, that file does not exist".  The error you need to trap is called ``FileNotFoundError``.

Things to remember
------------------

#. Use ``try``-``except`` blocks to catch :term:`exceptions`.  Exceptions are errors or problems raised for the program to handle in a proper manner.

#. The code inside a ``try``-``except`` block is indented, like an ``if`` block.

#. It is best to name an exception type, to avoid surprises.  You can find out what the exception type is by using the interactive interpreter to provoke the same error.

#. :term:`Syntax errors` are when the program breaks the rules of the language.  :term:`Runtime errors` or :term:`logical errors` are problems in the operation of the program itself.
