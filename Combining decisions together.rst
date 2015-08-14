Combining decisions together
============================

Juggling tests
-------------

We have learned how to use the ``if`` statement to evaluate a test, and if true it then executes a block of code you provide immediately underneath.  It makes our programs cleverer so that they can take different decisions depending on the circumstances at the time.

This chapter introduces logical operators which make combining tests together easier.  Although this part of programming is not essential, it does make our programs much easier to write.

For example, take a program that wants to tell the user whether he can go the beach or not.  This decision depends on the weather (preferably warm), and whether it is during the holidays or not.

With what we know now, we could code this as follows, so type this into a new file window::

    weather = input('How is the weather, warm or cold? ')
    holidays = input('Are we on holiday at the moment, yes or no? ')

    if weather == 'warm':
        if holidays == 'yes':
            print('Yes! Let\'s go to the beach!')
        else:
            print('Sorry, let\'s try again later!')
    else:
        print('Sorry, let\'s try again later!')

Save this program and call it beach.py.  Run it and test it out - it should all work fine, regardless of the combination of values you type in.

However, this took a lot of typing to get working, and programmers like to avoid typing when we can!  One problem is that the 'Sorry' message is done twice, so we duplicating a line unnecessarily.  We also have two ``else`` statements to go with the two ``if`` statements.  It would be much better if we could combine the two tests together on one line, with one ``if`` statement and one ``else`` statement, with each call to the ``print`` function done once each as well.

So far, we have only learned how to attach one test to either an ``if`` statement or an ``elif`` statement.  With logical operators, we can combine a number of tests together to form a larger single test.  There are three logical operators:

    - ``and`` which tests whether the left-hand side and the right-hand side are both true, giving an overall result of true.  For example: ``a > 10 and b > 10`` tests whether *a* and *b* are both greater than 10, and if so the whole expression is true.
    
    - ``or`` which tests whether either the left-hand side or the right-hand side are true, thus giving a overall result of true.  For example, ``a < 0 or a > 100`` tests whether *a* is either less than zero (i.e. negative) or greater than 100 (but obviously not both at the same time), and if so the whole expression is true.  Both sides can be true, which is also fine.
    
    - ``not`` which takes a single boolean value and inverts its value, so ``true`` becomes ``false`` and ``false`` becomes ``true``.  For example, ``not weather == 'warm'`` which tests whether the variable weather is equal to the value 'warm', and then flips the result.
    
So, how do we apply this to our code in the beach.py program?  To see this, you need to change your big ``if`` statement from this::

    if weather == 'warm':
        if holidays == 'yes':
            print('Yes! Let\'s go to the beach!')
        else:
            print('Sorry, let\'s try again later!')
    else:
        print('Sorry, let\'s try again later!')
        
to this::

    if weather == 'warm' and holidays == 'yes':
        print('Yes! Let\'s go to the beach!')
    else:
        print('Sorry, let\'s try again later!')

Save and run this version, and make sure it does the same thing.

Notice how we have taken the two separate ``if`` statements in the previous version of the program, and combined them together - since one was inside the other - with the logical *and* operator.  This will then only perform the first call to the ``print`` function if both the weather is 'warm' ``and`` and holidays is 'yes'.  Otherwise, we do what comes after the ``else`` statement.

The logical ``or`` operator is useful when a number of separate tests all do the same thing, so their blocks of code are all the same.

For example, create a number program called numbers.py, and type in the following::

    ticket1 = input('Enter ticket number 1: ')
    ticket2 = input('Enter ticket number 2: ')
    ticket3 = input('Enter ticket number 3: ')
    
    prize_number = input('What is the prize number? ')

    if ticket1 == prize_number or ticket2 == prize_number or ticket3 == prize_number:
        print('We won the prize')
    else:
        print('Nevermind, maybe next time!')
        
Without the use of the ``or`` operator, we would have to have written 3 ``if`` statements, all doing the same thing.  The ``or`` operator has allowed us to combine these 3 tests into one, thus saving on lots of typing and duplication in our code, which is never a good thing.

Exercises
---------

1. Write a program called largest.py to input three numbers, convert the inputs from strings to integers, and print out the largest.  Use the ``if`` and ``elif`` statements and the ``and`` operator to perform your tests.

2. Write another program called car.py, to ask the user the attributes of a car, such as colour (e.g. 'red', 'green' or 'blue'), type (e.g. 'van', 'sports', 'estate') and price.  The program should print out 'I want that car' if the colour is 'red', the type is 'sports' and the price is less than 10,000.


Things to remember
------------------

1. There are three logical operators: ``and`` for testing whether the left and right-hand side tests are both true; ``or`` for testing whether either the left or right-hand side tests are true; ``not`` for inverting a boolean value.

2. Put the ``and`` and ``or`` operators inbetween boolean expressions.  Put the ``not`` operator infront of a boolean expression.
