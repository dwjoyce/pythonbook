Walking along data
==================

Round and round
---------------

Python actually has two ways of repeating a block of code, something we call looping.  The first method which we have already covered is by using the ``while`` keyword.  The ``while`` statement includes a test (a boolean expression) that can change over time, thus affecting how many times the following block of code is run.  Effectively the block of code is repeated while that expression remains ``True``.  It stops repeating when the expression becomes ``False``.

For example, if we want to print out the numbers up to 10, then on the interactive shell we could do the following::

    >>> num = 0
    >>> while num < 10:
            print(num)
            num = num + 1

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
    
The test is whether the variable ``num`` is less than 10.  We initially set it to 0, and every time we repeat the block of code, we add 1 onto it, and give it the same name.  Eventually, it reaches 10, and the loop stops, as the variable ``num`` now equals 10, it is not less than 10.  Hopefully this is all very straightforward by now.

However, Python has an easier way of repeating a block of code a set number of times (10 in this example).  It is the ``for`` loop, and all it does is to step through a sequence such as a list.  We have been working with lists in the previous two chapters.

.. pythontest:: nooutput

So let's introduce this step by step.  First define a list and give it a name using the assignment operator::

    >>> numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
The name of the list is ``numbers``, and we have given it the same values as we printed out using the ``while`` loop above.

Now we use our new keyword ``for``.  We combine it with the ``in`` operator we first saw in chapter 15 on working out whether a value is a member of a list, but this time it is used to step along each item *in* the list.  To see it in action, type this in and make you you get the same result as when we used the ``while`` loop earlier::

    >>> for num in numbers:
            print(num)
        
And that is all we need to print out the numbers from the list we created.  We could combine those three lines into two like this, thus avoiding the need for defining the list variable::

    >>> for num in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(num)

To explain what is going on - the ``for`` keyword is telling Python that *for each* item (which we have called ``num``) in the list provided, then execute this block of code.  It is simply a way of stepping over a list, one item at a time.

To put it another way, you are asking for each item in the list, which Python passes to your program in the variable name provided, and repeats the code until the list runs out.

Ranges
------

However, it is a bit of a chore to have to type out the contents of our lists all the time.  Typing in ten numbers is one thing.  What if we wanted to have a list with a 1,000 numbers?  Or a million?  Not only would this be very time consuming (and also make our programs very long), it would also be rather error prone.  Think about typing in a few thousand numbers, and then make a mistake somewhere in the middle!

It is useful then that Python provides a function to give us a list of numbers in just the way we ask for.  It is called ``range``, and given its name, it simply provides a range of numbers as a list of integers.  Let's do the above program again using this ``range`` function::

    >>> for num in range(10):
            print(num)
    
Even shorter than before, now that we are using the ``range`` function to do the work for us.  Usually, it just take one argument - the number of integers that you want.  If you pass in ``5``, you get back ``[0, 1, 2, 3, 4]``, that is, 5 numbers starting with 0.  If you pass in ``1000``, you get a list of a 1000 numbers, from 0 to 999.

.. note:: In programming, we like to start from 0 and not from 1, just like when indexing lists.  A list called ``numbers``, the first item is referenced by an index offset from the beginning, so ``numbers[0]`` is 0 items from the beginning, so is the first item.  ``numbers[1]`` is the first item from the start, so is the second item, and so on.

If you don't want to start from 0, then you need to pass in two numbers - a start point and an end point.  For example, if you want the numbers between 100 and 200, you simply ask for ``range(100, 200)``; for numbers between -100 and 50, you ask for ``range(-100, 50)``.

The third thing you can do is to ask for a step in the numbers, so instead of each number going up by 1, you can go up by a different amount.  This is achieved by using a third argument, the ``step``.  For example, type this in the interactive shell to print out all the even numbers from 100 to 200::

    >>> for num in range(100, 200, 2):
            print(num)

Using the *step*, you can also obtain a list that counts down rather than counting up.  All the number ranges we have done so far have counted up.  To count down, you need to use a negative step.  However, you must also remember to make the end point lower than the start point!  Try this to count down from 10 to 1, inclusive::

    >>> for num in range(10, 0, -1):
            print(num)

The variable used to step through the list can be called anything you like.  It is a little different to how we have defined variables up until now which is by using the assignment operator::

    >>> num = 10
    >>> number = 20
    >>> my_int = 123
    
The ``for`` loop defines its loop variable as part of the ``for`` statement, but just like with ordinary variable, we can call it what we want to::

    >>> for item in range(10):
            print(item)
    
    >>> for counter in range(100):
            print(counter)
        
