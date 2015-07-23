Drawing Turtles
===============

Importing
---------

Let us take a break from using Python to do Maths and switch to doodling instead!

What we will do is to use a Python program called ``turtle`` to move a shape around the screen, leaving a trail behind in the process.  Think of it like a piece of graph paper, with the origin in the centre, and the pen being moved by your instructions.

To use this separate Turtle program, we have to use a new command called *import*.  What import does is to bring in, or include, a separate program - called *module* in Python - into your own program.  We cannot ever hope to write every piece of code ourselves, so often we depend on programs that others have written and build on them.

It was Isaac Newton who said the following:

  "If I have seen further it is by standing on the shoulders of Giants"

In other words, he could only have made the advances in the fields of mathematics and physics, but building on the work of those who came before him.

Programming is similar.  If we make use of the work of others, we can go far.  We can build more interesting programs much faster, and we also use other people's code which we can depend upon.  Modules that Python itself includes, ready to be included into your program, is often very well written and tested.

So, to include another program, we must use the ``import`` command, and give it the name of the module to import.  Although this program will have the ".py" extension (e.g. math.py), we do not include that part when naming the module.

Therefore, to use the math (for mathematics) module, you would type::

  >>> import math
  
and then you can use it thereafter, such as the square root function::

  >>> math.sqrt(64)
  
which should give us the answer of 8 (8.0 to be exact), as you would expect.  You cannot use a module until you have performed the import, not before!  Notice the ``.`` (period) character - it separates the module name (``math``) from the function being used (``sqrt``).

Here is another example - using the value of pi as defined as a variable by the math module::

  >>> math.pi

Stick your head out of the shell
--------------------------------

So let us get back to our drawing.  To import the turtle module, you just need to type the following::

  >>> import turtle
  
Now we can begin to use it.  The first thing to do is to get our window onto the screen.  This is used to display our canvas (or graph paper), so that we can begin our drawing.  This is done by calling the Turtle function::

  >>> turtle.Turtle()
  
At first you may find this confusing - ``turtle`` (with a lowercase 't') is the module name, and ``Turtle`` (with an uppercase 't') is the function that creates the drawing window.  Please do not confuse the two - the function name begins with a CAPITAL letter!

You should see a new window pop up onto the screen.  Move it so it does not obscure what you are typing.

We are now ready to get drawing.  Try typing the following in order::

  >>> turtle.forward(100)
  
See how the small shape leaves a trail behind as it moves.  Let us carry on::

  >>> turtle.left(90)
  >>> turtle.forward(100)
  >>> turtle.left(90)
  >>> turtle.forward(100)
  >>> turtle.left(90)
  >>> turtle.forward(100)
  >>> turtle.left(90)
  
We have drawn a box!  We have effectively done the same thing four times - moved forward 100 places (measured in *pixels*, which stands for picture elements), and then turned left 90 degrees.

If you make a mistake, you can go back a turn, or *undo* your previous move, by typing the following::

  >>> turtle.undo()
  
There are lots of other functions to call as well.  Try the following::

  >>> turtle.circle(75)
  >>> turtle.right(30)
  >>> turtle.forward(50)
  >>> turtle.begin_fill()
  >>> turtle.circle(40)
  >>> turtle.end_fill()
  
The ``begin_fill`` must be called before you start drawing your shape, and the ``end_fill`` function is called when the shape is complete.  Then the turtle code knows what to fill in.

Here is a list of turtle functions you may find useful: ``forward``, ``left``, ``right``, ``up``, ``down``, ``goto``, ``begin_fill``, ``end_fill`` and ``undo``.

Exercises
---------

1. Draw a hexagon - a six sided shape, where the angle of turn is 120 degrees (180 minus 60 degrees).
2. Draw a star that has been filled in.
3. Draw a house, complete with roof, windows and door.  You will need to use ``turtle.up()`` and ``turtle.down()`` to pick the pen up and put it down, respectfully, so that you do not draw a line everywhere.

Things to remember
------------------

1. You can use another program by using the ``import`` command and the module's name (without the .py extension).

2. You cannot use variables or functions inside a module until you have imported it.

3. Use the ``.`` character to dip inside a module, with the module name first, and the variable or function inside the module second.
