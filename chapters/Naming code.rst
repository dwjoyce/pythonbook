Naming code
===========

Data and code
-------------

Variables are a way of naming data.  A piece of data, like the number *123*, can be given the name *number* like this in Python (try it in the interactive shell)::

    >>> number = 123
    
In this case, the data is an integer, a whole number.  We can name other types of data as well::

    >>> cups_of_flour = 2.5
    >>> name_of_recipe = 'wholemeal bread'
    >>> pages_from_book = [19, 22, 23]
    >>> is_recipe_tasty = True
    
This is very good for people reading the code, as it describes the meaning behind the data much clearer when it is given a name like this.  We can also use the same name, but modify its value over the course of the execution of the program, thus allowing variables to really *vary*::

    >>> people_going_to_mordor = ['Frodo', 'Sam']
    >>> people_going_to_mordor.append('Merry')
    >>> people_going_to_mordor.append('Pippin')

or more simply such as::

    >>> number = 100
    >>> number = number + 1
    
Programs are made up of data, which we have been discussing above, and code.  We have the ability to name our data, but it would be helpful if we also had the ability to name our code.  This would prevent repeating our code, using the name instead of the code itself, and also allow our programs to become more organised.

Functions
---------

We have already used named sections of code - they are called *functions*.  Python programs are generally organised into modules (the programs themselves) and functions (the named sections of code contained within each module).  A function is given a name, and we invoke it (call it) by placing parentheses afters its name.  Try the following, again in the interactive shell::

    >>> print()
    
    >>> print('Hello, World!')
    Hello, World!
    >>> abs(-15)
    15
    >>> new_num = round(10.75)
    >>> print(len('The quick brown fox jumps over the lazy dog'))
    43

As we can see above, functions take take in values (which we have learned are called *arguments*), or not.  They can return values, or not.  It just depends on what they do, and what we want to use them for.

In this chapter, we will begin learning how to define our own functions, and not just use functions already present in the language (built-in ones), or from other programs (imported modules).

But before we do, why should we bother?  Can't we just use loops instead?

Loops are very useful, but only when the code to be repeated is in the same place.  Functions are useful when they are being used from a number of places, especially if they are not in related parts of your program.  They are more flexible, and offer a way of being called from anywhere - even outside your program, just like we do to other modules (e.g. ``turtle``).  Moreover, giving pieces of your code a name makes it more understandable to those reading it, or even to you when you come back to your program in the future.

Here is an example of a bit of code that needs sections to be separated into functions and given a name.  You don't need to type this in, it is just provided for information::

    print('Hello there')
    print()
    print('Hello there')
    num = 10
    print('Hello there')
    num = num + 1
    print('Hello there')

Lots of repetitive code that could be parcelled up, given a name and put in one place, but called from where it is needed.  When code only needs to be written once, we tend to make less mistakes than when we have to write it lots of times.

Rolling our own
---------------

While naming data we use the assignement operator, when naming code we use the ``def`` keyword.  This means we are *defining* a function - not calling it, but defining it.  Just because you define a function, doesn't mean it gets called - it is simply there ready to be called upon when needed.

Open up a new file window, and type in the following::

    def say_hello():
        print('Hello there')
        
Save your program as functions.py, and run it.  It should do nothing - as described just above, it is available to your program, but it is not being run yet.  To do that, insert the following line beneath your program::

    say_hello()
    
Now save and run your program again - it should now print out something.  In fact, it should say hello!  Just like calling other functions, if you miss off the parentheses, then the function does not get called, it simply returns where it is located in memory - probably not what you intended!

So to define a function, we use the ``def`` keyword.  To call or invoke a function, we use the name of the function followed by parentheses ``()``.

Passing in data
---------------

However, a function that always does the same thing is very limited.  It is more useful to have the ability to pass information into the function, so the function can use this information on the inside, as it were.  For example, let's take the example we did above, but vary it slightly.  So type this in beneath your definition of the say_hello function in your functions.py program (i.e. not at the bottom, so as to keep your functions together, and your calls together)::

    def say_hello_times(times):
        print('Hello there' * times)

Now insert this new line below your ``say_hello()`` call at the bottom of your program::

    say_hello_times(5)

Run it and ensure it prints out the same message, but this time 5 times.  That will be 6 times in total, with the initial call to the ``say_hello`` function as well.  Try a couple more combinations::

    say_hello_times(10)
    say_hello_times(50)
    
It should print out the message the number of times you are requesting.  If not, then something is very wrong!

Now, of couse, if you can pass in one thing, you can pass in many.  So our next function (again, insert it between where the functions are defined and where they are being called), will take a message and a number, so the caller can specify what he wants printing::

    def say_message_times(msg, times):
        print(msg * times)

and insert these lines below the last call to ``say_hello_times``::

    say_message_times('Yo! ', 25)
    say_message_times('I will stop talking in class', 100)
    
.. note:: An argument is the value or variable being passed *into* a function.  A parameter is the variable as received inside a function.  Or in other words, it has parameters, but takes in arguments.  Perhaps it is easier to remember it like this: for the sake of argument, if we pass in ``'Yo!'`` and ``25``, the function uses them as parameters.

These parameters can be anything you like, it just depends on what the function does, and what information it needs to operate.  Let's add onto our list of functions with one that takes in two numbers, and prints out the sum::

    def add_two_nums(num1, num2):
        print(num1 + num2)
        
and again, lower down, we can call this function::

    add_two_nums(10, 20)
    add_two_nums(-50, 25)
    add_two_nums(100, 200)
    
If you call this function with three arguments, then Python will complain - three arguments into two parameters does not go!

These functions are very short, so may not appear very useful yet, but imagine writing a function that is 10 or 20 lines long, and is used in a number of places in your program.  Then your program will be much shorter, more readable and produce better results.

In the next chapter, we will discuss not only passing data into a function, but also getting data out again.

Exercises
---------

1. Write another function called ``calc`` which accepts two numbers and also a string value which you can call ``opertor``.  The operator parameter can be either "add", "subtract", "multiply" or "divide".  Depending on this value, you should perform the appropriate calculation, and print out the result,  For example, if the values 4, 5, "add" are passed in, then it should print out the result 20.  If the values 100, 8, "divide" are passed in, then it should print out 12.5.  You can place this function inside the same functions.py program.

2. Write a function called ``timestable`` which receives a number and prints out a times table with that number of rows and columns.  For example, if the number 5 is passed in, then the 5 times table is printed.  If the number 12 is passed in, then the 12 times table is printed.  It is best to use two for loops - one for the rows, and inside this, another for the numbers themselves, both counting along the same range of numbers.  Again, put it in the same functions.py program.

3. Start a new program called shapes.py.  It should use the ``turtle`` module and repeatedly ask the user what shape to draw - for example, box, circle, polygon, star.  Depending on what the user types in, the program should draw that shape.  The code for drawing each shape should reside in its own function, e.g. a function for ``box``, ``circle``, ``polygon`` and ``star``.  Each function will have to ask the information it needs itself, e.g. a circle will need to input the radius.

Things to remember
------------------

1. To define a new function, use the ``def`` keyword, followed by the name of the function, and then parentheses.

2. Inside the parentheses, place any parameters you are expecting.  Separate each one using a comma.  This is a way of passing in data to affect how the function behaves - pass in different data, it should do different things.

3. The function definition is completed with a colon ``:`` symbol, followed by the code that is inside the function.  This code, like any block of code, is indented to the right.

4. Defining a function does not mean it is used - it is simply available to be used, like a tool in a toolbox.  To call or invoke a function, you must use its name, followed by parentheses, but without the ``def`` keyword.