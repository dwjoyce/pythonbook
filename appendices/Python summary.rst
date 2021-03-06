:orphan:

Python summary
==============

.. quote::
    :author: Jack Sparrow
    :source: Pirates of the Caribbean: On Stranger Tides

    I understand everything! Except that wig.

This chapter summarises what we have learnt about the Python programming language.  It is only a subset of the total language, but it is enough for you to do your coursework well.

Examples
--------

This section lists a number of examples using various parts of the Python languages to achieve a variety of tasks.  Refer to this when you need an example of how to do something, from printing out messages or numbers, making decisions, performing loops or catching errors.

Note that comments start with the ``#`` character.

The ``print`` :term:`function` to print to the screen::

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

Using :term:`variables` to store values in memory::

    a = 10
    b = a + 20
    my_name = 'Fred'
    my_age = 101
    print('hello there', my_name, 'you are', my_age, 'old')

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

Reading :term:`input` from the user (using a function)::

    name = input('What is your name? ')
    print('Hello there', name)

Converting from one :term:`type` to another::

    age_str = input('What is your age? ')
    age = int(age_str)  # converts from a str to int
    print('In 10 years time you will be', age + 10)
    num_int = 10
    num_float = float(num_int)
    num_float2 = num_int * 10.0  # performs float calculation
    day = 18
    print('The date today is the', str(day) + 'th')  # join strings together

Using code from other programs (:term:`modules`)::

    import turtle
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

:term:`Looping` (repeating the same code whilst a test is ``True``)::

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

:term:`Sequences`::

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

:term:`Defining functions` allows us to organise our code better::

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

Reading from a :term:`file` on disk::

    my_file = open('textfile.txt')
    for line in my_file:  # step through file line by line
        print(line)
    my_file.close()

Writing to a file on disk::

    # Open output file, and then write lines to file and close
    output_file = open('test.txt', 'w')  # 'w' for writing

    output_file.write('first line\n')  # note newline symbol

    lines = ['second line\n', 'third line\n']
    output_file.writelines(lines)

    output_file.close()

Catching :term:`exceptions`::

    try:
        number_str = raw_input('Give me a number: ')
        number = int(number_str)  # Try converting it to an int
        print('Another 10 added on is:', number + 10)
    except:
        # If not an integer, an error will be thrown
        print('That was not a number!!')
    # Now carry on as normal...


Operators
---------

The most commonly used operators in Python.

Arithmetic operators
^^^^^^^^^^^^^^^^^^^^

========  ======================================
Operator    Description                                  
========  ======================================
 ``+``      Addition
 ``-``      Subtraction
 ``*``      Multiplication
 ``/``      Division
 ``**``     Power
 ``//``     Floor division (Whole number division)
 ``%``      Modulus (remainder)
========  ======================================

Examples::

    >>> 10 + 20 * 2
    50
    >>> 100 / 4 - 3
    22.0
    >>> 10 / 4
    2.5
    >>> 10 // 4
    2
    >>> 9 % 4
    1
    >>> 2 ** 8 + 1
    257

Assignment operators
^^^^^^^^^^^^^^^^^^^^

========  ======================================
Operator    Description                                  
========  ======================================
 ``=``      Assign expression to variable
 ``+=``     Add expression to variable     
 ``-=``     Subtract expression from variable
 ``*=``     Multiple expression to variable
 ``/=``     Divide expression into variable
 ``**=``    Performs power to variable
 ``//=``    Floor division into variable
 ``%=``     Modulus into variable
========  ======================================

Examples::

    >>> a = 10
    >>> a += 1   # a is 11
    >>> a -= 3   # a is 8
    >>> a *= 2   # a is 16
    >>> a /= 4   # a is 4.0
    >>> a **= 3  # a is 64.0
    >>> a //= 2  # a is 32.0
    >>> a %= 25  # a is 7.0

Comparison operators
^^^^^^^^^^^^^^^^^^^^

