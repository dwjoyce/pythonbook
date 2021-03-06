More on functions
=================

.. quote::
    :author: William Shakespeare
    :source: Henry V

    Once more unto the breach, dear friends, once more!

In the previous chapter we learned how to define functions of our own, and how to pass in data that the functions can then use.  To follow on from this, we will now learn how to define functions that not only allow data to be passed in, but also return data that can be used by the calling code.  We are already used to this in the way we use functions built into Python itself.  Try these in the interactive interpreter::
    
    >>> round(1.75)
    2
    >>> abs(-10)
    10
    >>> max(10, 30, 20)
    30
    >>> min(50, 100, 25)
    25
    >>> sum(range(1000))
    499500

Hopefully that is all very straightforward to you now.  The last example gets a list of numbers from the ``range`` function, and passes it into the ``sum`` function, which sums all the numbers together, returning the total which is then shown in the interactive interpreter.  It has effectively added up the first 1000 numbers, from 0 to 999.

How do we do this in our own functions?

Please talk to me
-----------------

Open up your :file:`functions.py` program, and add the following function between your functions and the code calling them::
    
    def add_5(num):
        return num + 5
    
We have used the new keyword ``return`` - this takes an expression, and returns it to the caller of the function.  This means it is used (or discarded if it is not needed), by whatever code that has called the function in the first place.

Now add these lines onto the bottom of your program, so that the function defined above is called::
    
    print(add_5(10))
    
    my_num = 20
    print(add_5(my_num))
    
    new_num = add_5(my_num)
    print(new_num)
    
Now run the program, and see what it does.  It should call our new function ``add_5`` a number of times.  The first ones simply passed in the integer value 10.  Inside the function, the parameter ``num`` will refer to this value of 10.  The value is incremented by 5, and the result is :term:`returned` or sent back to the code that called the function.  In the first call of ``add_5``, this happens to be a ``print`` function, which naturally prints out the result it has been given (the number returned back from the function call).

The second use of the ``add_5`` function is similar, but instead of passing in a value, it passes in a variable which is referring to an integer value.  It then proceeds as before.

The third use of the ``add_5`` function is similar to the second use, but instead of printing the value returned back from the function call straight away, it first assigns the returned value to a new variable called ``new_num``.  This is then printed out on its own.

Forming a chain
---------------

With the use of the ``return`` keyword to send data back, you can effectively form a chain of functions just like we have done with the built-in ones at the beginning of the chapter.  Type this into your :file:`functions.py` program, under your other function definitions::

    def sum_up(num1, num2):
        return num1 + num2
        
Then below, with the other calling code, add the following lines::

    print(sum_up(10, 20))
    
    total = sum_up(100, -50)
    print(total)

This is very similar to what we have done already.  Now let's chain our functions together::

    print(sum_up(sum_up(1, 2), sum_up(3, 4)))
    
This could go on and on!  You are effectively forming an expression in the shape of a tree - the inner calls to ``sum_up`` are called first, the one on the left, and then the one on the right.  With these two values, 3 and 7, respectively, the outer ``sum_up`` is called, thus producing the final printed result of 10. This expression is equivalent to ``(1 + 2) + (3 + 4)``.

Naming parameters
-----------------

So far we pass :term:`arguments` into functions, used inside the function as :term:`parameters`, to feed data into the function.  We generally do the following, which you should now type into your ever increasing :file:`functions.py` program::

    def box_volume(length, height, width):
        return length * height * width
        
    print(box_volume(10, 20, 30))

You should place the calling of the function, the line containing the function name ``print``, along with the other code towards the bottom of your program.

It is quite clear that the integer value ``10`` is passed into parameter ``length``, ``20`` is passed into the parameter ``height``, and ``30`` is passed into the parameter ``width``.  In Python, these are called :term:`positional arguments` - the position of each argument determines which parameter it is passed into.  The first argument is passed into the first parameter, the second argument is passed into the second parameter, and so on.  If you get the order of your arguments wrong, then then the wrong data will be fed into the wrong parameters.  Bad things will happen.

An alternative is to explicitly state what parameters you want to use for each argument (remember, arguments on the outside are being passed into parameters on the inside).  Use the same function definition, but call it in this way.  You should place this line beneath the last statement from above::

    print(box_volume(length=10, height=20, width=30))
    
