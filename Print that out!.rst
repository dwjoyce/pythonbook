Print that out!
===============

Printing numbers
----------------

Now that we have started writing proper programs that can be saved and run over and over, we will soon discover a little problem.

To see this, open up a new file (click on the *File* menu and select *New File*), and type in the following into the new window that appears::

  a = 10
  b = 20
  c = a + b
  c

This is just the same code as we did in Chapter 2 when working with variables for the first time.  However, back then, we typed in each individual line in the interactive shell, and it gave an answer every time.

What happens now, given that it is living in its own program?  Try it and see - press the ``F5`` key, click ``OK`` to save it and give it the name sum.py.  Remember, the ".py" postfix stands for Python.  Try and save all your programs onto your USB stick.

When the program runs in the run window (the same as the interactive shell), what does it display onto the screen?  Does it give 30 as expected?  No, it does not!

The reason for this is that just typing a value (e.g. ``10``) or an expression to be evaluated (e.g. ``10 + 20``) or a variable name (``c`` in the example above) will do nothing in a real program.  The interactive shell is just that - interactive.  But in a real program, you have to tell it what to do with the item you are dealing with.  Otherwise, Python will simply discard the value.

So what do we want to do with the variable ``c`` above?  We want to display or print it out onto to the screen.  In Python, the way to do this is to use the ``print`` function.  You simply wrap your value to display in the ``print()`` call, and it will then print it out as you originally intended.  Therefore, modify your program so it looks like this::

  a = 10
  b = 20
  c = a + b
  print(c)

Run your program again, using the ``F5`` key (you may have to click the ``OK`` button, or just press the Return key to confirm).  This should now print out the number 30 in the run window.

You can print out more than one item by using a comma ``,`` between the items to separate them.  Modify your program again::

  a = 10
  b = 20
  c = a + b
  print(a, b, c)

and run, again by using the ``F5`` key and pressing Return to confirm.  This will print out 10, followed by 20 and finally 30, all on the same line.

You can even get the print function to perform the calculation for you when passing in the values to print.  Again, modify your program like so::

  a = 10
  b = 20
  c = a + b
  print(a, b, c, a + b + c)

This will print out the three numbers from before (10, 20 and 30), and then 60 (the other numbers added together), all without the need of a fourth variable.

Printing messages
-----------------

Dealing with numbers all the time is very useful, but it is bit limiting.  Dealing with messages containing text is very easy, but subtly different.

To deal with text, we need to enclose the words with quotation marks, just like in the first book of the Bible:

  And God said, "Let there be light," and there was light.
  
In Python, it is similar, apart from missing out the words either side of the quotes!

Open up a new file (click on the ``File`` menu and select ``New File``), and type the following::

  print("Hello World!")
  print('How are you?')
  print("I love Python")
  print('This is fun!')
  
Save this file as lines.py (press the ``F5`` button, press Return to confirm and save it onto your USB stick), and see the text being printed out onto the screen.  Notice how we use either double quotation marks ``"`` or single quotation marks ``'`` - Python does not mind which one you use, as long as you are consistent.  This means that if you start with a double quote, then you must close with a double quote.

These pieces of text in Python are called ``strings``.  Think of them as strings of characters, made up of either letters from the alphabet, digits or symbols.  This includes almost any key from your keyboard, and more besides.  Similar to a string of pearls, a ``string`` in programming is a sequence of characters.  Now we know three types of data - integers, floats and strings.

Now modify your lines.py program to include strings and integers together, below the lines you added previously::

  print("1 plus 2 equals:", 1 + 2)
  print("I am", 18, "years old")
  print("That bag of apples cost", 75, "pence")
  
Again note how we separate a number of items being printed together - using a comma between each.

We can even have a bit of fun, and join and replicate strings like so::

  print('One piece of text' + 'joined to another')
  print('How about this ' * 10)

Here we are using the addition operation ``+`` to join two items of text together, and then print out the result.  Notice, the result does not have a space between each item, as the other examples previously do.  This is called string concatenation.  The multiplication operation ``*`` is used to replicate the text however many times you specify - 10 times in this example.

Variables can also be assigned to strings.  Add the following onto your program, lines.py::

  name = 'Fred'
  occupation = 'Farmer'
  age = 25
  print('Here are my details:', name, occupation, age)
  
Finally, you can use special characters in strings to denote certain things.  Here I will introduce just three of them, so add these lines to finish::

  print('Here is a new line character\nThis is now on a separate line!')
  print('This is how to introduce a horizontal tab \t to space out my text')
  print('I love St. Michael\'s school - notice the quote inside the quote!')

The first one breaks the line with a new line character (``\n``), the second spaces out the text using a tab, and the third is a way of using quotes inside quotes, otherwise Python will get confused between an apostrophe (e.g. St. Michael's School) and the closing quotation mark.

Exercises
---------

1. Assign 5 variables to various numbers, and print them out, along with the sum
2. Print out the year of your birth, your age, and your age in 10 years time.
3. Print out the same as number 2, but with strings of text indicating what number is what, e.g. I was born in: 1999, my age: 16, in 10 years: 26
4. Print out your name a hundred times, with a tab (using the code ``\t``) to introduce space inbetween each item.

Things to remember
------------------

1. Use the ``print()`` function to display or output any expression onto the screen.
2. Separate the items to print using a comma.
3. A piece of text can be used by enclosing it in quotation marks, whether using single (e.g. ``'fred'``) or double quotes (e.g. ``"fred"``).
4. The only operators that can be used with text are addition (i.e. joining strings together, known as concatenation) and multiplication (replication).
5. Use the ``\n`` for newline, ``\t`` for tab and ``\'`` or ``\"`` (quotation marks) inside strings.
6. Text inside quotes is a string.