========  ======================================
Operator    Description                                  
========  ======================================
 ``==``     Equal to
 ``!=``     Not equal to
 ``<``      Less than
 ``>``      Greater than
 ``<=``     Less than or equal to
 ``>=``     Greater than or equal to
========  ======================================

Examples::

    >>> a, b, c = 10, 15, 5
    >>> a == b
    False
    >>> a != b
    True
    >>> a < b
    True
    >>> a >= c
    True
    
Bitwise operators
^^^^^^^^^^^^^^^^^

========  ======================================
Operator    Description                                  
========  ======================================
 ``<<``     Shift bits to the left
 ``>>``     Shift bits to the right
 ``&``      Bitwise and (set to 1 when both are 1) the bits together
 ``|``      Bitwise or (set to 1 when either are 1) the bits together
 ``~``      Return compliment - all the 1's and 0's are flipped
 ``^``      Bitwise exclusive or the bits together, unless both are 1 when the result is 0
========  ======================================

Examples::

    >>> 8 << 1
    16
    >>> 16 >> 2
    4
    >>> 127 & 15
    15
    >>> 10 | 5
    15
    >>> 10 ^ 15
    5

Logical operators
^^^^^^^^^^^^^^^^^

========  =============================================================
Operator    Description                                                         
========  =============================================================
 ``and``    If both operands are true, then condition is true
 ``or``     If either of the operands is true, then the condition is true
 ``not``    Reverses the condition                                       
========  =============================================================

Examples::

    >>> a, b, c = 10, 15, 5
    >>> a > b and a > c
    False
    >>> a > b or a > c
    True
    >>> not a == b
    True

Membership operators
^^^^^^^^^^^^^^^^^^^^

========  =======================================================================
Operator    Description                                                                   
========  =======================================================================
 ``in``     Condition is true if the value or variable is contained in a sequence
========  =======================================================================

Examples::

    >>> 'a' in 'abc'
    True
    >>> 'ab' in 'abc'
    True
    >>> 'abcd' in 'abc'
    False
    >>> num = 10
    >>> num in [5, 10, 15, 20]
    True
    >>> num in [0, 20, 40, 60]
    False

Operator precedence
^^^^^^^^^^^^^^^^^^^

The following table summarises the operator precedences in Python, from lowest precedence (least binding) to highest precedence (most binding). Operators in the same box have the same precedence - so they are evaluated from left to right.  If in doubt, use parentheses ``(`` ``)`` to force a particular order!

===================================================================================== ========================================================================
Operator                                                                              Description
===================================================================================== ========================================================================
``or``                                                                                Boolean OR
``and``                                                                               Boolean AND
``not``                                                                               Boolean NOT
``in``, ``not in``, ``is``, ``is not``, ``<``, ``<=``, ``>``, ``>=``, ``!=``, ``==``  Comparisons, including membership tests and identity tests
``|``                                                                                 Bitwise OR
``^``                                                                                 Bitwise XOR
``&``                                                                                 Bitwise AND
``<<``, ``>>``                                                                        Shifts
``+``, ``-``                                                                          Addition and subtraction
``*``, ``/``, ``//``, ``%``                                                           Multiplication, division, remainder
``+x``, ``-x``, ``~x``                                                                Positive, negative, bitwise NOT
``**``                                                                                Exponentiation
``x[index]``, ``x[index:index]``, ``x(arguments...)``, ``x.attribute``                Subscription, slicing, call, attribute reference
``(expressions...)``, ``[expressions...]``, ``{key: value...}``, ``{expressions...}`` Binding or tuple display, list display, dictionary display, set display
===================================================================================== ========================================================================


Data types
----------

.. pythontest:: nooutput

Python allows more one type of data.  Whilst calculators generally deal with only numbers, computers can store all sorts of data that can be interpreted in different ways.  In addition to numbers (integers, floating point), programs can also process strings of characters, lists of values, files to store data on a more permanent basis.  A bit of interpretation is required (the type itself) as all this data is invariably stored in binary.

