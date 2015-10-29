Performing selection
====================

.. quote::
    :author: Gollum / Sméagol

    If Baggins loses, we eats it whole.

Taking a different route
------------------------

With what we have learned up until now, we can do arithmetic, store values against variable names, call functions, import other people's modules, and even get input from the user.  We have also dealt in different types of data, whether numbers (integers or floating point) or strings (sequences of letters, digits and symbols).  Our programs have started running (technically known as :term:`executing`) from the top, and finished at the bottom, performing each line (a code statement) at a time, without any deviation whatsoever.

If a program simply performs the same instructions, line by line, every single time, then effectively they do the same thing every time they are run.  This is not very interesting!  Programs become more useful when they can make decisions on what to do, depending on the circumstances.  Usually, this involves testing the value of a variable, and then performing some instructions over others.  In programming, this is known as :term:`selection` - the program is running some code statements selectively over others - it is making a decision.

For example, if the program is working out the price of a cinema ticket, and VIP tickets cost 20% extra, the program needs to take a decision as to whether to add on this 20% or not.  It cannot add on 20% for all the tickets!

To achieve this in Python, we use the ``if`` statement.  We start with the word ``if``, and then give it a test to evaluate.  If the test evaluates to true (i.e. it is successful), then the statements underneath are performed (executed).  If the test evaluates to false (i.e. it was unsuccessful), then the statements underneath are skipped.

.. note:: Statements that belong to an ``if`` statement must be pushed to the right in order to show what code belongs to what line.  In programming, this is called :term:`indentation`.  In Python, we indent by four spaces.  When the code block is finished, we unindent back to the column of the initial line.

Let us start a new program called vip.py - click on the ``File`` -> ``New File`` menu item, and type in the following::

    print('Welcome to our VIP program for calculating cinema ticket prices')
    print('Ticket prices are £5.00 for ordinary tickets, £6.00 for VIPs')

    vip = input('Do you want a VIP ticket, yes or no? ')

    price = 5.0

So far, so good!  Now we need to take a decision, so add the following to your program::

    if vip == 'yes':
        price = price * 1.2

You will notice we have used the ``if`` statement to perform a test.  The test is whether the variable ``vip``, created when we saved the answer from asking the user the question over VIP tickets, is the same as the string *yes*.  To perform the test, we have introduced a new operator, called the equals operator.  It is looks similar to the assignment operator, which creates variable names, but the equals operator has two equals signs, not one.  It is testing whether what is on the left is equal to what is on the right.  If the equals test is successful, then the expression is ``True``, and the code drops into the code below the ``if`` statement, indicated by the code being indented to the right.

Also note the use of the colon ``:`` symbol.  This is used at the end of every line that has other lines that are attached to it.  We will be seeing that on many more occasions in the future with other statements we will be introducing.  It effectively tells Python to run the following lines if the test just evaluated was true.  Please don't miss these off!

We can now finish our program, so add the last line on the end so that your complete programs looks like the following::

    print('Welcome to our VIP program for calculating cinema ticket prices')
    print('Ticket prices are £5.00 for ordinary tickets, £6.00 for VIPs')
    
    vip = input('Do you require a VIP ticket, yes or no? ')
    
    price = 5.0

    if vip == 'yes':
        price = price * 1.2
        
    print('Your total price is:', price)

See how the program carries on past the test, whether the ``if`` statement test was true or not - you simply have to move back 4 spaces to the left.  This means our :term:`code block` attached to the ``if`` statement is over, and we now carry on as usual.

Now save and run your program using the ``F5`` key, pressing Return, and using the program name of vip.py.  Remember, to save your program onto your USB stick.

You will have to run your program twice.  Initially, input *yes* as the answer to the question, and secondly, input *no* (or vice versa).  You should get different results depending on what you enter on the keyboard - either a price of £6 or £5.  Be careful what you type - if you do not type *yes* exactly, then the test will fail, and the indented statement will not be executed.

In a code block, you can have any number of statements, just like the program as a whole.  Add onto your code block, belonging to the ``if`` statement, so it looks like this::

    if vip == 'yes':
        price = price * 1.2
        print('You have chosen a VIP seat - enjoy your film!')

Run your program again, and notice how either both of these statement will be performed, or neither of them.  They belong together in the same code block, and are attached to the ``if`` statement above them.  You can even have blocks inside blocks.  Change your ``if`` statement block to do the following::

    if vip == 'yes':
        price = price * 1.2
        print('You have chosen a VIP seat - enjoy your film!')
        weekend = input('Is your viewing at the weekend, yes or no? ')
        if weekend == 'yes':
            price = price * 1.5
            print('Weekend viewing adds on another 50%, sorry!')
            
Watching films at the weekend is very expensive, 50% more expensive!  You will notice, though, that this is only added on for VIP seats, as the question and the test, along with the increase in price, all live inside the test for VIP seats only.  Regardless, this demonstrates that one block of code (with a certain level of indentation) can reside inside another.  There is no limit to how many blocks can be inside other blocks, although if we overdo this, it will make the code less readable.

You can add another block of code that is selectively executed after the ``if`` statement above, just by starting it in the same column as the first.  Add these extra three lines onto your program::

    if vip == 'yes':
        price = price * 1.2
        print('You have chosen a VIP seat - enjoy your film!')
        weekend = input('Is your viewing at the weekend, yes or no? ')
        if weekend == 'yes':
            price = price * 1.5
            print('Weekend viewing adds on another 50%, sorry!')

    popcorn = input('Would you like popcorn, yes or no? ')
    if popcorn == 'yes':
        price = price + 1.25

You finish with the ``print`` statement as usual.  Now run your program again - there are now six routes or paths through your vip.py program - firstly, whether the seat chosen is VIP or not, and within this, whether it is weekend or not, and finally whether popcorn was purchased.  That is 3 possibilities, multiplied by two ways for each (either yes or no), to reach our six paths in the program.  See if you can run the vip.py program, with all of these possibilities tried out.

Exercises
---------

1. Modify your vip.py program so that the question, test and price increase for weekend seats occurs for both ordinary and VIP seats (i.e. move this part of the code outside the VIP block, and ensure the indentation is the same as the rest of the program).

2. Write a program called kiosk.py which prints out a menu of snacks to buy, e.g. Mars bar for 50p, Kitkat for 40p, Galaxy for 55p, Haribo for 30p (even better: make up your own items).  Ask the user to type in a choice (it could even be "1", "2", "3", etc.), and print out the correct price for the item chosen.

3. Write a program called weather.py which asks whether it is sunny or rainy or cloudy.  If the user types in "sunny", then tell the user to bring some sun cream.  If the user typed in "rainy", then tell the user to bring his umbrella.  If the user typed in "cloudy", then tell the user to bring his jumper.  Otherwise, just ignore the response.


Things to remember
------------------

1. Use the ``if`` statement to perform selection.  It is given an expression to evaluate, and if true, it will then execute the statements below the ``if`` statement.

2. Put a colon ``:`` at the end of the line containing the ``if``.

3. Statements grouped together belonging to an ``if`` statement is called a block of code.  It should be indented by 4 spaces, thus showing Python what code belongs to which test.

4. To resume the program regardless of whether the test for the ``if`` statement was successful or not, then you should unindent your code (push it back to the left by 4 spaces).

5. Use the double equals operator ``==`` to test whether the left-hand side of the expression is equal to the right-hand side.  Do not use the assignment operator ``=`` for this!
