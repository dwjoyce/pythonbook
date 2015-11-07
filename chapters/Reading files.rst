Reading files
=============

.. quote::
    :author: Brian W. Kernighan

    Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?

Opening the file
----------------

.. pythontest:: nooutput

We have used Python to store values in memory by using variables.  Type the following in the interactive shell::

    >>> message = 'The attack starts at dawn'
    >>> troops = 85
    >>> print('Your message:', message, 'and your troops:', troops)

However, storing values in memory by using variables is only transitory - just like your maths calculator.  If you store a number in memory using the ``MS`` (memory store) button, turn your calculator off and on again, and try and recall the number you stored by using ``MR``, it will be gone.  Variables in computer memory are similar - when your program stops (or the computer is switched off), the memory is gone.  To demonstrate this, having typed in the code above, select the *Restart Shell* menu item from the *Shell* menu.  Then redo the print command (you can use the up arrow and press the Return key twice), and see what happens - Python will complain it cannot find the variables stating you have not defined them.  In other words, they have gone from memory!

So how do we retain information from one run of our program to the next?  How do we, as a computer scientist would say, make our data persistent - i.e. recall the data when the program is run again?  Think of a game with a highest scores table - we need a way to store these numbers (and names) so that they can be read and changed every time the game is run.  To do this, we need to place our data in a :term:`file` that is stored on disk - whether a hard drive or flash storage such as a USB stick.  This data, when the electricity is turned off, retains its state - the data does not drain away with the current!  To work with files, we need to learn how to read from them (in this chapter) and write to them (in the next).

The first step in reading a file is opening it.  Think if a file like a folder or a book - before you can start reading its contents, you need to open its cover to reveal the pages within.  Firstly, we need to create our book, so click on File -> New File, and copy in the following text (remember to use Ctrl-C keys to copy and Ctrl-V to paste):

.. code-block:: none
    :pythontest: off

    Three Rings for the Elven-kings under the sky,
    Seven for the Dwarf-lords in their halls of stone,
    Nine for Mortal Men doomed to die,
    One for the Dark Lord on his dark throne,
    In the Land of Mordor where the Shadows lie,
    One ring to rule them all, one ring to find them,
    One ring to bring them all and in the darkness bind them
    In the Land of Mordor where the Shadows lie.

    - The Lord of the Rings, Epigraph

Save it as mission.txt, making sure you save it in your home directory (``/home/pi`` directory), not on your USB stick.  That way we can experiement with it in the interactive shell.  We now have a file to open and read.

In Python, we use the ``open`` function to open files, so type the following::

    >>> f = open('mission.txt')
    >>> f
    <_io.TextIOWrapper name='mission.txt' mode='r' encoding='UTF-8'>

This shows that the file has been opened. The ``mode`` is ``'r'``, which means the it is open for reading. The other mode, ``'w'``, is for writing and it is covered in the next chapter.  Note you have to enclose the name of the file - the *filename* - in quotation marks as it is string.  If this does not work, make sure the *mission.txt* file is in the correct location as indicated above.

We have called the variable that refers to our open file ``f``, but it could be called anything just like other variables, such as ``my_file``, ``saurons_dark_secret``, ``input_file``, ``my_todo_list`` or the like.

.. note::

    If you get the filename wrong (or the file is located in a different directory), you will get an error like this::

        >>> open('missing.txt')
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'

Reading words of wisdom
-----------------------

Once we have an open file, in this case ``f``, we can read its contents. The open file has a function, ``read``, to give the contents of the file as a string::

    >>> print(f.read())
    Three Rings for the Elven-kings under the sky,
    Seven for the Dwarf-lords in their halls of stone,
    Nine for Mortal Men doomed to die,
    One for the Dark Lord on his dark throne,
    In the Land of Mordor where the Shadows lie,
    One ring to rule them all, one ring to find them,
    One ring to bring them all and in the darkness bind them
    In the Land of Mordor where the Shadows lie.

    - The Lord of the Rings, Epigraph 

This allows us to call all the functions that belong to the string type.  To convert the file into a list of words, type the following::

    >>> f = open('mission.txt')
    >>> f.read().split()
    ['Three', 'Rings', 'for', 'the', 'Elven-kings', 'under', 'the', 'sky,',
    'Seven', 'for', 'the', 'Dwarf-lords', 'in', 'their', 'halls', 'of',
    'stone,', 'Nine', 'for', 'Mortal', 'Men', 'doomed', 'to', 'die,', 'One',
    'for', 'the', 'Dark', 'Lord', 'on', 'his', 'dark', 'throne,', 'In',
    'the', 'Land', 'of', 'Mordor', 'where', 'the', 'Shadows', 'lie,', 'One',
    'ring', 'to', 'rule', 'them', 'all,', 'one', 'ring', 'to', 'find',
    'them,', 'One', 'ring', 'to', 'bring', 'them', 'all', 'and', 'in', 'the',
    'darkness', 'bind', 'them', 'In', 'the', 'Land', 'of', 'Mordor', 'where',
    'the', 'Shadows', 'lie.', '-', 'The', 'Lord', 'of', 'the', 'Rings,',
    'Epigraph']

And to count the number of words in the file we can do::

    >>> words = open('mission.txt').read().split()
    >>> len(words)
    81

