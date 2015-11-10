:orphan:

Extra exercises
===============

.. quote::
    :author: William Shakespeare
    :source: Richard III

    Now is the winter of our discontent

These exercises are designed to allow you to practice your programming skills learned during class.  Please complete each each task and save in a folder called :file:`practice` on your USB stick to show the teacher when finished.  However, you need not complete the tasks in the order written - if you get stuck with one, move onto another and return to the first task later.

This work must be done on your own without help or assistance from others in the class.  However, you may consult your previous work, or the books and examples provided by the teacher, as you wish.

:file:`welcome.py`
------------------

Write a program that asks for the user's name and a number, and then prints out their name that number of times.

For example:

.. code-block:: none
    :pythontest: off

    What is your name? Snoopy
    How many times should I print your name: 5
    Snoopy Snoopy Snoopy Snoopy Snoopy


:file:`oddoreven.py`
--------------------

Write a program that inputs a number, and then tells the user whether the number is odd or even.

For example:

.. code-block:: none
    :pythontest: off

    Please input a number: 17
    The number 17 is odd.

    Please input a number: 42
    The number 42 is even.


:file:`century.py`
------------------

Write a program to input the user's name and age, and then print out a greeting including the user's name, and the year in which the user will be 100 years old.  Your program can assume the current year is 2015.

For example:

.. code-block:: none
    :pythontest: off

    What is your name: Fred
    How old are you? 99
    Hello Fred you will be 100 in 2016

    What is your name: Bob
    How old are you? 20
    Hello Bob you will be 100 in 2095


:file:`circlearea.py`
---------------------

Write a program that asks for the diameter of a circle, and prints out its area.  The area can be calculated as follows:

.. math:: area = \pi * r^2

.. hint:: For :math:`\pi`, import the module ``math`` and use ``math.pi``.

For example:

.. code-block:: none
    :pythontest: off

    Please enter the diameter of the circle: 12
    The area is: 113.10


:file:`drawline.py`
-------------------

Write a program to draw a line on the screen given two x and y coordinates, using the ``turtle`` module.

.. hint:: The turtle window has its 0,0 point at the centre, with increasing x and y in the right and up direction, respectively.  In other words, x starts at 0 in the centre and goes negative towards the left, and positive towards the right.  y starts at 0 in the centre and goes negative towards the bottom and positive towards the top.  This is somewhat like graph paper.

This is the turtle coordinate system illustrated (reference: :url:`http://101computing.net`):

.. image:: /images/extraex/image02.png
    :width: 200pt
    :align: center

You will need to create the turtle window using the ``Turtle`` function, to pick your pen up using the ``up`` function, and move using the ``goto`` function.

For example (drawn with a thicker pen using the ``pensize`` function on a 500x500 window):

.. code-block:: none
    :pythontest: off

    From where should the line start? -100 -200
    And to where should the line end? 275 175

.. image:: /images/extraex/image07.png
    :width: 200pt
    :align: center


:file:`countingdown.py`
-----------------------

Write a program to input a number from the user and then print all the numbers from this down to zero.  Make sure the number is positive!

For example:

.. code-block:: none
    :pythontest: off

    Please input a number: 10
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    0


:file:`span.py`
---------------

Write a program to ask for two numbers, and print the numbers that span from the first up to the second.  Care should be taken in the case that the second number is lower than the first number - you should always count up.

For example:

.. code-block:: none
    :pythontest: off

    Please input your first number: 10
    Please input your second number: 20
    The span of numbers are:
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19


:file:`squares.py`
------------------

Write a program to ask for two numbers, and print out the square of the numbers that span from the first number up to the second.  Care should be taken in the case that the second number is lower than the first number - you should always count up.

For example:

.. code-block:: none
    :pythontest: off

    Please input your first number: 10
    Please input your second number: 20
    The square numbers between those numbers are:
    100
    121
    144
    169
    196
    225
    256
    289
    324
    361


