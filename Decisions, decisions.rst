Decisions, decisions
====================

Differing ways of comparing
---------------------------

In the previous chapter, we introduced the ``if`` statement, which evaluates a test, and if true, it runs the statements which have been indented to the right following the colon ``:`` symbol.  We call this group of statements indented to the right a *block of code*.

We also introduced our first comparison operator, the equals sign ``==``.  There are many more, most of which you will recognise from your mathematics material.  We list the possibilities at the end of this chapter, but here are some highlights.

We will use the interactive shell to experiment for a while.  Type the following for practice::

    >>> a = 10
    >>> b = 20
    >>> a == b
    >>> a != b
    >>> a < b
    >>> a <= b
    >>> a > b
    >>> a >= b
    
The first two lines create our variables, ``a`` and ``b``, using the assignment operator (not a comparison operator).  The next six lines demonstrate the different comparison operators, one by one.  The only one that really requires explanation is the second one, the not equal to operator ``!=``.  In maths, you would use a different symbol, such as this one: :math:`\neq`.  Since this symbol is not readily available on the average computer keyboard, we use the exclamation mark in front of the equals sign, to make the not equals operator ``!=``.  The other symbols are also separated, so in maths you could use the :math:`\geq` symbol, in programming, we expand it into ``>=``, thus taking up two symbols to mean the same.  Similarly with :math:`\leq` being turned into ``<=``.

.. note:: We call these expressions, as they express a value once properly evaluated by the computer.  Normally, one value is on the left, and another on the right, with the operator in the middle.  Each of these operators can be used with other types of data than just integer numbers - floats and strings could also be used, e.g. ``2.5 > 1.2`` and ``"fred" != "harry"``.

You will also notice that the result of each expression is either True or False.  This is our fourth type of data, and it is the simplest of all - they are either True or False.  They cannot be any other value.  This is the equivalent of on or off, 1 or 0, up or down.  There is no in between value, it is one or the other.  For example, above we tested whether 10 was equal to 20 (``a == b``) - this is either True or it is False (obviously the latter).  It cannot be something else, or both!

Booleans are very useful, and you can set variables to boolean values as well.  We will see more of this in the next chapter.

More than one possibility
-------------------------

Testing just with the ``if`` statement is very useful, but Python does offer more flexibility than just this.  For example, if we want to write a program that inputs two numbers, and prints out the largest number, we could do the following.  So open up a new file window, and type the following::

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

Many, many possibilities!
-------------------------

What if we had more than two possibilities - doing one things for the main test, and another thing for everything else?  Python has you covered for this eventuality as well - a combination of the ``if`` and the ``else`` put together to form the ``elif`` - short for *else if*.

The ``elif`` statement sits after the ``if`` (so there must always be an ``if`` statement first), and there can be as many ``elif`` statements as you need.  Each one has an expression to evaluate, and if true, then the ``elif`` code block is run.

For example, modify your ``if`` and ``else`` statement in your nums.py program above, so that it now states the following::

    if num1 > num2:
        print('The largest number is:', num1)
    elif num1 == num2:
        print('The numbers are the same!')
    else:
        print('The largest number is:', num2)

We introduced the middle two lines, the ``elif`` followed by the call to the ``print`` function.  What this does is test the ``elif`` condition only if the test for the ``if`` fails.  If the ``elif`` test succeeds (it is true), then the line - or lines - under the ``elif`` statement are run.

A bit more practice
-------------------

Combining what we have learned in this chapter, let us write another program called noises.py.  Start it in the usual method of clicking on the ``File`` menu and selecting ``New File``.  Once the new blank window has appeared, type in the following::

    animal = input('What animal do you have there with you? ')
    if animal == 'cow':
        print('Moo!')
    elif animal == 'sheep':
        print('Baa!')
    elif animal == 'pig':
        print('Oink!')
    elif animal == 'horse':
        print('Neigh!')
    elif animal == 'chicken':
        print('Cluck!')
    elif animal == 'duck':
        print('Quack!')
    elif animal == 'dog':
        print('Woof')
    elif animal == 'cat':
        print('Meow!')
    elif animal == 'dinosaur':
        print('Roar!')
    else:
        print('Sorry, I don\'t recognise that animal!')

Obviously, we could go on and on!  Save it using the ``F5`` key, name it noises.py making sure you save it onto your USB stick, and run it.  You need to run it several times in order to test all the possibilities (i.e. see all the noise words being printed out).

As you can see, the ``if`` statement is tested first.  If the test evaluates to true, then the first optional block of code is run (printing out 'Moo!'), and it will then jump to the end (past the ``else``).  Otherwise, it will test each test in turn, only running the code blocks if the test is true.  Otherwise, it will eventually drop down to the ``else`` statement, and run the last block of code, but only if all the other tests have failed.


Exercises
---------

1. Modify your kiosk.py program you wrote for the previous chapter so that instead of using lots of ``if`` statements, you use one ``if`` statement, followed by a number of ``elif`` statement.  The ``else`` statement should be used to print out a message telling the user that he has not entered a valid choice.

2. Write a program called move.py, and ask the user the form of transport, either a plane, car, bicycle or walking.  Depending on what they have entered, print out 'fast', 'quick', 'steady' or 'slow'.

3. Write a program that uses the ``turtle`` module called shapes.py.  Ask the user what shape to draw, e.g. circle, square or star.  Depending on what the user has entered, draw the appropriate shape.  If the user didn't type in anything sensible, then print out an error message.


+Things to remember
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
   
2. We now know four types of data - integer, floats, strings and booleans.  Boolean values are either ``True`` or ``False``.

3. Each selection statement must contain an ``if`` statement, along with a test to evaluate and at least one line of code to run, indented to the right.  If the test is evaluated to true, then even if there are ``elif`` or ``else `` statements below, the program will skip them all.

4. You can optionally include one or more ``elif`` statements, each with their own tests to evaluate and their own blocks of code.  If more than one of these evaluated to true, then the first one is run, and the other skipped.

5. Finally, you can also optionally include an ``else`` statement, without any test, but with its own block of code to run.  This block of code is only run if the ``if`` and ``elif`` tests all fail (i.e. are all false).