Essentially, a data type determines the size of the data being stored, a set of permitted values, and the operations that can be performed on the data.  Obviously, we can divide an integer by 2, but it would make no sense to divide a telephone number or someone's address by 2 - that operation is not permitted by strings.
 
The following table summarises the types of data we have introduced in this book, along with examples of their values and operations you can perform on them:

- **integers (int)** - integers are whole numbers, such as -1, 0, 1, 2, 3, 4, and so on.  You convert to an integer data type using the ``int`` function.  However, when doing so, make sure the argument passed in is an actual number, or else an error will be raised.  If a floating point number is passed in, then the fractional part is dropped.  If a string is passed in, ensure that the string contains a single whole number, without even a fractional part.

  The operations that can be performed on an integer mainly include the arithmetic operators, such as ``+``, ``-``, ``*``, ``/`` (which results in a floating point answer), ``//`` (which results in an integer answer), ``**`` and ``%``.

  For example::

      >>> 10 * 4 + 21 // 2    # results in 50
      >>> 10 * 4 + 21 / 2     # results in 50.5
      >>> 2 ** 8              # results in 256
      >>> 10 % 6              # results in 6 (remainder of 10 divided by 6)
      >>> int("123")          # results in number 123
      >>> int(123.5)          # also results in number 123
      >>> int(input('num?'))  # convert from number

- **floats (float)** - floating point numbers are fractional numbers that contains a whole number and a fractional part, such as -10.5, 0.0, 1.75, 15.0.  You convert to a float data type using the ``float`` function.  Make sure the argument passed in is an actual number, whether just a whole number or one already containing a fraction.

  The operators that can be performed on a floating point number are the same as integers.
  
  For example::

      >>> 10.0 * 4 + 21 // 2     # results in 50.5
      >>> 10.0 * 4 + 21 / 2      # also results in 50.5
      >>> 2.0 ** 8               # results in 256.0
      >>> 10.0 % 6               # results in 4.0
      >>> float("123")           # results in number 123.0
      >>> float(123.5)           # results in number 123.5
      >>> float(input('num?'))   # convert from input to number
      
- **strings (str)** - strings are a sequence of alphanumeric characters, such as those found on your keyboard.  You can convert to a string data type using the ``str`` function.  You can pass almost anything into this function in order to get its string representation.

  Although you can join and repeat strings by using the ``+`` and ``*`` operators, respectively, you can also use methods belonging to the string type or class to perform operations contained by the string value or object.
  
  For example::
  
      >>> name = 'General Ike'
      >>> capitalised = name.upper()
      >>> new_name = name.replace('General', 'President')
      >>> repeated = 'Fred' * 100
      >>> joined_up = 'Fred' + 'Bloggs' + str(10)
      >>> num_to_str = str(123.456)

- **booleans** - booleans are either ``True`` or ``False``, and are produced when you compare values or combine comparisons.  You can convert to a boolean data type using the ``bool`` function.

  For example::
  
      >>> 10 < 20          # results in True
      >>> run = True       # sets run to True
      >>> run and 10 < 20  # results in True
      >>> not run          # results in False

- **lists** - sequences of items of any type.  A list is simply a sequence of items, such as a range of numbers, a list of names or months.  You can convert to a list data type using the ``list`` function.

  For example::

      >>> list('abcdefg')
      >>> tunnels = 'tom dick harry'.split()
      >>> spring = ['Mar', 'Apr', 'May']
      >>> sorted(spring)
      >>> list(reversed(spring))
      >>> spring.append('gorilla')
      >>> spring[0]
      
- **files** - a value or object pointing to an open file.  You specify its name when opening the file, including its path if necessary, and optionally the mode in which you wish to open it - ``'r'`` for reading, ``'w'`` for writing.

  For example::

      >>> my_file = open('shopping-list.txt')
      >>> my_file.read()
      >>> my_file.readlines()
      >>> my_file.close()
      
      >>> new_file = open('todo.txt', 'w')
      >>> new_file.write('Finish computing coursework\n')
      >>> new_file.writelines(['one\n', 'two\n', 'three\n'])
      >>> new_file.close()
      
      
