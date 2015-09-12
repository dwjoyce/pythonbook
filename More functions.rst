More functions
==============

In the previous chapter we learned how to define functions of our own, and how to pass in data that the functions can then use.  To follow on from this, we will now learn how to define functions that not only allows data to be passed in, but also returns data that can be used by the calling code.  We are already used to this in the way we use functions built into Python itself.  Try these in the interactive shell::
    
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

Things to remember
------------------

1. Functions can both receive and return data.  Data is received via the use of parameters.  Data is returned via the use of the ``return`` keyword.

2. Even functions without the ``return`` keyword return a value - the value ``None``.  It is sort of like a non-value, similar to zero but not actually an integer number.

3. When a program comes across the ``return`` keyword, control returns immediately to the calling code.  This is the case even if there is code after the return satement - this code is effectively out of reach by the program.  This is why it is called *unreachable* code.
