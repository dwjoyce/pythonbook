Escaping the cycle
==================

.. quote:: Edsger Dijkstra

    If debugging is the process of removing software bugs, then programming must be the process of putting them in.

In the previous chapter we posed a problem that a sequential way of programming cannot solve - needing to repeat a block or set of instructions a number of times that is unknown in advance.  In other words, you have to repeat a set of statements, but you only know when to stop at the very end.  It is not possible to code this in a top-down or sequential way.  However, we can achieve this by using loops in our programs.

Breaking out
------------

Although we have introduced looping, we have only used it by counting from a starting number to an end number, and then stopping.  We really just want to repeat a block of code a certain number of times.  But what, like our problem above, you don't know when to stop until the end?

Remember that the test after the ``while`` keyword is just a boolean expression.  If it evaluates to a ``True`` value, then the loop should perform another cycle of its block of code.  It will then test the expression again to see if it has changed in the meantime.  So if we don't know when to stop, a good start is to make the loop go round and round indefinitely.  It is a called an :term:`infinite loop`, and - in theory at least - it goes round forever!  And to make an infinite loop, we simply make the boolean expression True by using the value ``True``.

To see this in action, start a new file window and type in the following:

.. code-block:: py3con
    :pythontest: compile

    while True:
        print('Help, I\'m stuck in a loop!')
        
Save it as adder.py, and see what happens.  It should keep printing out the *Help* message.  To stop the program, you need to press the ``Ctrl`` and ``C`` keys together - this breaks out of the loop.

Clearly, we need a better way of breaking out of the loop than relying on the user to do it for us.  This is where the ``break`` keyword comes in, combined with what we know already about the ``while`` loop and the ``if`` statement to make a selection.

Therefore, modify your adder.py program like so::

    while True:
        name = input('What is your name, or type stop to quit: ')
        if name == 'stop':
            break
        print('Hello there', name)
        
Save and run it again and see what happens.  Notice how the ``while`` statement is the same, but inside the loop it is very different.  The first line of the loop code block simply asks for the user's name, using the ``input`` function, and stores it in a variable called ``name``.  Then we do something new - we test whether the contents of the variable ``name`` is equal to the value 'stop' (which we have told the user to type in to quit the loop), and if so, we use the new keyword ``break`` to break out of the loop.  It simply jumps passed the end of the code block, attached to the ``while`` loop, to carry on with the rest of the program (if there was any).  If we didn't break out of the loop, then we print a message to the user, using the contents of the variable ``name`` as we do so.

We could also do this by using a boolean variable in a slightly different way::

    keep_going = True
    while keep_going:
        name = input('What is your name, or type stop to quit: ')
        if name == 'stop':
            keep_going = False
        else:
            print('Hello there', name)
            
It is slightly longer, but is a useful technique to use in certain situations.

Adding up
---------

Let us change our program a third time to finish with a program that will ask the user for one number at a time, adding them onto the total as it goes along.  The user can gain type 'stop' to break out of the loop, but this time, it will print out the total of the numbers at the end.

Therefore, modify your ``while`` loop to reflect the following::

    total = 0
    while True:
        num = input('Enter a number, or type stop to quit: ')
        if num == 'stop':
            break
        total = total + int(num)
    print('The grand total is:', total)

Notice how creating the variable of ``total`` with a value of 0 is outside of the ``while`` loop code block, as is the call to the ``print`` function at the end.  This is determined by those lines of code being aligned with the ``while`` statement, and not with the code block beneath the header of the loop.  The four middle lines form the code block which is repeated, potentially forever.  What stops the loop is the user typing the word 'stop' into the variable ``num``.  This then means the test belonging to the ``if`` statement is True, so the break is then run.  If the user does not type 'stop', then the number is converted into an integer using the ``int`` function, and added onto the running total.  The loop then repeats until the user does type 'stop', and then print function finally does its bit.

.. note:: The ``break`` keyword will break out of your present loop.  There is another keyword called ``continue`` which will stop executing the code block and continue the loop from the beginning again.  This is a way of skipping any remaining lines in the loop and starting the next loop cycle early.

Exercises
---------

1. Change your adding.py so tha the user types 'quit' instead of 'stop' to break out of the loop.

2. Write a program called words.py which inputs a word at a time, appends it onto a string (e.g. ``sentence = sentence + word``), and prints it out at the end.

3. Modify your polygon.py program from the previous chapter so that it keeps drawing polygons, one on top of the other, until the user types 'stop'.  Each time it will ask the user how  many sides to draw, just as before.

Things to remember
------------------

1. Use the value of ``True`` as the expression - or test - for the ``while`` loop to make it go on indefinitely, i.e. an infinite loop.

2. Use the keyword ``break`` to break out of the present loop.  If one loop is nested inside another and the break resides in the inner loop, it only breaks out of the inner loop, not the outer one as well.

3. The ``while`` loop is best used for this kind of looping - when you do not know when to stop until you have reached the end.
