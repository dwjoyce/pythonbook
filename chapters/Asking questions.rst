Asking questions
================

.. quote::
    :author: Homer Simpson
    :source: In response to the message, "Press any key"

    Where is the :button:`any` key?”

String input
------------

It is now time to make our programs more interactive, allowing the user to get involved whilst the program is running.  Up until now, Python has carried out our instructions, one line at a time, with the program doing exactly the same thing every time.

In this chapter, we will allow the user to affect what happens in the program with the opportunity to enter data of their own.  The way Python allows the user to enter data is by using the ``input`` function.  This reads in what the user is typing on the keyboard, and returns the value to the program as a string so that it can be stored or used elsewhere.

Begin by creating a new program (:menu:`File -> New File`), and type the following::

    name = input('What is your name? ')
    print('Hello there', name)
    
Press :kbd:`F5` to run your program, and give it the name :file:`hello.py`.  You will notice the program pauses at the first line - it is waiting for your input.  Use the keyboard to type in your name, and press the :button:`Return` or :button:`Enter` key.  You may have to click on the interactive window used to run your program with your mouse to make it active.  Whatever you typed in will be stored in the variable ``name``.  This variable is then used in the second line to print out a message along with the value referred to by the variable ``name``.

Note that we are using a message (a :term:`string` value) when calling the ``input`` function - this is the message that is presented to the user when you are asking for input.  This is not essential - you could miss it out, but then the user may not know they are expected to type something.  It is best to present the message, so they know what to do next.

Using numbers
-------------

The type of data given to us by the ``input`` function (i.e. its return value) is always a string.

Remember, when you *add* two strings, you are really joining them together or :term:`concatenating` them (e.g. ``"12" + "34"`` would equal ``"1234"``).  When you *multiply* a string by a number, you are :term:`repeating` the contents of the string (e.g. ``"123" * 3`` would equal ``"123123123"``).

Therefore, if you need to use the input as an actual number, you need to convert it from a string type to an integer or float type.  This means you can then use the result in a normal calculation like any other number.  It is effectively converts a sequence of digits into a proper number where the right most digit is the 1s, the second column is the 10s, the third column is the 100s, etc., with all the numbers combined together to form a complete number.

.. note:: Each character of a string is actually encoded according to a table of numbers (a character set).  One common character set is :term:`ASCII` (American Standard Code for Information Interchange), which includes all the Latin characters, digits and common symbols.  Another is :term:`Unicode`, which includes characters from many other languages.  These character sets encode the letter 'A' as the number 65, the digit '0' as 48, and the symbol "!" as 33.  This demonstrates how text is stored inside computer systems.

To convert from a string to an integer, you use the ``int`` function.  So for example, ``int("123")`` would return the actual number ``123``.

To convert from a string to a floating point number, you use the ``float`` function.  So for example, ``float("123")`` would return the actual number ``123.0``.

To convert back from a number (whether integer or float) into a string, you use the ``str`` function.  So for example, ``str(123)`` would return ``"123"``, and ``str(123.0)`` would return ``"123.0"``.

To appreciate what is involved in converting a string of digits into an integer using the ``int`` function, look at the following diagram to see how Python multiplies the place values, and adds them all together:

.. image:: /images/intconversion.pdf
    :width: 350 pt
    :align: center

To practice, start a new program called :file:`sumup.py`, and type in the following into your new window::

    first_num_str = input('First number: ')
    second_num_str = input('Second number: ')
    
    first_num = int(first_num_str)
    second_num = int(second_num_str)
    
    total = first_num + second_num
    
    print('The sum of those two numbers is', total)

Press :kbd:`F5` to run it, confirm to save, and name your program :file:`sumup.py`.  Careful when entering those numbers - they must be integers, otherwise converting from a string to an integer in the program will not work!

To explain what is going on, we first input what the user has typed in, and save it in a variable called ``first_num_str``.  We do the same again for ``second_num_str``.  We then convert this input from a string value to an integer value so that we can perform a proper numerical addition operation.  We do this addition with the line where we assign a new variable called ``total`` to ``first_num`` added onto ``second_num``.  We finish by printing out a message, printing the value of total alongside.

Run your program again with different numbers to check it works.  Now run it, and instead of entering integer numbers (e.g. ``10``, ``20``, ``-50``, ``123``, etc.), type in a fractional number (e.g. ``10.75``).  This should result in an error, as the period ``.`` is not part of an integer number.  Python will not like this!

To correct this, let us finally modify your program to change the calls to the ``int`` function, so that they call the ``float`` function instead, as follows::

    first_num_str = input('First number: ')
    second_num_str = input('Second number: ')
    
    first_num = float(first_num_str)
    second_num = float(second_num_str)
    
    total = first_num + second_num
    
    print('The sum of those two numbers is', total)

Now try entering fractional numbers, and it should handle them quite happily.

Exercises
---------

#. Ask the user's name.  Print it out a 100 times.

#. Ask the user's name and a number.  Print out the name that number of times.  You will need to convert the number string to an integer using the ``int`` function before repeating the name string.

#. Ask for a day between 10 and 20.  Print it out with the letters "th" appended onto the day, as with a date.  So if the user entered 10, print out ``10th``; if the user entered 18, print out ``18th``.  There is no need to convert the number to an integer - use the addition operator ``+`` to simply join the data input and the letters "th" together.

#. Expand on the :file:`sumup.py` program we did in the chapter so that it also prints out the second number subtracted from the first (i.e. the first minus the second), the first divided by the second, and both numbers multiplied together.

Things to remember
------------------

#. Use the ``input`` function to read input from the keyboard.  You can store this in a variable by putting the variable name and the assignment operator to the left hand side of the call to input.  Moreover, you can optionally include a message (a string) to present to the user when the program pauses for input.

#. To convert to an :term:`integer`, use the ``int`` function.

#. To convert to a :term:`float`, use the ``float`` function.

#. To convert to a :term:`string`, use the ``str`` function.
