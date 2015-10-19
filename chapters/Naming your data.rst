Naming your data
================

.. quote:: Emo Philips

    A computer once beat me at chess, but it was no match for me at kick boxing.

Saving and recalling
--------------------

Remember in the last chapter we looked at how your calculator works and started using the Python programming language to copy and build on this.

One feature of a calculator is the Memory button, usually marked by the letter **M**.  This allows you to store a number, add onto or subtract from it, and recall it later for use in a new calculation.  It effectively makes the calculator remember a number for you, so that you do not have to.

All programming languages, including Python, have a similar feature. Instead of having a memory button, Python has :term:`variables`.  It is really just a way of putting a name against the data (e.g. a number) you are working with, giving your program the ability to store data, change it (i.e. vary its value), and recall it later.

For example, the initial sum we worked on in the previous chapter::

  >>> 10 + 20
  30
  
Python will evaluate this sum, give you the result, but it will not save it anywhere.  It effectively throws the answer away.

How can we save the result in memory?

Similar, to a calculator, we can store it in a variable called ``M``::

  >>> M = 10 + 20

What this does is take the integer values 10 and 20, with the addition operator it adds them together and then assigns them, using the assignment operator = (equals), to the variable name ``M``.

.. note:: In Python, variables names are like labels attached to boxes which contain the data.  If you give a present to someone (e.g. at Christmas), the label is the name to which the present is being given, with the box containing the present.  In Python, the label is the variable name, the box contains the data, e.g. an integer number.

We can then recall the value stored against this name later.  For example::

  >>> M + 5
  35
  
You will see it gives an answer of 35.  The variable name ``M`` refers to 30 (from the addition of 10 and 20 above), and then we are adding a further 5 to it, giving 35.

If we now try::

  >>> M + 10
  40
  
You will notice it results in 40.  It does not take the previous result of 35 and add on 10, as we did not store that back into ``M``, but simply recalled the value of ``M`` and used it as before.

To change the value of ``M``, we have to put it back on the left hand side of the assignment operator::

  >>> M = M + 10

This changes ``M`` once more, using it on the right (recalling ``M``, being 30, and adding on 10), and putting that back into the variable name ``M``.  We are effectively reusing the same name, or giving it a new value.

To see what the new value of ``M`` is, just type ``M``::

  >>> M
  40
  
This gives 40, as expected (30 plus 10, as above).

More and more
-------------

Your calculator will have just the one memory to store numbers, but in a Python program, you have have any number of variables in your program.  And they do not have to be called ``M`` either!  In fact, if you want to store your data separately, you need different names for each value.

For example::

  >>> M1 = 5
  >>> M2 = 10
  >>> M3 = 15

Try this, so one variable makes use of two others::

  >>> a = 10
  >>> b = 20
  >>> c = a + b
  >>> c
  30
  
And this::

  >>> first_num = 123
  >>> second_num = 456
  >>> third_num = first_num * second_num
  >>> third_num
  56088
  
And arithmetic operators can be used that we learnt in our previous chapter::

  >>> A1 = 10 + 20
  >>> B2 = A1 - 4
  >>> C3 = B2 / 2 * 3
  >>> C3 + A1
  69.0

That last line displays the value of ``C3``, calculated from the value of ``B2``, and adds on the value of ``A1``.

You can name your variables with any combination of letters and numbers along with the ``_`` (underscore, not minus sign) character, as long as the name does not start with a number. You can use the underscore to separate words if you use them in your variable names - spaces are not allowed inside names!

Exercises
---------

1. Define a variable called ``age`` and set it to your age (use an integer number).

2. Use your ``age`` variable to calculate how many days old you are (assume each year has 365 days).

3. Again, use your ``age`` variable to calculate in what year you will be 100 years old.  You will need to take the value of ``age`` from the present year, 2015, and then add on 100.

Things to remember
------------------

1. You define a variable by giving it a name, and using the assignment operator to give it a value.  The value can be evaluated (calculated) from other variables.

2. Begin your variable names with a letter from the alphabet (upper or lowercase) or the ``_`` (underscore) character.  To use the underscore character, you need to press the Shift key down whilst pressing the key to the right of the 0 (zero).

3. Use the ``_`` (underscore) character to divide up words in your variable names to make them more readable, e.g. ``first_num``.
