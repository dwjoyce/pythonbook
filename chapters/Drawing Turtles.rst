Drawing Turtles
===============

.. quote::
    :author: Anonymous

    Theory is when you know something, but it doesn't work. Practice is when something works, but you don't know why. Programmers combine theory and practice: Nothing works and they don't know why.

Importing
---------

Let us move from using Python to do maths and switch to doodling instead!

What we will do is to use a Python program called ``turtle`` to move a shape around the screen, leaving a trail behind in the process.  Think of it like using a piece of graph paper, with the origin in the centre, and the pen being moved by your instructions.

To use this separate turtle program, we have to use a new command called ``import``.  What :term:`import` does is to bring in, or include, a separate program - called a :term:`module` in Python - into your own program.  We cannot ever hope to write every piece of code ourselves, so often we depend on programs that others have been written and build on them.

It was Isaac Newton who said:

  "If I have seen further, it is by standing on the shoulders of giants."

In other words, he only made the advances in the fields of mathematics and physics he did by building on the work of those who came before him.

Programming is similar.  If we make use of the work of others, we can go far.  We can build more interesting programs much faster by using other people's code which we can depend upon.  Modules that Python itself offers as standard, ready to be included into your program, are often very well written and tested.

So, to include another program, we must use the ``import`` command, and give it the name of the module to import.  Although this program will have the :file:`.py` filename extension (e.g. :file:`turtle.py`), we do not include that part when naming the module.

Therefore, to use the ``math`` (for mathematics) module, you would type::

    >>> import math
  
and then you can use it thereafter, such as the square root function::

    >>> math.sqrt(64)
    8.0
  
which should give us the answer of 8 (8.0 to be exact), as you would expect.  You cannot use a module until you have performed the import, not before!  Notice the ``.`` (period) character - it separates the module name (``math``) from the function being used (``sqrt``).  We must write the name of the module first, followed by the ``.`` period, and then the function name that is to be found inside the module.  The period is used to say that this function is found inside this module - we will see more of this later when talking about functions that belong to a particular type.

Here is another example - using the value of :math:`\pi` as defined as a variable by the ``math`` module::

    >>> math.pi
    3.141592653589793

Using the name ``math.pi`` is not calling a function, it is referring to a floating point (i.e. fractional) variable inside the ``math`` module, therefore we do not need to use parentheses.  Although we refer to ``math.pi`` as a :term:`variable`, we do not expect it change in value.  We call this type of value a :term:`constant`.

Stick your head out of the shell
--------------------------------

So let us get back to our drawing.  To import the turtle module, you just need to type the ``import`` command followed by the name of the module, as follows::

  >>> import turtle
  
Now we can begin to use it.  The first time we use a function inside the turtle module, a window (similar to a canvas or graph paper) will pop up so that we can draw in it.  Let us do this by drawing something, so type in the following::

    >>> turtle.forward(100)
  
You should see a new window pop onto the screen.  Move it to the right of your screen so it does not obscure what you are typing, like so:

.. image:: /images/screenshots/idle_turtle.png
    :width: 90%
    :align: center

See how the small shape leaves a trail behind as it moves.  Let us carry on::

    >>> turtle.left(90)
    >>> turtle.forward(100)
    >>> turtle.left(90)
    >>> turtle.forward(100)
    >>> turtle.left(90)
    >>> turtle.forward(100)
    >>> turtle.left(90)
  
We have drawn a box!  We have effectively done the same thing four times - moved forward 100 places (measured in :term:`pixels`, which stands for picture elements), and then turned left 90 degrees each time.

If you make a mistake, you can go back a turn, or *undo* your previous move, by typing the following::

    >>> turtle.undo()
  
There are lots of other functions to call as well.  Try the following::

    >>> turtle.circle(75)
    >>> turtle.right(30)
    >>> turtle.forward(50)
    >>> turtle.begin_fill()
    >>> turtle.circle(40)
    >>> turtle.end_fill()

The ``begin_fill`` must be called before you start drawing your shape, and the ``end_fill`` function is called when the shape is complete.  The turtle program then knows what to fill in.

Here is a list of turtle functions you may find useful: ``forward``, ``left``, ``right``, ``up``, ``down``, ``goto``, ``begin_fill``, ``end_fill`` and ``undo``.

Exercises
---------

#. Draw a hexagon - a six sided shape, where the angle of turn is 120 degrees (180 minus 60 degrees).

#. Draw a star that has been filled in.  Hint: try turning 144 degrees and 72 degrees, alternatively, each time you draw a spike.

#. Draw a house, complete with roof, windows and door.  You will need to use ``turtle.up`` and ``turtle.down`` to pick the pen up and put it down, respectfully, so that you do not draw a line everywhere.

Things to remember
------------------

#. You can use another program by using the ``import`` command and the module's name (without the :file:`.py` extension).

#. You cannot use variables or functions from a separate module until you have imported it.

#. Use the ``.`` character to dip inside a module, with the module name first, and the variable or function from inside the module second.
