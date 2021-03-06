Writing files
=============

.. quote::
    :author: Larry Bossidy

    Complexity has nothing to do with intelligence, simplicity does.

Prepare your ink
----------------

The opposite to reading a file is writing to it.  Whilst in the previous chapter on reading we used IDLE's editor to create a file in order to read from it, this chapter we will do the writing from within the program itself.

To write to a file, we first have to open it in writing mode. To do this, we pass a mode of ``'w'`` into the ``open`` function::

    >>> f = open('todo.txt', 'w')

This will open the file, creating it if it does not exist, and assigns the data containing the open file to the variable ``f``. The file is then emptied or truncated, "cleaning the slate" for any data you will write.  In the previous chapter, we could have passed in ``'r'`` for reading, but this is not necessary as it is the default (normal) behaviour when opening a file.

Learning to write
-----------------

To write a string to the file, we use the ``write`` function::

    >>> f.write('Do homework\n')

Subsequent calls to write will append data on the end, instead of overwriting::

    >>> f.write('Make death star fully armed and operational\n')

The file will now look like:

.. code-block:: none
    :pythontest: off

    Do homework
    Make death star fully armed and operational

.. note:: If you forget the newlines ``'\n'``, then the file will look like this:

    .. code-block:: none
        :pythontest: off

        Do homeworkMake death star fully armed and operational

After writing, always remember to ``close`` the file, or the data may not be written fully.  This is why we always have to 'Safely Remove' our USB sticks before we physically remove them from the Raspberry Pi computer - data may still be in the process of being written to one or more files.

Writing lists
-------------

To write a list of lines, like that produced by ``readlines``, we use ``writelines``::

    >>> f = open('todo.txt', 'w')
    >>> f.writelines(['Do homework\n',
                      'Make death star fully armed and operational\n'])
    >>> f.close()

Exercises
---------

#. Write a program called :file:`notes.py` which repeatedly asks the user for a sentence, stores it in a variable (a string), and writes it out to file each time (a file called :file:`notes.txt` for instance).  The loop should stop (break out) when the user types 'stop'.  Use a ``while`` loop to keep on asking the user for input, and the file ``write`` function to write the sentence to the file.  At the end of the program, the file should contain each sentence, one after the other, each taking up a line by itself.

#. Modify the program in exercise 1 so that each line is prefixed by the line number, so the first sentence is output with ``"1. "`` added onto the beginning, with the second having ``"2. "`` added on at the beginning, and so on.

#. Write a program called :file:`cipher.py` so that it reads in a sentence, but instead of writing the sentence to a file, it writes the ordinal value of each character instead.  To find out the ordinal value of a character, use the built-in ``ord`` function, passing in a single character at a time.  You only need to read in one sentence, but you will need to step over the sentence using a ``for`` loop.  To check your result, an input of ``"abcdef"`` should be stored in the file as ``"97 98 99 100 101 102"`` (i.e. the numbers from 97 for 'a', to 102 for 'f'), and an input of ``"ABCDEF"`` should be stored as "65 66 67 68 69 70" (i.e. the numbers from 65 to 70).  Separate each number by a space as demonstrated above.  Remember, the ``str`` function can take an integer and return a string in order for you to output it to file using the ``write`` function.

Things to remember
------------------

#. Use the built-in ``open`` function with the ``'w'`` mode to open files for writing.

#. Use the ``write`` function on the file variable to write a string to a file.

#. Use the ``writelines`` function on the file variable to write a list of lines to a file.

#. Don't forget to call the ``close`` function on the file when you have finished.
