Walking along data
==================

Round and round
---------------

Python actually has two ways of repeating a block of code, somethign we call looping.  The first method which we have already covered is by using the ``while`` keyword.  Put an expression alongside, which can change over time, and a block of code underneath.  The block of code is then repeated while that expression remains True (maybe not at all).

For example, if we want to print out the number up to 10, then on the interactive shell we could do the following::

    >>> num = 0
    >>> while num < 10:
    ...     print(num)
    ...     num = num + 1
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    
The test is whether the variable ``num`` is less than 10.  We initially set it to 0, and every time we repeat the block of code, we add 1 onto it, and give it the same name.  Eventually, it reaches 10, and the loop stops.  Hopefully all very straightforward.

However, Python has an easier way of repeating a block of code a set number of times (10 in this example).  It is the ``for`` loop, and all it does is to step through a sequence such as a list.  We have been working with lists in the previous two chapters.

So let's introduce this step by step.  First define a list and give it a name using hte assignment operator::

    >>> numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
The name of the list is ``numbers``, and we have given it the same values as we printed out using the ``while`` loop above.

Now we use our new keyword ``for``, along with the ``in`` operator we first saw in chapter 15 on working out whether a value is a member of a list::

    >>> for num in numbers:
    ...    print(num)
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
        
And that is all we need to print out the numbers from the list we created.

To explain what is going on - the ``for`` keyword is telling Python that *for each* item, which we have called ``num``, in the list provided, then execute this block of code.  It is simply a way of stepping over a list, one item at a time.

Ranges
------



Exercises
---------

1. Write a program called sides.py which uses the ``turtle`` module to draw a polygon having the number of sides the user has input.  Use a ``for`` loop to draw the sides of the polygon.  This is similar to the exercise in chapter 12, but this time the looping is different.

2. Write a program called brekkie.py which creates an empty list called breakfast (using the notation ``[]`` to create an empty list).  Ask the user what they had for breakfast, one item at a time, and ``append`` each item to the breakfast list.  Use a ``while`` loop to accomplish this, allowing the user to type 'stop' to break out of the loop.  Then use a ``for`` loop to print out each item in the breakfast list, printing out how yummy each item is.

Things to remember
------------------

1. Use the ``for`` loop to repeat a block of code a set number of times.  Use the ``while`` loop to repeat a block of code an unknown number of times (e.g. depending on whatever the user types in).  The *for* keyword can be read as *for each* if that makes its easier to understand.

2. Use the ``range`` function to provide a sequence of number to step through.