However, if you play with files, you will some interesting behaviour, such as::

    >>> f = open('mission.txt')
    >>> f.read()
    'Three Rings for the Elven-kings under the sky,\nSeven for the
    Dwarf-lords in their halls of stone,\nNine for Mortal Men doomed
    to die,\nOne for the Dark Lord on his dark throne,\nIn the Land
    of Mordor where the Shadows lie,\nOne ring to rule them all, one
    ring to find them,\nOne ring to bring them all and in the
    darkness bind them\nIn the Land of Mordor where the Shadows lie.
    \n\n - The Lord of the Rings, Epigraph \n'
    >>> f.read()
    ''

These special escape sequences (such as ``\n`` for new line and ``\t`` for tab) were covered briefly in chapter 7 on printing.  This is the text file as it really is, not formatted nicely for reading.

If you read a file completely, the open file points to the end of the file. This is like having a book open at the end of the last page. If you want to re-read the file, you can re-open the file (similar to closing a book and reopening it at the beginning again), or use the function ``seek`` to move back to the start (similar to flicking through the pages back to the beginning, but much quicker)::

    >>> f.seek(0)
    0
    >>> f.read()
    'Three Rings for the Elven-kings under the sky,\nSeven for the
    Dwarf-lords in their halls of stone,\nNine for Mortal Men doomed
    to die,\nOne for the Dark Lord on his dark throne,\nIn the Land
    of Mordor where the Shadows lie,\nOne ring to rule them all, one
    ring to find them,\nOne ring to bring them all and in the
    darkness bind them\nIn the Land of Mordor where the Shadows lie.
    \n\n - The Lord of the Rings, Epigraph \n'

Line by line
------------

To get the entire file as a string, we use ``read``. If we want it line by line, however, we can use a ``for`` loop, and iterate over the file::

    >>> f = open('mission.txt')
    >>> for line in f:
            print(line)
        
    Three Rings for the Elven-kings under the sky,

    Seven for the Dwarf-lords in their halls of stone,

    Nine for Mortal Men doomed to die,

    One for the Dark Lord on his dark throne,

    In the Land of Mordor where the Shadows lie,

    One ring to rule them all, one ring to find them,

    One ring to bring them all and in the darkness bind them

    In the Land of Mordor where the Shadows lie.



    - The Lord of the Rings, Epigraph 

For most purposes, this is the best way to read a file and fits in well with what we have learnt elsewhere in the book.  Notice how the print inserts an extra blank line in-between each line from the file - since the line from the file contains a new line character already, this is added onto the new line that the print function does ordinarily.

This also works for the ``list`` function::

    >>> f = open('mission.txt')
    >>> list(f)
    ['Three Rings for the Elven-kings under the sky,\n',
     'Seven for the Dwarf-lords in their halls of stone,\n',
     'Nine for Mortal Men doomed to die,\n',
     'One for the Dark Lord on his dark throne,\n',
     'In the Land of Mordor where the Shadows lie,\n',
     'One ring to rule them all, one ring to find them,\n',
     'One ring to bring them all and in the darkness bind them\n',
     'In the Land of Mordor where the Shadows lie.\n',
     '\n', ' - The Lord of the Rings, Epigraph \n']

To read directly as a list, we can use ``readlines``::

    >>> f = open('mission.txt')
    >>> f.readlines()
    ['Three Rings for the Elven-kings under the sky,\n',
     'Seven for the Dwarf-lords in their halls of stone,\n',
     'Nine for Mortal Men doomed to die,\n',
     'One for the Dark Lord on his dark throne,\n',
     'In the Land of Mordor where the Shadows lie,\n',
     'One ring to rule them all, one ring to find them,\n',
     'One ring to bring them all and in the darkness bind them\n',
     'In the Land of Mordor where the Shadows lie.\n',
     '\n', ' - The Lord of the Rings, Epigraph \n']

Notice that in both cases, the newline characters (``'\n'``) are still in the string.

.. pythontest:: all

Put down the book
-----------------

When we have finished with a file, we should always call ``close`` on the file variable::

    >>> f.close()

This just like closing the covers of a book, or the flap of a real folder from a filing cabinet.  It is polite way to finish working on a file - in the next chapter, this becomes more essential.

Exercises
---------

For these exercises, you will need to copy the text file ``mission.txt`` from the home directory on the Raspberry Pi (``/home/pi/mission.txt``) to the same location as your programs on your USB stick (e.g. ``/home/pi/USB_STICKS/USB Disk``).

#. Open and print out the contents of the mission.txt file, converting each line to uppercase (tip: use the ``upper`` function on the line string to achieve this).

#. Open and print out the length of each line in the mission.txt file.

#. Open and step through each line of the mission.txt file.  Once done, print out the average word length - you will need to keep a running total of all the word lengths, plus how many words there were in order to print out the average.

Things to remember
------------------

#. Use the built-in ``open`` function to open files.

#. Use ``read`` function on the file variable to get the contents of the file.

#. Use a ``for`` loop to iterate over the file, getting each line in turn.  This is the best way to step over the contents of a file, one line at a time.

#. Use the ``readlines`` function on the file variable to get a list of lines.

#. When you ``read`` a file, you need to move back to the start by re-opening the file, or using ``seek``.