:file:`headstails.py`
---------------------

Write a program to ask the user how many times the program should flip a coin, and count how many times the coin landed on heads and tails.

.. hint:: Use ``random.choice`` function with a parameter of ``["heads", "tails"]`` to choose between the two options.

For example:

.. code-block:: none
    :pythontest: off

    How many times should I flip the coin? 1000
    The number of heads totalled 459 and the number of tails totalled 541


:file:`randompathtracer.py`
---------------------------

Write a program, using turtle, that asks the user for a number of steps. The program should then loop, and at each step, randomly turn the turtle left by 90 degrees, right by 90 degrees or not turn at all. It should then go forward by 10 pixels.

For example:

.. code-block:: none
    :pythontest: off

    How many steps should I draw? 500

.. image:: /images/extraex/image00.png
    :width: 200pt
    :align: center


:file:`ascii.py`
----------------

Write a program to print out a section of the :term:`ASCII` table.  It should print out the decimal, binary, hexadecimal and character representation for the values from 32 to 127, inclusive.  Use the built-in ``bin`` function to get the binary value, ``hex`` for the hexadecimal value and ``chr`` to get the character representation.

For example:

.. code-block:: none
    :pythontest: off

    32    0b100000    0x20     
    33    0b100001    0x21    !
    34    0b100010    0x22    "
    35    0b100011    0x23    #
    36    0b100100    0x24    $
    37    0b100101    0x25    %
    38    0b100110    0x26    &
    39    0b100111    0x27    '
    40    0b101000    0x28    (
    41    0b101001    0x29    )
    42    0b101010    0x2a    *
    43    0b101011    0x2b    +
    44    0b101100    0x2c    ,
    45    0b101101    0x2d    -
    46    0b101110    0x2e    .
    47    0b101111    0x2f    /
    48    0b110000    0x30    0
    49    0b110001    0x31    1
    50    0b110010    0x32    2
    51    0b110011    0x33    3
    52    0b110100    0x34    4
    53    0b110101    0x35    5
    54    0b110110    0x36    6
    55    0b110111    0x37    7
    56    0b111000    0x38    8
    57    0b111001    0x39    9
    58    0b111010    0x3a    :
    59    0b111011    0x3b    ;
    60    0b111100    0x3c    <
    61    0b111101    0x3d    =
    62    0b111110    0x3e    >
    63    0b111111    0x3f    ?
    64    0b1000000    0x40    @
    65    0b1000001    0x41    A
    66    0b1000010    0x42    B
    67    0b1000011    0x43    C
    68    0b1000100    0x44    D
    69    0b1000101    0x45    E
    70    0b1000110    0x46    F
    71    0b1000111    0x47    G
    72    0b1001000    0x48    H
    73    0b1001001    0x49    I
    74    0b1001010    0x4a    J
    75    0b1001011    0x4b    K
    76    0b1001100    0x4c    L
    77    0b1001101    0x4d    M
    78    0b1001110    0x4e    N
    79    0b1001111    0x4f    O
    80    0b1010000    0x50    P
    81    0b1010001    0x51    Q
    82    0b1010010    0x52    R
    83    0b1010011    0x53    S
    84    0b1010100    0x54    T
    85    0b1010101    0x55    U
    86    0b1010110    0x56    V
    87    0b1010111    0x57    W
    88    0b1011000    0x58    X
    89    0b1011001    0x59    Y
    90    0b1011010    0x5a    Z
    91    0b1011011    0x5b    [
    92    0b1011100    0x5c    \
    93    0b1011101    0x5d    ]
    94    0b1011110    0x5e    ^
    95    0b1011111    0x5f    _
    96    0b1100000    0x60    `
    97    0b1100001    0x61    a
    98    0b1100010    0x62    b
    99    0b1100011    0x63    c
    100    0b1100100    0x64    d
    101    0b1100101    0x65    e
    102    0b1100110    0x66    f
    103    0b1100111    0x67    g
    104    0b1101000    0x68    h
    105    0b1101001    0x69    i
    106    0b1101010    0x6a    j
    107    0b1101011    0x6b    k
    108    0b1101100    0x6c    l
    109    0b1101101    0x6d    m
    110    0b1101110    0x6e    n
    111    0b1101111    0x6f    o
    112    0b1110000    0x70    p
    113    0b1110001    0x71    q
    114    0b1110010    0x72    r
    115    0b1110011    0x73    s
    116    0b1110100    0x74    t
    117    0b1110101    0x75    u
    118    0b1110110    0x76    v
    119    0b1110111    0x77    w
    120    0b1111000    0x78    x
    121    0b1111001    0x79    y
    122    0b1111010    0x7a    z
    123    0b1111011    0x7b    {
    124    0b1111100    0x7c    |
    125    0b1111101    0x7d    }
    126    0b1111110    0x7e    ~
    127    0b1111111    0x7f 


:file:`vowel.py`
----------------

Write a program to input a character, and tell the user whether it is a vowel or not (i.e. one of these characters - a, e, i, o or u).  Make sure only a single character has been input.

For example:

.. code-block:: none
    :pythontest: off

    Please type one character from the alphabet: a
    The letter a is a vowel!

    Please type one character from the alphabet: z
    The letter z is not a vowel!

    Please type one character from the alphabet: E
    The letter E is a vowel!


:file:`prayers.py`
------------------

Write a program to offer an index of prayers, ask for a choice of one of them - or none at all - and print out that prayer in full.  Your choice of prayers is up to you.

For example:

.. code-block:: none
    :pythontest: off

    The choice of prayers is as follows:

    1) Apostles Creed, 2) Our Father, 3) Hail Mary, 4) Glory Be,
    5) Hail Holy Queen, 6) Exit

    What is your choice? 3
    Hail Mary, full of grace, the Lord is with thee; blessed art thou
    amongst women, and blessed is the fruit of thy womb, Jesus. Holy Mary,
    Mother of God, pray for us sinners, now and at the hour of death. Amen


:file:`palindrome.py`
---------------------

Write a program that will input a word, and then inform the user whether the word is a palindrome or not (i.e. words that when reversed, are the same).  So the words "nun", "radar" and "kayak" are palindromes.

For example:

.. code-block:: none
    :pythontest: off

    Input a word: bob
    The word bob is a palindrome!

    Input a word: fred
    The word fred is not a palindrome


:file:`histogram.py`
--------------------

Write a program that will accept a list of numbers and then draw a histogram using the star ``*`` character.

For example:

.. code-block:: none
    :pythontest: off

    Input the numbers for the histogram: 1, 3, 5, 4

    Here is the histogram for the numbers 1, 3, 5, 4:
    *
    ***
    *****
    ****


:file:`length.py`
-----------------

Write a program to input a list, and print out how long that list is.  Use ``sentence.split`` to split the sentence returned by ``input`` into a list of items.
For example:

.. code-block:: none
    :pythontest: off

    Please input your sentence: a b c 1 2 3
    The number of items in your sentence is: 6

    Please input your sentence: monday tuesday wednesday
    The number of items in your sentence is: 3


:file:`turtleboxes.py`
----------------------

Write a program to draw 100 rectangles of a random length and width, and a random color and at random positions in the turtle window.

.. hint:: You will need to use the ``turtle`` module, and functions from the turtle module such as ``goto``, ``up``, ``down``, ``forward``, ``right`` (or ``left``), ``begin_fill``, ``end_fill`` and ``fillcolor``.  Use the help system to find out how to call these functions.

For example:

.. image:: /images/extraex/image04.png
    :width: 200pt
    :align: center


:file:`longest.py`
------------------

Write a program to input a sentence and then print out which word is the longest.

For example:

.. code-block:: none
    :pythontest: off

    Please input your sentence: The quick fox jumped over the lazy dog
    The longest word in that sentence is: jumped


:file:`reverse.py`
------------------

Write a program to input a sentence and then print it out in reverse.

For example:

.. code-block:: none
    :pythontest: off

    Please input your sentence: mary had a little lamb
    The reverse of your sentence is: bmal elttil a dah yram


:file:`twist.py`
----------------

Write a program that draws a number of squares, using the ``turtle`` module, each one larger than the last and with the drawing turtle turning after each square.  Each square should also be a different color - use the ``random.choice`` function to select from a variety of colors.

The first square should have sides of 25 pixels in length, with each succeeding square being 10 pixels longer on each side.  The turtle should turn 10 degrees to the right after every square.

For example:


.. image:: /images/extraex/image05.png
    :width: 200pt
    :align: center


:file:`factorial.py`
--------------------

Write a program to input a number, and then print out the factorial of that number.  The factorial is all the numbers up to and including the actual number multiplied together.

For example:

.. code-block:: none
    :pythontest: off

    Please input your number: 6
    The factorial of 6 is 720

    Please input your number: 10
    The factorial of 10 is 3628800


:file:`quiz.py`
---------------

Write a program to ask the user a number of questions, with multiple choice answers, and then print out their score at the end.  You should ask 5 questions in total.  You are free to make up your own questions.

For example:

.. code-block:: none
    :pythontest: off

    Welcome to the QUIZ program!

    Question 1: Who won the football world cup in 1970?
    a) England b) Brazil c) West Germany d) Italy
    Your answer: b
    Correct!

    Question 2: Who won the Formula 1 world championship in 2008?
    a) Michael Schumacher b) Fernando Alonso c) Lewis Hamilton d) Niki Lauda
    Your answer: c
    Correct!

    Question 3: Who has won the most Wimbledon tennis titles?
    a) Roger Federer b) Boris Becker c) Andre Agassi d) Pete Sampras
    Your answer: d
    Incorrect, it is a!

    Question 4: Who has won the most Rugby World Cups?
    a) South Africa b) Australia c) New Zealand d) all three
    Your answer: b
    Incorrect, it is d!

    Question 5: Who has won the most Olympic medals?
    a) Michael Phelps b) Carl Lewis c) Usain Bolt d) Steve Redgrave
    Your answer: a
    Correct!

    Well done - you got 3 out of 5!


:file:`hangman.py`
------------------

Write a program to implement a simple hangman game.  Give the user 11 tries, and you can draw the hangman as you go along as follows (piece by piece):

.. code-block:: none
    :pythontest: off

     _______
     |/    |
     |     O   
     |    /|\
     |    / \
    ---

However, this part of drawing the hangman is optional as it makes the program more complicated.

.. hint:: You will need three strings, one for the word to guess (which selects one from the word list below randomly using the ``random.choice`` function), one containing the letters guessed so far, and one for the letters not in the word being guesses.  You can add onto a string by doing the following:

    .. code::
        :pythontest: norun

        string_name = string_name + character_entered

You may use the following as your word list, or create your own::

    WORD_LIST = ['adult', 'aeroplane', 'air', 'aircraft', 'airforce',
                 'airport', 'album', 'alphabet', 'apple', 'arm', 'army',
                 'baby', 'backpack', 'balloon', 'banana', 'bank',
                 'barbecue', 'bathroom', 'bathtub', 'bed', 'bed', 'bee',
                 'bible', 'bible', 'bird', 'bomb', 'book', 'boss', 'bottle',
                 'bowl', 'box', 'boy', 'brain', 'bridge', 'butterfly',
                 'button', 'cappuccino', 'car', 'carpet', 'carrot', 'cave',
                 'chair', 'chess', 'chief', 'child', 'chisel', 'chocolates',
                 'church', 'church', 'circle', 'circus', 'circus', 'clock',
                 'clown', 'coffee', 'comet', 'compass', 'computer',
                 'crystal', 'cup', 'cycle', 'database', 'desk', 'diamond',
                 'dress', 'drill', 'drink', 'drum', 'dung', 'ears', 'earth',
                 'egg', 'electricity', 'elephant', 'eraser', 'explosive',
                 'eyes', 'family', 'fan', 'feather', 'festival', 'film',
                 'finger', 'fire', 'floodlight', 'flower', 'foot', 'fork',
                 'freeway', 'fruit', 'fungus', 'game', 'garden', 'gas',
                 'gate', 'gemstone', 'girl', 'gloves', 'god', 'grapes',
                 'guitar', 'hammer', 'hat', 'hieroglyph', 'highway',
                 'horoscope', 'horse', 'hose', 'ice', 'insect', 'jet',
                 'junk', 'kaleidoscope', 'kitchen', 'knife', 'leather',
                 'leg', 'library', 'liquid', 'magnet', 'man', 'map', 'maze',
                 'meat', 'meteor', 'microscope', 'milk', 'milkshake',
                 'mist', 'money', 'monster', 'mosquito', 'mouth', 'nail',
                 'navy', 'necklace', 'needle', 'onion', 'paintbrush',
                 'parts', 'parachute', 'passport', 'pebble', 'pendulum',
                 'pepper', 'perfume', 'pillow', 'plane', 'planet', 'pocket',
                 'potato', 'printer', 'prison', 'pyramid', 'radar',
                 'rainbow', 'record', 'restaurant', 'rifle', 'ring',
                 'robot', 'rock', 'rocket', 'roof', 'room', 'rope',
                 'saddle', 'salt', 'sandpaper', 'sandwich', 'satellite',
                 'school', 'ship', 'shoes', 'shop', 'shower', 'signature',
                 'skeleton', 'slave', 'snail', 'software', 'solid', 'space',
                 'spectrum', 'sphere', 'spice', 'spiral', 'spoon', 'sport',
                 'square', 'staircase', 'star', 'stomach', 'sun',
                 'sunglasses', 'surveyor', 'swimming', 'sword', 'table',
                 'tapestry', 'teeth', 'telescope', 'television', 'tennis',
                 'thermometer', 'tiger', 'toilet', 'tongue', 'torch',
                 'torpedo', 'train', 'treadmill', 'triangle', 'tunnel',
                 'typewriter', 'umbrella', 'vacuum', 'vampire', 'videotape',
                 'vulture', 'water', 'weapon', 'web', 'wheelchair',
                 'window', 'woman', 'worm']


:file:`checkerboard.py`
-----------------------

Write a program to input a number, and then draw - using the ``turtle`` module - a checkerboard with that number of squares across.

.. hint:: Use the ``turtle`` module, and to see what turtle offers you, type ``dir(turtle)`` in the interactive shell to see the available functions.  You can use the ``turtle.setup`` function set arrange a square window for drawing.

For example:

.. code-block:: none
    :pythontest: off

    Please input the number of squares across: 4


.. image:: /images/extraex/image08.png
    :width: 200pt
    :align: center

.. code-block:: none
    :pythontest: off

    Please input the number of squares across: 20


.. image:: /images/extraex/image03.png
    :width: 200pt
    :align: center


:file:`prime.py`
----------------

Write a program to input a number, and then tell the user whether the number is prime or not.

.. note:: A prime number is a number only divisible by 1 and itself - assume 1 is not prime, and 2 is prime.

For example:

.. code-block:: none
    :pythontest: off

    Please input your number: 50
    The number 50 is not prime.

    Please input your number: 29
    The number 29 is prime.


:file:`factors.py`
------------------

Write a program to input a number, and then print outs the factors of that number.

For example:

.. code-block:: none
    :pythontest: off

    Please input your number: 20
    The factors of 20 are: 1, 2, 4, 5, 10, 20


:file:`turtlehistogram.py`
--------------------------

Write a program to allow the user to input a list of numbers, separated by spaces. Then, using turtle, draw a vertical histogram, with alternating colors, representing those numbers.

For example:

.. code-block:: none
    :pythontest: off

    Enter the numbers for the histogram: 1 1 2 5 10 20 35 25 12 4 2 1 1

.. image:: /images/extraex/image09.png
    :width: 200pt
    :align: center


:file:`kiosk.py`
----------------

Write a program that lists a set of products and their prices and allows the user to pick a number.  The program should then print out the price of the item chosen.

For example:

.. code-block:: none
    :pythontest: off

    1 Coke        50p
    2 Fanta       45p
    3 Pepsi       55p
    4 Sprite      40p
    5 Dr Pepper   60p
    Your choice: 3
    That's 55 pence please!

.. hint:: You can store your items in a list of items, with the name in the first field and the price in the second field of each item:

    .. code::

        [["1 Coke", 50], ["2 Fanta", 40], ["3 Pepsi", 55],
         ["4 Sprite", 40], ["Dr Pepper", 60]]


:file:`order.py`
----------------

Expand on the previous program to allow the user to enter a number of choices, the money they are entering, and finally the change they should get.

For example:

.. code-block:: none
    :pythontest: off

    1 Coke        50p
    2 Fanta       45p
    3 Pepsi       55p
    4 Sprite      40p
    5 Dr Pepper   60p
    Your choice: 2 3
    Your total is 100 pence
    Please enter your money: 500
    Your change is 400 pence

Again, use the ``numbers.split`` command to split the original string input into a list of entries.  The list you used in the previous practice can be used again for this program.


:file:`brackets.py`
-------------------

Write a program that reads in a sentence, and prints out whether the number of brackets match or not.  You will need to account for brackets out of order as well, for example ``")("``, instead of ``"()"``.

For example:

.. code-block:: none
    :pythontest: off

    Please input your sentence to perform a bracket match: (5 + 10) / (8 / 2
    That sentence does not have matching brackets!

    Please input your sentence: 5 + 2) / (5
    That sentence does not have matching brackets!

    Please input your sentence: (1 + 2) * (3 + 4)
    That sentence does have matching brackets!

    Please input your sentence: ((10 * 2) + ((8 / 4) - 1))
    That sentence does have matching brackets!


:file:`calc.py`
---------------

Write a program to give the user sums to perform until he types the word "quit".  Randomly chose two numbers between 1 and 10, and one operator of either addition, subtraction, division or multiplication.  Use ``random.randrange`` function to choose the number, and also to select between your operator (1 for addition, 2 for subtraction, and so on).

For example:

.. code-block:: none
    :pythontest: off

    What is 10 + 5? 15
    Correct, it is 15!

    What is 8 * 2? 15
    Wrong, it is 16!

    What is 8 - 4? 4
    Correct, it is 4!

    What is 10 / 2? quit
    Goodbye!


:file:`compound.py`
-------------------

Write a program to ask the user the amount of money to invest, the interest rate per year and the number of years, and then print out total per year and the total interest earned over the investment period.

For example:

.. code-block:: none
    :pythontest: off

    Please input the amount: 1000
    And what is the loan period in years: 10
    And finally, what is the interest rate per year in percent: 5

    Total now: £1050.00 after 1 years
    Total now: £1102.50 after 2 years
    Total now: £1157.62 after 3 years
    Total now: £1215.51 after 4 years
    Total now: £1276.28 after 5 years
    Total now: £1340.10 after 6 years
    Total now: £1407.10 after 7 years
    Total now: £1477.46 after 8 years
    Total now: £1551.33 after 9 years
    Total now: £1628.89 after 10 years
    Interest earned: £628.89 over 10 years


:file:`temprange.py`
--------------------

Write a program to ask for the start temperature, the end temperature, the type (whether Celsius or Fahrenheit), and then print out the conversion from one to the other at every degree from the start to the end.

.. pythontest:: off

Remember to convert from Celsius to Fahrenheit, you need to use this formula::

    fahrenheit = (9 / 5.0) * celsius + 32

and to go from Fahrenheit to Celsius you use this formula::

    celsius = (5.0 / 9) * (fahrenheit - 32)

.. pythontest:: on

For example:

.. code-block:: none
    :pythontest: off

    What is the start temperature: 20
    And what is the end temperature: 50
    and finally, what is your reading in, celsius or fahrenheit? celsius

    Celsius 20 in Fahrenheit is 68
    Celsius 21 in Fahrenheit is 69
    Celsius 22 in Fahrenheit is 71
    Celsius 23 in Fahrenheit is 73
    Celsius 24 in Fahrenheit is 75
    Celsius 25 in Fahrenheit is 77
    Celsius 26 in Fahrenheit is 78
    Celsius 27 in Fahrenheit is 80
    Celsius 28 in Fahrenheit is 82
    Celsius 29 in Fahrenheit is 84
    Celsius 30 in Fahrenheit is 86
    Celsius 31 in Fahrenheit is 87
    Celsius 32 in Fahrenheit is 89
    Celsius 33 in Fahrenheit is 91
    Celsius 34 in Fahrenheit is 93
    Celsius 35 in Fahrenheit is 95
    Celsius 36 in Fahrenheit is 96
    Celsius 37 in Fahrenheit is 98
    Celsius 38 in Fahrenheit is 100
    Celsius 39 in Fahrenheit is 102
    Celsius 40 in Fahrenheit is 104
    Celsius 41 in Fahrenheit is 105
    Celsius 42 in Fahrenheit is 107
    Celsius 43 in Fahrenheit is 109
    Celsius 44 in Fahrenheit is 111
    Celsius 45 in Fahrenheit is 113
    Celsius 46 in Fahrenheit is 114
    Celsius 47 in Fahrenheit is 116
    Celsius 48 in Fahrenheit is 118
    Celsius 49 in Fahrenheit is 120
    Celsius 50 in Fahrenheit is 122


:file:`cipher.py`
-----------------

Write a program to read in a sentence, and then print it out with each letter shifted back by three (a Caesar cipher).  So, "a" will become "x", "b" will become "y", "c" will become "z", "d" becomes "a", and so on until "z" becomes "w".  You can ignore all letters apart from lowercase ones ("a" to "z") and print them out unchanged (e.g. spaces).

Having printed out the encoded message, the program should then decode it so that each letter is shifted forwards by three, and then print out the result.  Obviously, the decoded message should be the same as the one originally input by the user in the first place.

.. hint:: Use the ``ord`` function to get the numerical representation of a letter, and ``chr`` to convert them back to their character representation.  Use ``string.ascii_lowercase`` as a shortcut for the lowercase alphabet, although you will have to import the ``string`` module first.

For example:

.. code-block:: none
    :pythontest: off

    Please input your sentence to encode: mary had a little lamb
    The encoded sentence is: jxov exa x ifqqib ixjy
    The decoded sentence is: mary had a little lamb


:file:`turtlebattleship.py`
---------------------------

Write a program that, until the user hits the ship, does:

Draws a checkerboard board using turtle. The unbombarded squares should be left white, misses colored blue (or some other symbol) and hit squares colored red (or some other symbol).
The user should then be asked for an x, y coordinate for his shot.

At the end, the board should be drawn one last time, then the program should wait for the user to quit.

For example:

.. image:: /images/extraex/image10.png
    :width: 200pt
    :align: center

.. code-block:: none
    :pythontest: off

    What is your move in the form 'x y'? 3 4

.. image:: /images/extraex/image01.png
    :width: 200pt
    :align: center

.. code-block:: none
    :pythontest: off

    What is your move in the form 'x y'? 1 1

.. image:: /images/extraex/image06.png
    :width: 200pt
    :align: center

.. code-block:: none
    :pythontest: off

    You sunk me, press enter to quit...
