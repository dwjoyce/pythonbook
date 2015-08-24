Naming code
===========

Data and code
-------------

.. pythontest:: nooutput

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
    >>> ord(-15)
    >>> new_num = round(10.75)

As we can see above, functions take take in values (which we have learned are called *arguments*), or not.  They can return values, not not.  It just depends on what they do, and what we want to use them for.

In this chapter, we will begin learning how to define our own functions, and not just use functions already present in the language (built-in ones), or from other programs (imported modules).

But before we do, why should we bother?  Can't we just use loops instead?

Loops are very useful, but only when the code to be repeated is in the same place.  Functions are useful when they are being used from a number of places, especially if they are not in related parts of your program.  They are more flexible, and offer a way of being called from anywhere - even outside your program, just like we do to other modules (e.g. turtle).  Moreover, giving pieces of your code a name makes it more understandable to those reading it, or even to you when you come back to your program in the future.

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
        
Save your program as functions.py, and run it.  It should do nothing - as described just above, it is available to your program, but it is not being run yet.  To do that, then insert the following line beneath your program::

    say_hello()
    
Now save and run your program again - it should now print out something.  In fact, it should say hello!  Just like calling other functions, if you miss off the parentheses, then the function does not get called, it is simply referred to

.. pythontest:: all

Exercises
---------

Things to remember
------------------

1. To define a new function, use the ``def`` keyword, followed by the name of the function, and then parentheses.

2. Inside the parentheses, place any parameters you are expected.  Separate each one using a comma.
