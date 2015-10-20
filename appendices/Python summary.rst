:orphan:

Python summary
==============

.. quote::
    :author: Jack Sparrow
    :source: Pirates of the Caribbean: On Stranger Tides

    I understand everything! Except that wig.

This short chapter summarises what we have learnt about the Python programming language.  It is only a subset of the total language, but it is enough for you to do your coursework well.
Refer to it when you need an example of how to do something, from printing out messages or numbers, making decisions, performing loops or catching errors.

Note that comments start with the ``#`` character.

The ``print`` function to print to the screen::

    print("Hello, World!")
    print('I will meet you at Fred\'s house')  # quote in quote
    print('My name is', 'David', 'and my age is', 21)
    print('I love Python ' * 1000)
    print('two strings' + 'joined together')

Arithmetic::

    # add, multiply, divide, subtract, power,
    # remainder (modulo) - but not in that order!
    print(3 + 4 * 10 / 2 - 5 ** 2 % 5)
    
    print(3 + 4 * 5)    # will print 23
    print((3 + 4) * 5)  # will print 35, brackets go first!

Using variables to store values in memory::

    a = 10
    b = a + 20
    my_name = 'Fred'
    my_age = 101
    print('hello there', my_name, 'you are', my_age, 'old')
    print('hello there %s you are %d old' % (my_name,
                                             my_age))  # inline formatting

Getting help in :term:`IDLE`::

    dir(__builtins__)  # list all the builtin functions
    help(range)  # display help on the range function
    help('modules')  # list all the supplied modules
    dir(str)  # or dir(int), dir(float), dir(list)
    help(str.isdigit)  # or help(str), help(float), help(list)

Calling :term:`functions` (pieces of code that you can use easily)::

    # Putting () after function names means you are calling (invoking) it
    print(abs(-123))  # prints 123 (makes number positive)
    print(len('Hello there'))  # length of a sequence
    print(ord('a'))  # print out ordinal number of a character
    print(bin(183))  # prints binary 10110111
    print(hex(183))  # prints hexadecimal B7
    print(int('10110111', 2))  # prints decimal 183

Reading input from the user (using a function)::

    name = input('What is your name? ')
    print('Hello there', name)

Converting from one :term:`type` to another::

    age_str = input('What is your age? ')
    age = int(age_str)  # converts from a str to int
    print('In 10 years time you will be', age + 10)
    num_int = 10
    num_float = float(num_int)
    num_float2 = num_int * 10.0  # performs float calculation

Using code from other programs (:term:`modules`)::

    import turtle
    turtle.Turtle()  # make sure the 'T' in the function call is uppercase!
    turtle.circle(100)
    dir(turtle)  # provide a directory listing of module
    help(turtle.fillcolor)  # help on a particular item

Taking decisions using ``if`` statement (:term:`operators` you can use are: ``==``, ``>``, ``<``, ``<=``, ``>=``, ``!=``, ``in``, ``and``, ``or``, ``not``)::

    a = 10
    b = 20
    if a > b:
        print('a is larger than b')
    elif b > a:  # means "else if"
        print('b is larger than a')
    else:  # catch all when other tests are False
        print('a and b are the same')

    if a in range(10, 20):  # check if in range of numbers
        print('a is between 10 and 20!')


Looping (repeating the same code whilst a test is ``True``)::

    a = 10
    b = 20
    while a < b:  # print out numbers between a and b
        print(a)
        a = a + 1  # or a += 1

    while True:  # loop forever
        input_str = input('what is your name or quit? ')
        if input_str == 'quit':
            break  # escape from loop
        print('Hello there', input_str)

To generate :term:`random` numbers, we use the ``random`` module::

    import random
    print(random.randrange(1, 100))  # random number between 1 - 100
    print(random.random())  # random number between 0.0 - 1.0

Sequences::

    import random

    # Make a list of items using the square brackets []:
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    print(random.choice(month_names))  # print random month

    print(month_names[0])    # prints Jan, indices start from 0
    print(month_names[5])    # prints Jun
    print(month_names[-1])   # prints Dec
    print(month_names[-2])   # prints Nov
    print(month_names[2:5])  # prints Mar, Apr, May

    friends = ['Tom', 'Dick', 'Harry']
    friends.append('Fred')  # append a new item onto list
    print(len(friends))  # will now print out 4

``for`` loops make stepping through sequences (or looping) very easy::

    for letter in 'hello there':
        print(letter)

    for num in range(100):  # range creates a list of numbers
        print(num)

    for name in ['tom', 'dick', 'harry']:
        print('Hello there', name)

    breakfast = ['bacon', 'egg', 'tomato', 'mushroom', 'bread']
    for item in breakfast:
        print('Yum, I\'m having', item, 'for breakfast.')

Defining functions allows us to organise our code better::

    def say_hello():
        print('hello')


    def say_hello_times(times):
        print('hello' * times)


    def square_number(number):
        return number * number


    def lowest_highest(numbers):  # accepts a list of numbers
        lowest = min(numbers)
        highest = max(numbers)
        return lowest, highest  # returns two values

    say_hello()
    say_hello_times(10)
    print(square_number(5))  # prints 25
    low, high = lowest_highest([5, 10, 35, 15, 50, 20])

Reading from a file on disk::

    my_file = open('textfile.txt')
    for line in my_file:  # step through file line by line
        print(line)
    my_file.close()

Writing to a file on disk::

    # Open output file, and then write lines to file and close
    output_file = open('test.txt', 'w')  # 'w' for writing

    output_file.write('first line\n')  # note new line symbol

    lines = ['second line\n', 'third line\n']
    output_file.writelines(lines)

    output_file.close()

Catching errors::

    try:
        number_str = raw_input('Give me a number: ')
        number = int(number_str)  # Try converting it to an int
        print('Another 10 added on is:', number + 10)
    except:
        # If not an integer, an error will be thrown
        print('That was not a number!!')
    # Now carry on as normal...
