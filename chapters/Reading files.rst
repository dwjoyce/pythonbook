Reading files
=============

.. quote:: Brian W. Kernighan

    Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?

Opening the file
----------------

.. pythontest:: nooutput

The first step in reading a file is opening it. In python, we use the ``open`` function to open files::

    >>> f = open("mission.txt")
    >>> f
    <_io.TextIOWrapper name='mission.txt' mode='r' encoding='UTF-8'>

.. note::

    If you get the file name wrong, you will get an error like::

        >>> open("missing.txt")
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'


This shows that the file has been opened. The ``mode`` is ``"r"``, which means the it is open for reading. The other mode, ``"w"``, is for writing and it is covered in the chapter 21.

Reading words of wisdom
-----------------------

Once we have an open file, in this case ``f``, we can read the contents. The open file has a function, ``read``, to give the contents of the file as a string::

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

This allows us to do all the usual string things. If we want to convert the file into a list of words, we can do::

    >>> f = open("mission.txt")
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

    >>> words = len(open("mission.txt").read().split())
    >>> words
    81

However, if you play with files, you will some interesting behaviour, such as::

    >>> f = open("mission.txt")
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

If you read a file completely, the open file points to the end of the file. This is like having a book open on the last page. If you want to re-read the file, you can re-open the file, or use the function ``seek`` to move back to the start::

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

    >>> f = open("mission.txt")
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

This also works for the ``list`` function::

    >>> f = open("mission.txt")
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


To read directly to a list, we can use ``readlines``::

    >>> f = open("mission.txt")
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

Notice that in both cases, the newline characters (``"\n"``) are still in the string.

.. pythontest:: all

Put down the book
-----------------

When we have finished with a file, we should always call ``close``::

    >>> f.close()

This makes sure that any changes we make to the file are saved.

Exercises
---------

.. todo:: Exercises for Reading files


Things to remember
------------------

1. Use ``open`` to open files.
2. Use ``read`` to get the contents of the file.
3. Use a ``for`` loop to iterate over the file, getting each line.
4. Use ``readlines`` to get a list of lines.
5. When you ``read`` a file, you need to move back to the start by re-opening the file, or using ``seek``.

