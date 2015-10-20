Writing files
=============

.. quote::
    :author: Waseem Latif

    Give a man a program, frustrate him for a day.
    Teach a man to program, frustrate him for a lifetime.

Prepare your ink
----------------

The opposite to reading a file is writing to it. To write to a file, we first have to open it in writing mode. To do this, we pass the ``"w"`` to ``open``::

    >>> f = open("todo.txt", "w")

This will open the file, creating it if it does not exist. The file is then emptied or truncated, "cleaning the slate" for any data you will write.

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

After writing, always remember to ``close`` the file, or you data may not be written.

Writing lists
-------------

To write a list of lines, like that produced by ``readlines``, we use ``writelines``::

    >>> f = open("todo.txt", "w")
    >>> f.writelines(["Do homework\n",
                      "Make death star fully armed and operational\n"])
    >>> f.close()


Exercises
---------

.. todo:: Exercises for Writing files


Things to remember
------------------

1. Use ``open`` with the ``"w"`` mode to open files for writing.
2. Use ``write`` to write a string to a file.
3. Use ``writelines`` to write a list of lines to a file.
