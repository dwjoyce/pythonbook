Decisions, decisions
====================

Differing ways of comparing
---------------------------

In the previous chapter, we introduced the ``if`` statement, which evaluates a test, and if true, it runs the statements which have been indented to the right following the colon ``:`` symbol.  We call this group of statements indented to the right a *block of code*.

We also introduced our first comparison operator, the equals sign ``==``.  There are many more, most of which you will recognise from your mathematics material.  We list the possibilities at the end of this chapter, but here are some highlights.

We will use the interactive shell to experiement for a while.  Type the following for practice::

    >>> a = 10
    >>> b = 20
    >>> a == b
    >>> a != b
    >>> a < b
    >>> a <= b
    >>> a > b
    >>> a >= b
    
The first two lines create our variables, ``a`` and ``b``, using the assignement operator (not a comparison operator).  The next six lines demonstrate the different comparison operators, one by one.  The only one that really requires explanation is the second one, the not equal to operator ``!=``.  In maths, you would use a different symbol, such as this one: ``≠``.  Since this symbol is not readily available on the average computer keyboard, we use the explanation mark infront of the equals sign, to make the not equals operator ``!=``.  The other symbols are also separated, so in maths you could use the ``≥`` symbol, in programming, we expand it into ``>=``, thus taking up two symbols to mean the same.  Similarly with ``≤`` being turned into ``<=``.

**Note:** we call these expressions, as they express a value once properly evaluated by the computer.  Normally, one value is on the left, and another on the right, with the operator in the middle.  Each of these operators can be used with other types of data than just integer numbers - floats and strings could also be used, e.g. 2.5 > 1.2 and "fred" != "harry".

You will also notice that the result of each expression is either True or False.  This is our fourth type of data, and it is the simpliest of all - they are either True or False.  They cannot be any other value.  This is the equivelent of on or off, 1 or 0, up or down.  There is no inbetween value, it is one or the other.  For example, above we tested whether 10 was equal to 20 (``a == b``) - this is either True or it is False (obviously the latter).  It cannot be something else, or both!

Booleans are very useful, and you can set variables to boolean values as well.  We will see more of this in the next chapter.

More than one possibility
-------------------------

Testing just with the ``if`` statement is very useful, but Python does offer more flexability than just this.  For example, if we want to write a program that inputs two numbers, and prints out the largest number, we could do the following.  So open up a new file window, and type the following::

    num1_str = input('Enter your first number: ')
    num2_str = input('Enter your second number: ')
    
    num1 = int(num1_str)
    num2 = int(num2_str)
    
    if num1 > num2:
        print('The largest number is:', num1)
    if num2 > num1:
        print('The largest number is:', num2)
        
Run it with the ``F5`` key, and save it onto your USB stick with the name nums.py.

It should run fine, printing out the largest number of the two input by the user.  Note how we have to convert the inputs, entered as a sequence of digits, into integer numbers before we can use them in the comparisons.  Otherwise, the comparisons will not work correctly.

The problem is that we are doing the test twice, which is wasteful.  It is more efficient to do the test once, and do once block of code if the test was successful (i.e. it was true), and a different block of code if unsuccessful (i.e. the result was false).  This is where the ``else`` statement comes into play.  What is does it run a block of code if the ``if`` statement above it failed in all its tests.  To see this in action, change your last-but-one line to read as follows::

    if num1 > num2:
        print('The largest number is:', num1)
    else:
        print('The largest number is:', num2)

Don't forget those colon ``:`` symbols at the end of the lines above each new code block!  Remember, a block of code can be as little as a single statement, or hundreds of lines long.  It depends on what you want to do.

Now run your program again - it should exactly the same, but more efficiently (i.e. faster) this time.

Again, the ``else`` presents a block of code to be run if all of the tests in the ``if`` statement above it have failed.  It is like a safety net at the bottom of the ``if`` statement which takes care of everything if none of the tests are true.  Read the word *else* like the word *otherwise* if that helps - test this and do this if true, otherwise do this.

Exercises
---------

Things to remember
------------------

1. Remember your comparison operators:

   ======================================  ========
   Name                                    Operator    
   ======================================  ========
   Equals                                  ``==``
   Not equal to                            ``!=``
   Greater than                            ``>``
   Greater than or equal to                ``>=``
   Less than                               ``<``
   Less than or equal to                   ``<=``
   ======================================  ========
   
2. We now know four types of data - integer, floats, strings and booleans.  Boolean values are either True or False.