Different types of functions
----------------------------

In this section we will briefly describe the four general types of functions in Python:

Built-in functions
^^^^^^^^^^^^^^^^^^

You can see the list of built-in functions by typing ``dir(__builtins__)`` in the interactive interpreter.  Here is a list of the most useful ones, particularly the ones we have covered in this book with a brief note and example on each:

  ============== ====================================================================================  =====================
  Name           Description                                                                           Example
  ============== ====================================================================================  =====================
  ``all``        Returns ``True`` if all values in supplied sequence (iterable) are also ``True``      ``all(my_list)``
  ``any``        Returns ``True`` if any values in supplied sequence (iterable) are ``True``           ``any(my_list)``
  ``abs``        Returns the absolute (positive) value of an integer or float                          ``abs(-10)``
  ``bin``        Returns the binary number equivalent of the supplied integer as a string              ``bin(123)``
  ``bool``       Converts the supplied value into a boolean value                                      ``bool(1)``
  ``chr``        Returns the character equivalent of the supplied ordinal (integer) number             ``chr(65)``
  ``dir``        Returns a (directory) listing of the imported module                                  ``dir(math)``
  ``divmod``     Divide one number by another, and returns the quotient and remainder in a sequence    ``divmod(10, 8)``
  ``enumerate``  Supply a sequence, return a sequence of items paired with their index from ``0``      ``enumerate('abc')``
  ``exit``       Exit your program early (same as ``quit``)                                            ``exit()``
  ``float``      Converts the supplied value into a floating point (fractional) number                 ``float('1.5')``
  ``hex``        Converts the supplied value into a hexadecimal value as a string                      ``hex(127)``
  ``help``       Provides help on the supplied item                                                    ``help(input)``
  ``id``         Returns the memory address of the supplied name                                       ``id(my_num)``
  ``input``      Waits on the user to type something, and return sequence of characters as a string    ``input('name? ')``
  ``int``        Convert the supplied value into an integer number                                     ``int('100')``
  ``len``        Returns the length of the supplied sequence (e.g. string or list)                     ``len('fred')``
  ``list``       Converts the supplied value into a list                                               ``list('xyz')``
  ``max``        Returns the maximum value from the supplied sequence                                  ``max(1, 2, 3)``
  ``min``        Returns the minimum value from the supplied sequence                                  ``min(5, 1, 3)``
  ``oct``        Converts the supplied value into an octal value as a string                           ``oct(25)``
  ``ord``        Returns the supplied character into an ordinal (integer) value                        ``ord('a')``
  ``open``       Open the supplied filename and return the opened file                                 ``open('scores.txt)``
  ``pow``        Calculate the power of one number to another and return the result                    ``pow(2, 8)``
  ``print``      Print out or display the supplied string or list of items                             ``print('Hello')``
  ``range``      Provide a range of integers, with a set start, stop and step                          ``range(10, 20, 2)``
  ``reversed``   Reverse the order of a supplied sequence                                              ``reversed('abcde')``
  ``round``      Round the supplied floating point number to the specified precision                   ``round(4.75)``
  ``sorted``     Return the supplied sequence in order                                                 ``sorted('azgdbdc')``
  ``str``        Convert the supplied value into a string                                              ``str(100)``
  ``sum``        Sum or add up the supplied sequence of numbers returning the result                   ``sum([1, 3, 5, 7])``
  ``type``       Return the type of the supplied item, e.g. ``int``, ``float``, ``str``, ``bool``      ``type('bob')``
  ``zip``        Zips up or combines two or more supplied sequences                                    ``zip('abc', 'def')``
  ============== ====================================================================================  =====================

The full list will include other built-in items as well (e.g. exception types).  These can be called by any Python program without having to import anything else – they are built-in to the language itself.

Local functions
^^^^^^^^^^^^^^^

You can define your own functions in your Python module by using the ``def`` keyword.  These can then be called from within your own program by simply using the name of the function itself, similar to a built-in function.  For example, here is a function that accepts a number and returns its square::

    def square_number(number):
        return number * number

Which can then be called as follows::

    square_number(5)  # returns 25

Imported functions
^^^^^^^^^^^^^^^^^^

You can use functions in other modules by importing them first.  For example, to use functions inside the ``math`` module, you can do the following::

    import math
    math.sqrt(100)

You need to write module name followed by a period ``.`` before the name of the function when calling it.  You can print out a directory listing of what a module contains by performing a 'dir' on its name, for example::

    >>> dir(math)

Functions belonging to a type ("class methods")
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A particular set of values is called a type (integers, floating point numbers, strings, files) or a class.  These types wrap up the data they contain, and also offer functions that operate on that data.  This allows the data and related code to live in one place.  For example, once you have defined a string, you can calls its type or class methods (functions) to perform a number of operations on that string value::

    >>> message = 'the quick brown fox jumps over the lazy dog'
    >>> message.upper()  # returns the uppercase version
    >>> message.split()  # returns a list of words
    >>> message.replace('fox', 'coyote')  # replaces one word with another
    >>> message.count('o')  # returns how often one string is in another
    >>> message.startswith('the')  # does string start with this?
    
And so on.  You need to write the variable name (which refers to a piece of data, or object, belonging to a particular type), followed by a period ``.`` before the name of the function when calling it.  You can list the functions that a type contains by performing a ``dir`` on its name, for example::

    >>> dir(int)
    >>> dir(float)
    >>> dir(str)

This will show that some types have functions that are not relevant to other types.  For example, floats have a function called ``is_integer`` which returns ``True`` if it is a whole number, ``False`` if not.  Strings have functions such as ``lower``, ``split``, ``title``, ``upper``, which are relevant to strings of characters, but not numbers and files.  These methods are bound up with the data they work on, so only relevant functions are offered with the type of data the variable refers to.

Keep in mind that if you call a function to change its value, some functions will change the data referred to by the variable name, and others will return a new value.  This means that some types can change their values (e.g. lists, where you can ``append``, ``insert`` or ``remove`` values), and others cannot so give you a new value (e.g. integers, floats and strings).  Therefore, all the calls on the ``message`` variable above, being a string, would return a new value if you tried to change it (e.g. changing the string to uppercase or replacing values).  You could then assign this new value to a variable name using the assignment ``=`` operator.

Here are a few more examples to show this difference between types that allow the value to change (*mutable*) and types that do not (*immutable*)::
    
    >>> hobbits = ['Bilbo', 'Frodo', 'Sam']
    >>> hobbits.append('Pippin')  # changes value
    >>> hobbits.remove('Bilbo')   # changes value

    >>> num = 10
    >>> num = num + 1   # new value
    >>> num = num * 10  # new value
    
    >>> name = 'The 11th Doctor'
    >>> big_name = name.upper()  # new value
    >>> new_name = name.replace('11th', '12th')  # new value
    
Functions that change the existing value, rather than returning a new one, are known as in-place operations - they change the data where it lives or is placed in memory, rather than creating a new value with different contents.  It is a subtle but vital point!


Program layout
--------------

When a program gets past a few lines, including its own function definitions and the like, you need to structure your program in an orderly fashion to avoid it becoming messy.  The general structure of a Python program should follow this pattern::

    # firstly import any modules you need, e.g.
    import math
    
    # define constant variables (variables whose values don't change), e.g.
    MULTIPLIER = 2


    # function definitions, e.g.
    def get_integer():
        number = input('Give me a number: ')
        return int(number)


    def double_up(num):
        return num * MULTIPLIER
        
    # main code, e.g.:
    number = get_integer()
    
    print('Number doubled is:', double_up(number))
    print('and its factorial is:', math.factorial(number))
    print('Bye for now.')

.. pythontest:: all
