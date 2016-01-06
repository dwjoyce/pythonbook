Going loopy
===========

.. quote::
    :author: Anonymous

    Q. How did the programmer die in the shower?
    A. He read the shampoo bottle instructions: Lather. Rinse. Repeat.

Computers are very good at doing a number of steps repetitively, relieving us of many mundane tasks in our lives.  In programming, this makes our programs much more flexible and involves a lot less typing which is always a good thing!

Imagine drawing a hexagon (a 6 sided polygon) using turtle.  There is the hard way, and the easy way.

Doing it the hard way
---------------------

With what we have learned up until now, we would do the following.  So open a new file window, and this in::

    import turtle

    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)
    turtle.forward(100)
    turtle.left(60)

Run it - calling the program :file:`hexagon.py` - and check that it draws a hexagon in the turtle window.  Don't forget to make that call of the ``Turtle`` function with an initial capital letter!

This program is 14 lines long (not including the blank lines), with 12 of those lines just to draw the hexagon.  Not a great return!

Clearly, this is too much typing for what it does.  Imagine the typing involved in drawing a 100 sided polygon!  There are also cases where this kind of sequential programming (i.e. programming that executes - or performs - each line, one after another) simply cannot do what we want.  If you do not know in advance how many times to do a particular task, then you cannot do it sequentially.  For example, if the program is adding up a series of numbers, one after the other, and is relying on the user to press the ``=`` equals sign at the end (or perhaps typing "stop" in a programming context), then the program cannot calculate in advance how times to repeat the code to input the next number.  We have to find a different way.

Doing it the easy way
---------------------

To overcome this hurdle, Python - and pretty much every other programming language - has the ability to repeat a block of code a number of times.  This is called looping or :term:`iteration`.

Roughly speaking, looping is similar to the way we construct ``if`` statements.  In an ``if`` statement, we use the ``if`` keyword (a :term:`keyword` is a word reserved by Python and given a special meaning), following by a test which results in a boolean value - either ``True`` or ``False``.  It will then conditionally execute a given code block, which follows the ``:`` colon symbol.  If the test fails (results in a value of ``False``), then the code block is skipped.  Either way, the program continues on its way after the ``if``, along with any ``elif`` and ``else`` statements are done.

A loop uses a different keyword, but still has a condition that is tested, and also a code block that belongs to it.  The main difference is that a loop will execute the code block not just once, but potentially many times.  To be precise, the code block can execute zero or more times, depending on whether the test at the top of the loop is ``True`` in the first place!  The loop will repeat whilst the condition remains ``True``, so clearly we need a way of changing the condition as we go along or otherwise it will repeat forever.  In the next chapter, we will do this on purpose, but with a way of escaping!

Enough talking - let us go about changing our program above to get the computer to do more of the work!  Add the following lines onto your program (do not bother modifying your existing code, as it will be a good point of comparison)::

    side = 0
    while side < 6:
        turtle.forward(100)
        turtle.left(60)
        side = side + 1

Run your program, again saving it onto your USB stick, and see what it does.  It should now draw the same hexagon twice!

The new thing to learn here is the use of the new keyword ``while``.  With this, the program performs the indented block of code, following the ``:`` symbol, *while* the condition is true.  Initially, the condition is ``True``, as we have set an integer variable to zero, and zero is less than 6.  Each time we draw a side of the hexagon, we add (:term:`increment`) one onto the side variable.  So the variable side goes from 0 to 1 to 2, 3, 4, 5 and finally 6.  We then test whether the value 6 is less than 6, which it is not - it is equal to 6.  Therefore, the condition is then ``False``, and the loop stops.

You can see we have reduced 12 lines to draw a hexagon, down to 5.  The great thing is that if we change the condition from 6 to 100 (and changing the angle of turning left would be good too, as well as the length of each side), then we would then draw a 100 sided shape without any further changes.  In the hard way above, this would involve another 188 lines of code!

Exercises
---------

#. Write a program called :file:`hundred.py` that prints out the numbers from 0 to 100, inclusive.

#. Modify your :file:`hundred.py` program so that after counting up to a 100, it then counts down from 100 to 0, printing as it goes.

#. Modify your :file:`hundred.py` program so that the loops count up or down in steps of 5, not 1.  Run it again to check that it works as expected.

#. Write a program using the ``turtle`` module that asks the user how many sides to draw, converts it into an integer, and then uses turtle to draw a shape with that number of sides.  You will have to work out the angle by dividing 360 degrees by the number of sides when turning the turtle to the left or right.

Things to remember
------------------

#. Use the ``while`` keyword to repeat a block of code.

#. The condition used after the ``while`` keyword is just like when using an ``if`` statement - a boolean expression.  It can use any of the arithmetic and logical operators.

#. The code block to be repeated can contain 1 or many lines of code.  It all depends on what you want to do.  It can even contain other loops nested within the outer loop.
