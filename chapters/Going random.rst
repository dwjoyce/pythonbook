Going random
============

.. quote::
    :author: Robert R. Coveyou

    The generation of random numbers is too important to be left to chance.

A bit of variation
------------------

To add variation to our programs, we can ask the user for some input, and then behave differently depending on what the user has typed in.  But what if we wanted to play a game, with the game needing to change its behaviour from one run to the next?  If a game we played behaved exactly the same way every time, which computers tend to do, games soon become rather predictable!  A game of chess where the computer always started in the same way would never sell very well!

Computer programs which need a bit of variation are programs like flight simulators (where the weather differs from time to time), board games (so the moves vary from game to game), racing games (where your competitors do different things from race to race), and so on.  They do this by using a piece of software to provide them with some :term:`random` data, such as a simple number which varies between a range of numbers.  This simple piece of data is then used to vary the decisions made within the program, thus making the program more interesting to use.  In a way, it becomes a little more like the real world.

That's random
-------------

Python does this by using the ``random`` module.  We will get to know this by first using the interactive interpreter - bring this onto your screen, and you can then import the ``random`` module in a similar fashion to importing the ``turtle`` module::

    >>> import random

.. pythontest:: run

We can list what functions the random module offers by using the ``dir`` function::

    >>> dir(random)

We can then experiment with some of its functions.  Try calling the ``random`` module's ``random`` function (random module, random function), a few times::

    >>> random.random()
    >>> random.random()
    >>> random.random()
    
.. note:: You can repeat a command in the interactive interpreter by using the up arrow key on your keyboard, and pressing the :button:`Return` or :button:`Enter` key.  This brings the statement down onto your current line, allowing you change it.  Execute that statement by pressing the :button:`Return` or :button:`Enter` key again.

Run this line a few time with the note above.  See how it always returns a number that is between 0.0 and 1.0, but hardly ever the same exact number.  See if you can get it to repeat a number - it is not easy!

In fact, let's use our new found knowledge on looping to see how this random number changes every time you ask for it.  So type the following into the interactive interpreter:

.. code::
    :pythontest: compile

    while True:
        random.random()

Just like in the previous chapter on infinite loops, you will have to press the :kbd:`Ctrl` and :kbd:`C` keys together on your keyboard to break out of the loop manually.  It will probably go so fast, that only by breaking out of the loop will you be able to look at the numbers properly.  If this doesn't work, then make sure you have imported the ``random`` module first.

Let's try another function - ``randrange`` - this time, instead of returning a number between 0.0 and 1.0 (which could be scaled up, if needs be), it will return an integer up to (but not including) the number you give it.  For example, try the following a few times::

    >>> random.randrange(100)
    >>> random.randrange(100)
    >>> random.randrange(100)

And try different numbers too::

    >>> random.randrange(10)
    >>> random.randrange(50)
    >>> random.randrange(25)

Try any end number you like, although the number must be above zero.  You can also give it a start number as a first parameter, so try these or other numbers as you wish::

    >>> random.randrange(10, 20)
    >>> random.randrange(50, 100)
    >>> random.randrange(1000, 2000)

.. pythontest:: on

The number returned is always between the numbers you give, including the start number, but excluding the end number.

A guessing game
---------------

Now we can use this knowledge to construct a simple game, where the program comes up with a random number, and the user has to guess it.  We'll give the user 6 tries until we give the answer.  So call your program :file:`guess.py`, and type in the following for starters::

    import random
    
    number_to_guess = random.randrange(1, 101)
    
We have imported the random module, in order to use it within our :file:`guess.py` program, and asked for a random number between 1 and 101 (1 and 100, inclusive, not including 101) and stored it against a variable name ``number_to_guess``.  Now we add the loop to give the user 6 tries at guessing, so add the following::

    num_tries = 0
    while num_tries < 6:
        num_tries = num_tries + 1
        
We define a variable ``num_tries``, and initially set it to zero.  We then loop while this value is less than six (so it should loop over the values 0, 1, 2, 3, 4 and 5 - six numbers in total), adding 1 onto the ``num_tries`` variable each time.

Inside the loop, we can add these lines (only add the new lines!)::

    num_tries = 0
    while num_tries < 6:
        user_guess = int(input('Guess the number: '))
        if user_guess == number_to_guess:
            print('Well done - you guessed right!')
            break
        num_tries = num_tries + 1

We ask the user a question, input what they have typed, and convert it into an integer storing it against a variable name called ``user_guess``.  If this variable is equal to the value the computer stored initially, then we print a message and then break out of the loop.  Otherwise we carry on by adding one onto the ``num_tries`` variable, and go back up to the top of the loop to repeat.

You can then finalise your program by giving the answer at the end, after the loop has finished.  So, in total, your program should look like this::

    import random
    
    number_to_guess = random.randrange(1, 101)
    
    num_tries = 0
    while num_tries < 6:
        user_guess = int(input('Guess the number: '))
        if user_guess == number_to_guess:
            print('Well done - you guessed right!')
            break
        num_tries = num_tries + 1

    print('The answer was:', number_to_guess)
    
You could enclose the ``print`` at the end with a test to only display it if the ``num_tries`` is 6, as if the user did guess the number they don't really need to be told what it was.

Exercises
---------

#. Modify your :file:`guess.py` program so that after testing whether the ``user_guess`` variable is equal to the computer's number ``number_to_guess``, the program will then test whether the user's number is less than the computer's number and print an appropriate message (e.g. 'Too low!'), and also if the user's number is larger than the computer's number, then print out another message (e.g. 'Too high!').  This will give the user a hint as to which direction to head in!

#. Write a program called :file:`poly.py` to randomly choose how many sides a polygon should have (e.g. between 3 and 12), and then draw the appropriate polygon.  So if the ``randrange`` function returns 3, then a triangle is drawn, or if it returns 8, an octagon is drawn.

Things to remember
------------------

#. To add variation, or a bit of :term:`randomness`, into your program, then ``import`` the ``random`` module, and make use of what it offers.

#. Two functions we used in this chapter are the ``random`` function (note: it has the same name as the module), which returns a floating point number between 0.0 and 1.0, and ``randrange`` which returns an integer number between 0 (or the starting point you provide) and up to (but not including) the end point.
