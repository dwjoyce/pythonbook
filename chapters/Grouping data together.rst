Grouping data together
======================

.. quote:: Many people

    A programmer is a device for turning caffeine into code.

Scattered items
---------------

We have already covered variables, which just give a name to a piece of data.  This is very handy, and allows us to give data a memorable name we can refer to and modify later.  Technically, variable names (identifiers) are memory addresses that point to the data have stored - it is like a signpost pointing at the data.

However, it can become messy when there are many variables in our programs, especially if they are closely related.  For example, if we had a bunch of people's names, we could define each name individually.  Use the interactive shell to type in the following::

    >>> name1 = 'fred'
    >>> name2 = 'bob'
    >>> name3 = 'harry'
    >>> name4 = 'tom'
    
All the variables here describe the same kind of data - a group of names, one after the other.  It would be good if we could simply group these items together under a single name.  This is usually very good practice in programming - those things (whether code or data) that belong together should be kept together.

Boxing up
---------

The way we do this in Python is by using lists.  As its name suggests, a list is simply a sequence of other pieces of data, whether integers, floats, strings or even other lists.

Remember, if we have more than one item to print out, we simply use a comma ``,`` in-between each item.  This is easy to forget!  For example, if we wish to print out our names above, you can type the following::

    >>> print(name1, name2, name3, name4)
    fred bob harry tom
    
We do the same in lists to separate each item.  To define a list, to group a sequence of items together, we simply use brackets - square ones.  It is like a box grouping the values together.  So, for example, let's group together the names we defined earlier::

    >>> names = ['fred', 'bob', 'harry', 'tom']
    
Notice how we have done away with the individual variables, eg. name1, name2, etc., and now only have ones name, ``names``.  This means all four values are referred to by the same variable name - the entire list is given a single name.  You can print out the entire list in one go as well::

    >>> print(names)
    ['fred', 'bob', 'harry', 'tom']

This list is a sequence containing four strings - the names 'fred', 'bob', 'harry' and 'tom'.  As mentioned above, lists can contain almost anything, so let's try a list containing different data::

    >>> my_ints = [1, 2, 3, 4, 5]
    >>> my_floats = [2.5, 17.2, -1.7, 123.9]
    >>> my_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    
Notice how the contents of the list can be in any order you wish, although it can be sorted later.  The last one is slightly complicated - it is a list containing four sub-lists, each of which contain three integers.  A list of lists, or sometimes referred to as a :term:`matrix`.  The data can even be mixed, although this does not always make sense.  Try this::

    >>> my_stuff = ['bacon', 123, 99.5, [1, 44.2, 'fred']]
    
Again, you can print these list out using the ``print`` function.  Try it with each list in turn.

Playing with lists
------------------

We can do all sorts of things with lists in Python that can turn out to be very useful.  To get Python to sum up a group of numbers, we can just put them in a list and use the ``sum`` function::

    >>> numbers = [1, 5, 50, 23, 77]
    >>> sum(numbers)
    156
    
And other functions, ``min`` and ``max``, will give the minimum and maximum value out of a list::

    >>> numbers = [10, 123, 40, 89, 65]
    >>> min(numbers)
    10
    >>> max(numbers)
    123

You can even get Python to sort a list in any order you wish.  Try this out::

    >>> numbers = [15, 5, 35, 10, 25, 20, 30]
    >>> print(sorted(numbers))
    [5, 10, 15, 20, 25, 30, 35]
    >>> print(sorted(numbers, reverse=True))
    [35, 30, 25, 20, 15, 10, 5]
    
The first print statement prints out the numbers in ascending order.  The second prints out the numbers in descending (i.e. reverse) order.  Notice how we call ``sorted`` function initially with one argument (i.e. the list to sort), and secondly, we call the same function but we an extra argument we refer to by name - ``reverse``, which we set to True.  We will cover this kind of argument passing in chapter 19 when we are creating our own functions.

Lists can also be modified after they have been defined by using the ``append``, ``insert`` and ``del`` functions within the list variable itself.  The ``append`` function adds a new item onto the end of the list; ``insert`` adds an item into the list (so you need to give a position as well), and del is a built-in function to get rid of a variable (or part of a list, in this case).  We will cover how to index lists properly in the next chapter.  To see how this works, try out the following::

    >>> names = ['Bilbo', 'Frodo', 'Sam']
    >>> print(names)
    ['Bilbo', 'Frodo', 'Sam']
    >>> names.append('Pippin')
    >>> print(names)
    ['Bilbo', 'Frodo', 'Sam', 'Pippin']
    >>> names.insert(0, 'Merry')
    >>> print(names)
    ['Merry', 'Bilbo', 'Frodo', 'Sam', 'Pippin']
    >>> del names[1]
    >>> print(names)
    ['Merry', 'Frodo', 'Sam', 'Pippin']
    
.. todo:: Perhaps the previous section on modifying lists should be in the slicing chapter.

