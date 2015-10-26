Writing files
=============

.. quote::
    :author: Waseem Latif

    Give a man a program, frustrate him for a day.
    Teach a man to program, frustrate him for a lifetime.

Prepare your ink
----------------

The opposite to reading a file is writing to it.  Whilst in the previous chapter on reading we used IDLE's editor to create a file in order to read from it, this chapter we will do the writing from within the program.

To write to a file, we first have to open it in writing mode. To do this, we pass the ``'w'`` to ``open``::

    >>> f = open("todo.txt", 'w')

This will open the file, creating it if it does not exist, and assigns the data containing the open file to the variable ``f``. The file is then emptied or truncated, "cleaning the slate" for any data you will write.  In the previous chapter, we could have passed in ``'r'`` for reading, but this is not necessary as it is the default (normal) behaviour anyway.

Learning to write
-----------------

To write a string to the file, we use the ``write`` function::

    >>> f.write("Do homework\n")

Subsequent calls to write will append data on the end, instead of overwriting::

    >>> f.write("Make death star fully armed and operational\n")

The file will now look like:

.. code-block:: none
    :pythontest: off

    Do homework
    Make death star fully armed and operational

.. note:: If you forget the newlines ``"\n"``, the file will look like this:

    .. code-block:: none
        :pythontest: off

        Do homeworkMake death star fully armed and operational

After writing, always remember to ``close`` the file, or the data may not be written fully.  This is why we always have to "Safely Remove" the USB Stick before we physically take it out of the Raspberry Pi computer - data may still be in the process of being written to one or more files.

Writing lists
-------------

To write a list of lines, like that produced by ``readlines``, we use ``writelines``::

    >>> f = open("todo.txt", 'w')
    >>> f.writelines(["Do homework\n",
                      "Make death star fully armed and operational\n"])
    >>> f.close()

Exercises
---------

1. Write a program called notes.py which repeatedly asks the user for a sentence, stores it in a variable (a string), and writes it out to file each time (a file called notes.txt for instance).  The loop will stop (break out) when the user types 'stop'.  Use a ``while`` loop to keep on asking the user for input, and the file ``write`` function to write the sentence to file.  At the end of the program, the file should contain each sentence, one after the other, each taking up a line by itself.

2. Modify the program in exercise 1 so that each line is prefixed by the line number, so the first sentence is output with "1. " added onto the beginning, with the second having "2. " added on at the beginning, and so on.

3. Write a program called cipher.py so that it reads in a sentence, but instead of writing the sentence to a file, it writes the ordinal value of each character instead.  To find out the ordinal value of a character, use the built-in ``ord`` function, passing in a single character at a time.  You only need to read in one sentence, but you will need to step over the sentence using a ``for`` loop.  To check your result, an input of "abcdef" should be stored in the file as "979899100101102" (i.e. the numbers from 97 for 'a', to 102 for 'f'), and an input of "ABCDEF" should be stored as "656667686970" (i.e. the numbers from 65 to 70).  Remember, the ``str`` function can take an integer and return a string in order for you to output it to file using the ``write`` function.

Things to remember
------------------

1. Use ``open`` with the ``'w'`` mode to open files for writing.

2. Use ``write`` to write a string to a file.

3. Use ``writelines`` to write a list of lines to a file.

4. Don't forget to call the ``close`` function on the file when you have finished.
