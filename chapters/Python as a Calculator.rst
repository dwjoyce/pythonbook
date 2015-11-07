Python as a Calculator
======================

.. quote::
    :author: All programmers

    There, it should work now.

First steps (or sums)
---------------------

Let us start our journey by taking inspiration from something we all know well - your pocket calculator.

.. highlight:: none
.. pythontest:: off

To perform a sum on a calculator, such as 10 plus 20, you could simply hit the following buttons::

    10 + 20

and then hit the = (equals) button.  The result, 30, will then appear on your screen.  We could do other operations as well, such as subtraction, division and multiplication, like so::

    10 + 20 - 4 ÷ 2 × 3

and then finally hitting the equals button, you will get a result of 24 displayed on the calculator's screen.  This is assuming you are using a proper calculator, not a simple one which performs the calculation as it goes along, one step at a time!  In other words, it performs the division first, then the multiplication, and then subtracts this answer from the result of the addition.

So given their name, we should be able to use *computers* to do some *computing*, that is, working with numbers.  Particularly, we should be able to use our new programming language, Python, to do this for us.

Using the first example, the Python code is very simple.

.. highlight:: py3con
.. pythontest:: on

Bring up your Python interactive shell, as described in chapter 0 (i.e. by clicking on the IDLE icon on your desktop), and type the following::

    >>> 10 + 20
    30

and press the Return or Enter key on your keyboard.  The ``>>>`` (chevrons) appear automatically, so do not type these!  You should see the number 30 displayed below the line you typed, as in the example above.

How about the second example?  Let us try this::

    >>> 10 + 20 - 4 / 2 * 3
    24.0
    
The answer is the same as with our calculator example above.  However, what are these ``/`` and ``*`` symbols?  Well, the ``÷`` doesn't actually appear on your computer keyboard, so we use another symbol ``/`` (forward slash) instead.  And the ``×`` is too much like the letter ``x``, so we use the asterisk ``*`` symbol instead.  These *signs* or symbols in computer programming are called :term:`operators`, and we have leant four so far - ``+`` (addition), ``-`` (subtraction), ``*`` (multiplication) and ``/`` (division).

Type in it, press Return and see what the result is.  The result should read 24.0, the same as when we were using the calculator earlier.  This is not a whole number, but a fractional number - it has a decimal point included.  In Python, we will deal with two :term:`types` of numbers - whole numbers (:term:`integers`) and fractional numbers (:term:`floating point` or real numbers).

Remember, like in mathematics, a computer language does not work out the sum from left to right - it gives priority or precedence - to some operations over others.  It actually performs the division first (4 divided by 2, equalling 2), then the multiplication (2 times 3, equalling 6), then the addition (10 plus 20 equalling 30) and finally the subtraction (30 minus 6 equalling 24).  To see the full list of operator precedence - which operator is processed before others - then refer to appendix C on Operators.

To enforce a different order, you can use brackets.  Just like in Maths.  Put a pair of brackets around each part of the sum you want done separately.  So if you wanted to do the addition and subtraction section first, then type the following::

    >>> (10 + 20 - 4) / 2 * 3
    39.0
    
In programming, this way of expressing a value to form a result is called an expression.

Operator overload
-----------------

On your calculator there are more than 4 buttons to do things.  There is one labelled x\ :superscript:`2`\ . And x\ :superscript:`3`\ .  Python has this built-in as well and it is the ``**`` (power) operator.  For example, the number 9 to the power of 2 is as simple as::

    >>> 9 ** 2
    81

Which is 81. 2 to the power of 3 is::

    >>> 2 ** 3
    8

Which is 8. This works for any power.  How about working out large numbers, such as 19\ :superscript:`8`.  To do this, type in the following::

    >>> 19 ** 8
    16983563041


Your answer should state 16983563041. Negative numbers work as well to give fractional numbers less than 1.0.  Remember that 2\ :superscript:`-1` is the same as 1 ÷ 2?  Doing this in Python is similar::

    >>> 2 ** -1
    0.5

Your answer should read 0.5.

We can now move onto something your calculator cannot do.  Remember when you were in primary school, and you learnt that 7 divided by 3 was 2 remainder 1 (or to put it another way, 7 ÷ 3 = 2 r 1)? Python took that class too. To get the quotient (in this case 2), use the ``//`` (floor or :term:`integer division`) operator::

    >>> 7 // 3
    2

Which should be 2. And for the remainder, use the ``%`` (:term:`modulus`) operator::

    >>> 7 % 3
    1

Resulting in 1.  Reading both answers together, we have got 2 remainder 1.

Exercises
---------

#. Type the Python line to work out 3 plus 5 divided by 2.

#. Type the Python line to work out 4 times 2 minus 7.

#. To convert from Celsius to Fahrenheit temperature, you multiply the Celsius by 9 divided by 5, and add 32.  If the Celsius is 40, what is the Fahrenheit reading?

#. Type the Python line to work out 7 to the power of 6.

#. Type the Python lines to work out the quotient and remainder of 11 divided by 4.

Things to remember
------------------

#. Remember your arithmetic operators:

   ======================================  ========
   Name                                    Operator    
   ======================================  ========
   Addition                                ``+``
   Subtraction                             ``-``
   Division                                ``/``
   Multiplication                          ``*``
   Power                                   ``**``
   Floor division (Whole number division)  ``//``
   Modulus (remainder)                     ``%``
   ======================================  ========
   
   See Appendix C for a full list of operators, over and above arithmetic.

#. Use brackets to force Python to do a calculation in a particular order

#. Whole numbers are referred to as integers, fractional numbers are referred to as floats.

#. In programming, values are known as :term:`expressions`, potentially made up of values, operators and even other expressions that need to be evaluated to form a result.  They express a value.