And you don't need to use it all, of course.  It is used to just step through the list - what you do with it is up to you::

    >>> for num in range(10):
           print('Going round and round 10 times!')
           print('Weeeeee!')
           
    >>> for line in range(1000):
            print('I will not draw on the classroom wall again.')

The list that the for loop uses to step over need not be a list of numbers.  It can be a list containing anything you like.  Try this::

    >>> names = ['Bilbo', 'Gandalf', 'Thorin', 'Golum']
    >>> for name in names:
            print('Enjoy your adventure', name)
        
    >>> sentence = 'Mary had a litle lamb'
    >>> for word in sentence.split():
            print(word)
        
And finally, the variable to step along need not be a list - it can be any sequence at all, including strings::

    >>> word = 'rotavator'
    >>> for letter in word:
            print(letter)

.. pythontest:: all

Again, as in chapter 15 on grouping, whatever you can place in a list variable, you can use the ``for`` loop to step over and work with the block of code you provide.

Drawing
-------

Let's put this knowledge to use to draw a shape using turtle.  Open a new file window and type in the following::

    import turtle

    # Create our window to draw in
    turtle.Turtle()

    # Set colour and start shape
    turtle.fillcolor('red')
    turtle.begin_fill()

    # Draw octagon
    for side in range(8):
        turtle.forward(50)
        turtle.left(45)
    
    turtle.end_fill()

A bit of explanation: we import the turtle module so that we can use it in our program; we then created the canvas to draw on by calling the ``Turtle`` function; we then set the filling colour as red and start the fill operation; we then loop round 8 times using the ``for`` keyword by going forward 50 pixels and turning left 45 degrees each time; we end by ending our fill operation so that the shape is filled in red.

This is now much easier than before than either using a sequence of statements, or even when we were using ``while`` loops.

Vertico
-------

Open up another new file window, and type in the following::

        
    import turtle
    import random

    # Define the colours we will use below
    colors = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow']

    turtle.Turtle()

    # Set the pen size, colour and drawing speed
    turtle.pensize(2)
    turtle.pencolor('red')
    turtle.speed('fastest')

    # Start with a length of 5, and increase as we draw
    length = 5

    # Draw 300 lines, changing the color and length as we progress
    for i in range(300):
        new_color = random.choice(colors)
        turtle.pencolor(new_color)
        turtle.forward(length)
        turtle.right(91)
        length = length + 2

Run and save it as spirals.py, and see what happens.  If there any problems, then check your code carefully!

A bit of explanation: we impor the modules we need, turtle for drawing, random to introduce a bit of variaton.  We then define the colours (note, English spelling - Python requires the American splling) we are going to use.  We then create our drawing window, changing the speed (so it doesn't take so long) and the pen size as well.  We start with a line length of 5, which is increased for each line so the shape moves outwards.  We then use a ``for`` loop to step along the range of numbers, from 0 to 299 (300 in total).  Inside the block of code that we are repeating (the loop), we change the pen colour, move forward, change the angle (a little more than 90 degrees) and increase the length.  We then repeat.  The lines are drawn longer and longer, at an increasingly skewed angle.

Try changing the numbers to see what happens to the final result.
        
Exercises
---------

1. In the interactive shell, write a ``for`` loop that counts from 1000 to 2000 in steps of 50.

2. In the interactive shell, write a ``for`` loop that counts from 100 to 0 in steps of -5.

3. Write a program called sides.py which uses the ``turtle`` module to draw a polygon having the number of sides the user has input.  Use a ``for`` loop to draw the sides of the polygon.  This is similar to the exercise in chapter 12, but this time the looping is different.

4. Write a program called brekkie.py which creates an empty list called breakfast (using the notation ``breakfast = []`` to create an empty list).  Ask the user what they had for breakfast, one item at a time, and call ``append`` for each item to append it to the breakfast list.  Use a ``while`` loop to accomplish this, allowing the user to type 'stop' to break out of the loop.  Then use a ``for`` loop to print out each item in the breakfast list, printing out how yummy each item is.

Things to remember
------------------

1. Use the ``for`` loop to repeat a block of code a set number of times.  Use the ``while`` loop to repeat a block of code an unknown number of times (e.g. depending on whatever the user types in).  The ``for`` keyword can be read as *for each* if that makes its easier to understand.

2. Use the ``range`` function to provide a sequence of number to step through.  You can use it with just one argument, the end point, or with two, the start and end point, or three arguments, start, end and step.