Run your program again, and make sure it now prints out the same volume twice.  However, the line calling the function ``box_volume`` makes more sense with the parameter names being assigned to the argument values explicitly.  Yes, it is more typing, but reads better.

This is called :term:`keyword arguments` - you are referring to each parameter by name or keyword, and supplying the data you want to be associated with each.  This may not look very useful in this example, but when function definition and function invocation (i.e. calling the function) are in different modules, then it allows you to immediately see what value is being passed into what parameter.  The function call contains more information, and allows you to see what is going on.

A little more practice
----------------------

We will write a little turtle based program to demonstrate some of the concepts we have been learning here.  Open up a new file, and type in the following:

.. code::
    :pythontest: norun

    import turtle
    import random


    def draw_circle(radius, red, green, blue):
        turtle.pencolor(red, green, blue)
        turtle.fillcolor(red, green, blue)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        
    # Set the speed and save width and height
    turtle.speed('fastest')
    win_width, win_height = turtle.window_width(), turtle.window_height()
    
    while True:
        # Define the radius of the circle, between 20 and 200 pixels each
        size = random.randrange(20, 200)

        # Move to a random position in the window
        # Remember to pick up the pen first
        x = random.randrange(-win_width // 2, win_width // 2)
        y = random.randrange(-win_height // 2, win_height // 2)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

        # Draw circle
        draw_circle(radius=size,
                    red=random.random(), green=random.random(),
                    blue=random.random())

Run your program, saving it as :file:`circles.py`, and make sure it runs without errors.  You should be getting lots of randomly colored and sized circles on the screen, similar to the following:

.. image:: /images/screenshots/randomcircles.png
    :width: 250pt
    :align: center

A little explanation:

    - We import the modules we need, ``turtle`` for drawing, ``random`` for producing a bit of variation.
    - We then define a function called ``draw_circle`` which take four arguments - the radius, followed by red, green and blue to define the color.
    - Inside the ``draw_circle`` function, we set the pen and fill color, tell turtle we are starting the shape so it can be filled in later, and then draw a circle.  We then end the shape, so the circle is filled in.
    - In the main part of the program, we set the speed to hurry things up, and then save the window width and height so we can use them later.
    - We then enter a loop which continues forever.
    - Inside the loop, we first define the size of the circle by using the ``randrange`` function in the ``random`` module.  We ask for a radius somewhere between 20 and 200.
    - We then pick up the pen, and move it to a random place in the drawing window, and then put the pen down again.
    - We then call our ``draw_circle`` function using the data we have at hand.

Exercises
---------

#. Write a function called ``add_list`` in your :file:`functions.py` program, which accepts a list comprising of a list of integers.  The function will step through the list, and return the sum.  The sum should then be printed out.

#. Write a function called product in your :file:`functions.py` program, which accepts two numbers.  The function returns the product of these numbers (i.e. the numbers multiplied together).  Then call this function, ``product``, along with the function ``sum_up`` we wrote earlier, to form a tree-like expression.  Print out the result.  For example, use your functions to imitate this arithmetic expression: ``(4 * 5) + (6 * 7)``.

#. Write a function called prime in your :file:`functions.py` program, which accepts a single number and returns ``True`` (a boolean value) if it is a prime number or ``False`` if not.  Remember, 0 and 1 are not prime, 2 is prime, and for the other numbers, a prime number is one that is only divisible by itself and 1.

Things to remember
------------------

#. Functions can both receive and return data.  Data is received via the use of :term:`parameters`.  Data is returned via the use of the ``return`` keyword.  You combine the ``return`` keyword with an optional expression to form the :term:`return statement`.

#. Even functions without the ``return`` statement return a value - the value ``None``.  It is like a non or null value, similar to zero but not actually an integer number.

#. When a program comes across the ``return`` keyword, control returns immediately to the calling code.  This is the case even if there is more code after the return statement - this code is effectively out of reach by the program.  This is why it is called *unreachable* code.

#. There are two ways of passing in arguments with functions.  Firstly, by *position* (:term:`positional arguments`), so the order of arguments is matched up with the order of parameters.  Secondly, by *keyword* (:term:`keyword arguments`), so you can specify the name of the parameter, followed by the equals sign, and then the expression (e.g. a value or variable name) that parameter should set to.
