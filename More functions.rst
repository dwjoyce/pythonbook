More on functions
=================

In the previous chapter we learned how to define functions of our own, and how to pass in data that the functions can then use.  To follow on from this, we will now learn how to define functions that not only allow data to be passed in, but also return data that can be used by the calling code.  We are already used to this in the way we use functions built into Python itself.  Try these in the interactive shell::
    
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

Hopefully that is all very straightforward to you now.  The last example gets a list of numbers from the ``range`` function, and passes it into the ``sum`` function, which sums all the numbers together, returning the total which is then shown in the interactive shell.  It has effectively added up the first 1000 numbers, from 0 to 999.

How do we do this in our own functions?

Please talk to me
-----------------

Open up your functions.py program, and add the following function between your functions and the code calling them::
    
    def add_5(num):
        return num + 5
    
We have used the new keyword ``return`` - this takes an expression, and returns it to the caller of the function.  This means it is used, or discarded, by whatever code has called the function in the first place.

Now add these lines onto the bottom of your program, so that the function defined above is called::
    
    print(add_5(10))
    
    my_num = 20
    print(add_5(my_num))
    
    new_num = add_5(my_num)
    print(new_num)
    
Now run the program, and see what it does.  It should call our new function *add_5* a number of times.  The first ones simply passed in the integer value 10.  Inside the function, the parmater *num* will refer to this value of 10.  The value is incremented by 5, and the result is *returned* or sent back to the code that called the function in the first place.  In the first call of *add_5*, this happens to be a ``print`` function, which naturally prints out the result it has been given (the number returned back from the function call).

The second use of the *add_5* function is similar, but instead of passing in a value, it passes in a variable which is referring to an integer value.  It then proceeds as before.

The third use of the *add_5* function is similar to the second use, but instead of printing the value returned back from the function call straightaway, it first assigns the returned value to a new variable called *new_num*.  This is then printed out on its own.

Forming a chain
---------------

With the use of the ``return`` keyword to send data back, you can effectively form a chain of functions just like we have done with the built-in ones at the beginning of the chapter.  Type this into your functions.py program, under your other function definitions::

    def sum_up(num1, num2):
        return num1 + num2
        
Then below, with the other calling code, add the following lines::

    print(sum_up(10, 20))
    
    total = sum_up(100, -50)
    print(total)

This is very similar to what we have done already.  Now let's chain our functions together::

    print(sum_up(sum_up(1, 2), sum_up(3, 4)))
    
This could go on and on!  You are effectively forming an expression in the shape of a tree - the inner calls to *sum_up* are called first, the one on the left, and then the one on the right.  With these two values, 3 and 7, respectively, the outer *sum_up* is called, thus producing the final printed result of 10.

Naming parameters
-----------------

So far we pass arguments into functions, used inside the function as parameters, to feed data into the function.  We generally do the following, which you should now type into your ever increasing functions.py program::

    def box_volume(length, height, width):
        return length * height * width
        
    print(box_volume(10, 20 30))

You could place the calling of the function, the line containing the function name ``print``, along with the other code towards the bottom fo your program.

It is quite clear that the integer value *10* is passed into parameter *length*, *20* is passed into the parameter *height*, and *30* is passed into the parameter *width*.  In Python, this is called *positional arguments* - the position of each argument determines which parameter it is passed into.  The first argument is passed into the first parameter, the second argument is passed into the second parameter, and so on.  If you get the order of your arguments wrong, then then the wrong data will be fed into the wrong parameters.  Bad things will happen.

An alternative is to explicitly state what parameters you want to use for each parameter.  Use the same function definition, but call it in this way.  You should place this line beneath the print statement above::

    print(box_volume(length=10, height=20, width=30))
    
Run your program again, and make sure it now prints out the same volume twice.

This is called keyword arguments - you are referring to each parameter by name, by keyword, and supplying the data you want to be associated with each.  This may not look very useful in this example, but when function definition and function invocation (i.e. calling the function) are in different modules, then it allows you to immediately see what value is being passed into what parameter.  The function call contains more information, and allows you to see what is going on.

A little more practice
----------------------

We will write a little turtle based program to demonstrate some of the concepts we have been learning here.  Open up a new file, and type in the following::

    import turtle
    import random

    def draw_box(length, width, red, green, blue):
        turtle.fillcolor(red, green, blue)
        turtle.begin_fill()
        for side in range(4):
            if side % 2:  # is side even or odd?
                turtle.forward(length)
            else:
                turtle.forward(width)
            turtle.right(90)
        turtle.end_fill()

    turtle.Turtle()
    turtle.speed('fastest')
    win_width, win_height = turtle.window_width(), turtle.window_height()

    while True:
        # Generate the length and width, between 20 and 100 pixels each
        length = random.randrange(20, win_height / 2)
        width = random.randrange(20, win_width / 2)

        # Move to a random position in the window
        x = random.randrange(-win_width//2, win_width//2)
        y = random.randrange(-win_height/2, win_height/2)
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

        # Draw box
        draw_box(length, width,
                 red=random.random(), green=random.random(), blue=random.random())

Run your program, saving it as *boxes.py*, and make sure it runs without errors.  You should be getting lots of randomly coloured and sized boxes on the screen.

A little explanation:

    - we import the modules we need, turtle for drawing, random for producing a bit of variation.
    - we then define a function called *draw_box* which take five arguements - the length and width, followed by red, green and blue to define the colour.
    - inside the *draw_box* function, we set the fill colour, tell turtle we are starting the shape so it can be filled in later, and then draw a four sided box.  If the side number is not divisible by 2 (i.e. is odd), then we draw its length, otherwise its width.
    - in the main part of the program, we create our window using the Turtle() function, set the speed to hurry things up, and then save the window width and height so we can use them later.
    - we then enter a loop which continues forever.
    - inside the loop, we first generate the length and width of the new box by using the ``randrange`` function in the ``random`` module to generate the numbers for us.
    - we then pick up the pen, and move it to a random place in the drawing window, and then put the pen down again.
    - we then call our *draw_box* function using the data we have at hand.


Exercises
---------

1. Write a function called add_list in your functions.py program, which accepts a list comprising of a list of integers.  The function will step through the list, and return the sum.  The sum should then be printed out.

2. Write a function called product in your functions.py program, which accepts two numbers.  The function returns the product of these numbers (i.e. the numbers multiplied together).  Then call this function, *product*, along with the function *sum_up* we wrote earlier, to form a tree-like expression.  Print out the result.  For example, use your functions to imitate this arithmetic expression: (4*5) + (6*7).

3. Write a function called prime in your functions.py program, which accepts a single number and returns True (a boolean value) if it is a prime number or False if not.  Remember, 0 and 1 are not prime, 2 is prime, and for the other numbers, a prime number is one that is only divisible by itself and 1.

Things to remember
------------------

1. Functions can both receive and return data.  Data is received via the use of parameters.  Data is returned via the use of the ``return`` keyword.

2. Even functions without the ``return`` keyword return a value - the value ``None``.  It is sort of like a non-value, similar to zero but not actually an integer number.

3. When a program comes across the ``return`` keyword, control returns immediately to the calling code.  This is the case even if there is more code after the return satement - this code is effectively out of reach by the program.  This is why it is called *unreachable* code.

4. There are two ways of passing in argments with functions.  Firstly, by *position*, so the order of arguments is matched up with the order of parameters.  Secondly, by *keyword*, so you can specifiy the name of the paramter, followed by the equals sign, and then the expression (e.g. a value or variable name) that parameter should be given.