We can split a sentence into a lit of words using the split command::

    >>> sentence = 'Mary had a little lamb'
    >>> sentence.split()
    ['Mary', 'had', 'a', 'little', 'lamb']
    
We can also find out whether a value is a member of a list (i.e. is contained within the list) by using the ``in`` operator.  Try this out::

    >>> numbers = [1, 2, 3, 4, 5]
    >>> 3 in numbers
    True
    >>> 10 in numbers
    False
    >>> 
    >>> sentence = 'jack and jill ran up the hill'.split()
    >>> 'jack' in sentence
    True
    >>> 'jill' in sentence
    True
    >>> 'bob' in sentence
    False
    >>> 
    >>> breakfast = ['porrige', 'toast', 'coffee', 'juice', 'bacon', 'egg']
    >>> 'waffle' in breakfast
    False
    >>> 'pancake' in breakfast
    False
    >>> 'egg' in breakfast
    True
    
All of these things would have been much harder to do by ourselves - Python is great at helping out in this way.  There is so much to what Python offers, but here we have at least given a brief overview.

We will learn how to dip into a list to fetch individual items (or a section of the list) in the next chapter.  We learn how to step over a list, one item at a time, in two chapters time.  All this will make our programs easier to write.

Rock, Paper, Scissors
---------------------

Let's write a rock, paper, scissors game, where you play versus the computer.  The computer will use the random module we learnt in the previous chapter to choose one option out of either rock, paper or scissors, and we will do the same.  The program will compare the choices, and declare a winner (or possibly, a draw).

Start by opening up a new file window, and type in the following::

    import random
    
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        user_choice = input('Enter your choice, rock, paper'
                            ' or scissors (or stop to quit): ')
        if user_choice == 'stop':
            break

This should be fairly familar to you now.  We are importing the ``random`` module, and we have a loop which repeats until the user breaks out by entering the word 'stop'.

The new bit is the second line, where we define a list with the possible choices contained (boxed up) in a list, which we call ``choices``.  It is a list of strings.  We can then add onto our program (watch the indentation, these lines are *within* the while loop)::

    computer_choice = random.choice(choices)
        
This is also new - we are using a different function from the random module called ``choice``.  It takes a list, and returns back one item selected in a random fashion from that list.  We now have both choices needed in order to declare a winner - remember what the rules of the game are - rock beats scissors, scissors beats paper, paper beats rock.  So we can now finish::

    if user_choice == computer_choice:
        print('Draw!')
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or
          (user_choice == 'scissors' and computer_choice == 'paper') or
          (user_choice == 'paper' and computer_choice == 'rock')):
        print('You won!')
    else:
        print('Computer won!')
            
And that's it!  Now save and run your program calling it rockpaperscissors.py (or rps.py if you like).  

Notice how we can split a large test (the one attached to the ``elif`` testing whether the user has won or not) over 3 lines to make it more readable by putting parentheses around the entire expression.  Otherwise Python will complain.

There is one problem with our program - if the user does not type in exactly either 'rock or 'paper' or 'scissors', then the computer always wins.  Look at the tests - it fails the first test (the two choices cannot be equal), and it also fails the second test (as the user_choice is none of the possible values provided).  This is where we can use the ``in`` operator we described above.

Therefore, modify the long ``if`` statement in your rps.py program so it includes the new lines below::

    if user_choice not in choices:
        print('Not a valid choice, please try again.')
    elif user_choice == computer_choice:
        print('Draw!')
    elif ((user_choice == 'rock' and computer_choice == 'scissors') or
          (user_choice == 'scissors' and computer_choice == 'paper') or
          (user_choice == 'paper' and computer_choice == 'rock')):
        print('You won!')
    else:
        print('Computer won!')

Careful - you need to enter the first two new lines, and also change the existing ``if`` to an ``elif`` - otherwise, there would be two independant ``if`` statements instead of a series of tests following on from one another.

Now try our your program again.  It should behave itself whatever the user types in.

Exercises
---------

1. Modify your rps.py program so that it prints out what the choices were, particularly the computer choice.  It is nice for the user to know how they won or lost a game!

2. Write a program called sizes.py to use the ``turtle`` module to draw a shape (e.g. a circle) with a fill color randomly selected.  You could defined your colors such as ``colors = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow']``, and use the ``random.choice`` function to choose between them, passing the result into ``turtle.fillcolor`` function.  Don't forget to call ``turtle.begin_fill`` and ``turtle.end_fill`` before and after drawing your shape, respectively!

Things to remember
------------------

1. To group a number of items together we box them together using square brackets, with an opening bracket ``[`` at the beginning, and a closing bracket ``]`` at the end.

2. Separate each item within the list using a comma.

3. Use the ``in`` operator to test whether a value is contained by the list.

4. Use the ``choice`` function from the ``random`` module to select one item, chosen in a random fashion, from a list of possible items.

5. We now know five types of data - integers, floats, strings, booleans and lists.  Lists can contain any of the other types of data, including sub-lists!
