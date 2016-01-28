Slicing sequences
=================

.. quote::
    :author: Many people

    A programmer is a device for turning caffeine into code.

Dipping in
----------

In the previous chapter we learnt how to group a sequence of items together under a single name.  These are all sequences in Python::

    >>> escape_tunnels = ['tom', 'dick', 'harry']
    >>> numbers = [0, 1, 2, 3, 4, 5]
    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> jumble = [10, 'fred', 17.25, True, ['username', 123456789]]
    
However, there is another type of sequence that we are already familiar with - strings.  As we know from :ref:`chapter 7` on printing, strings are sequences of characters, whether letters, digits or symbols, and can be treated as sequences in terms of slicing as we shall see later in this chapter.  The main difference is that you cannot modify the contents of a string, but you can form new strings from old ones.

.. pythontest:: nooutput

We have been able to refer to the group as a whole, but what if we need to select individual items out of the group - how do we dip into the sequence and reference a single item?  Firstly, type this in so we start off with a simple string as our sequence to use::

    >>> letters = 'abcdef'
    
We can refer to the whole sequence of letters, such as ``print(letters)``, and even randomly select an item as we did the previous chapter.  But how would we get at just one of those letters?  Firstly, just like we illustrated in :ref:`chapter 7` on printing, think of this string as a sequence of boxes, each of which contains a single letter:

.. image:: /images/alien_pizza/indexing-middle.pdf
    :width: 200 pt
    :align: center

To "dip in" and fetch a single letter, we need to :term:`index` the item as an offset from the start of the sequence.  To picture this, think of a hotel, like so:

.. image:: /images/alien_pizza/hotel.pdf
    :height: 170 pt
    :align: center

In the UK at least, we do not number the floors from the 1st floor and count up - the floors are numbered as how far up they are.  Effectively, the floor number is an *offset* from the ground, i.e. 1st floor up, 2nd floor up, etc.  The ground floor is really floor 0.

In Python, sequences are very similar - the number of each item is how far from the beginning it is - the offset from the first item:

.. image:: /images/alien_pizza/indexing-top.pdf
    :width: 200 pt
    :align: center

To use the offset of a particular item inside a sequence, you need to use square brackets in the form ``[index]`` or ``[offset]``, just like how have leant how to box up a list of items.  This is placed directly after the name of the sequence itself.  We can now practice this in the interactive interpreter::

    >>> print(letters[0])
    >>> print(letters[1])
    >>> print(letters[2])
    >>> print(letters[3])
    >>> print(letters[4])
    >>> print(letters[5])
    
This should print off each letter in turn.  Remember, the offset refers to how many places from the beginning, or the left, the item is to be found.

If we want to refer to an item not from the beginning, but instead from the end, we simply use negative numbers:

.. image:: /images/alien_pizza/indexing-all.pdf
    :width: 200 pt
    :align: center

Practice again in the interactive interpreter::

    >>> print(letters[-1])
    >>> print(letters[-2])
    >>> print(letters[-3])
    >>> print(letters[-4])
    >>> print(letters[-5])
    >>> print(letters[-6])
    
This should print off each letter in turn, this time from the end or the right of the sequence.  Notice when we used positive numbers, we start from 0 and ended up at an item offset by 5 (one less than the length of the sequence itself).  When we use negative numbers, we start from -1 (as 0 is the beginning), and end up at -6.  This may not sound like a big improvement, but when your sequence is very long it is useful to state the offset from the right rather than from the left.

All of this is relevant for any type of list, whether they contain characters, strings, numbers, sub-lists or anything else.  Let us use one from the previous chapter::

    >>> names = ['fred', 'bob', 'harry', 'tom']
    >>> print(names[0])
    >>> print(names[3])
    >>> print(names[-1])
    >>> print(names[-4])

Be careful that you open and close the brackets correctly, if you are having problems!  Moreover, if you use an offset that is past the end of the sequence, Python will complain - ``print(names[4])`` in this example.

Outside In
----------

What if the sequence contains more than one level, like a matrix we mentioned in the previous chapter?  For example, type the following to define a matrix of numbers::

    >>> matrix = [[0,1,2], [3,4,5], [6,7,8]]

How do we get at the individual items inside on of the inner lists, such as the number 3?  We use the same notation, and go from the outside sequence inwards.  In this example, to get at the number 3, we first index the second item of the overall sequence, which gives us ``[3,4,5]``.  With this item, we can then index the actual number we wish, which being the first item has an index of 0.  Although it is conceptually two steps, we can do it in one line by first indexing the correct item in the overall list, and then indexing the individual item in this inner list::

    >>> matrix[1][0]
    3
    
So the indexing goes from outside in, left to right, with the name of the overall sequence (or matrix) on the left-hand side.

The same occurs if the list is even deeper, such as a list of lists, each containing a string::

    >>> names = [['tom', 'jones'], ['john', 'smith'], ['zippy', 'james']]

If we wish to pull out the ``'y'`` in ``'zippy'`` then - from the outside in - we index ``2`` to get at ``['zippy', 'james']`` then index ``0`` to get at ``'zippy'`` and finally ``4`` to index the ``'y'``::
                  
    >>> names[2][0][4]
    >>> 'y'

.. pythontest:: all

Unidentified Food Object
------------------------

The aliens have landed on Earth, and they have brought pizza!  Thankfully, their numbering system is the same as Python's, so here is a summary of how they refer to each slice:

.. image:: /images/alien_pizza/pizza-intro.pdf
    :height: 100 pt
    :align: center

However, aliens are not satisfied with one slice, they are greedy.  They are also lazy, and cannot be bothered to say every single number. So they say a range. For example, if an alien wants the red and yellow slice, he can say he wants all the slices between cuts 0 and 2. The serving alien takes piece 0, and adds one, taking piece 1. If he adds 1 again, he gets 2, so he has got all the pieces, and gives pieces 0 and 1 to the alien:

.. image:: /images/alien_pizza/slice02.pdf
    :height: 100 pt
    :align: center

Aliens also do negative slices. An alien wants -4 to -1, which is the same as 2 to 5 so adding 1 gives the slices 2, 3 and 4.:

.. image:: /images/alien_pizza/slice-4-1.pdf
    :height: 100 pt
    :align: center

The opposite does not work, as you cannot add ones to 5 to get 2. 1 to -1 is the same as 1 to 5, so the slices are 1, 2, 3, and 4:

.. image:: /images/alien_pizza/slice1-1.pdf
    :height: 100 pt
    :align: center

I'll pass
---------

What if an alien only likes red, green and blue? Well, he can ask for every second piece from 0 to 5. The serving alien takes 0, adds two, so takes 2, and adds 2 again and takes 4. Adding two again will mean that he takes slice 6, but 6 is greater than 5, so he stops:

.. image:: /images/alien_pizza/slice052.pdf
    :height: 100 pt
    :align: center

Every third slice from 1 to -1? That's the same as every third slice from 1 to 5, which is 1 and 4:

.. image:: /images/alien_pizza/slice1-13.pdf
    :height: 100 pt
    :align: center

Python likes pizza
------------------

OK, now we know how to ask aliens for pizza, but what about if a python stole our pizza? Let us represent the pizza as a list of the colors, one for each slice::

    >>> pizza = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

Our ``pizza`` has all the colors of the alien pizza, in clockwise direction.  As with indexing our letters string at the beginning of the chapter, we can pull out whole words from the list in a similar way (remember, each item is a word, not an individual letter):

    >>> pizza[1]
    'yellow'
    >>> pizza[4]
    'blue'
    >>> pizza[-1]
    'magenta'
    >>> pizza[-3]
    'cyan'

Now we can accommodate our hungry aliens.  If we want all the slices from 0 to 2 we first we type the first index, the start, like before: ``pizza[0``. Then we type a colon, ``:``, followed by our second index, ``2`` which is the stop, followed by the closing bracket, ``]``::

    >>> pizza[0:2]
    ['red', 'yellow']

See how Python has given us a list of our slices! The other aliens would be happy::

    >>> pizza[-4:-1]
    ['green', 'cyan', 'blue']
    >>> pizza[1:-1]
    ['yellow', 'green', 'cyan', 'blue']

But what if our red-green-blue loving alien turned up?  We first type the start and stop index: ``pizza[0:5``. Then we type another colon, ``:``, followed by the step we wish to take each time. To ask for every second slice, the step will be ``2``, followed by the closing bracket, ``]``::

    >>> pizza[0:5:2]
    ['red', 'green', 'blue']

To obtain a list from the color sequence with every third slice, use a step of 3 (this time starting from index 1, all the way to the end indicated by a stop value of -1)::

    >>> pizza[1:-1:3]
    ['yellow', 'blue']

Slicing and dicing
------------------

When we use a single number to reference a single item it is called :term:`indexing`; when we use more than one number to reference a range of items it is called :term:`slicing`. The general form for slicing is ``sequence[start:stop:step]``.

Indexing and slicing can happen on sequences containing data of any type.  Define this list of the numbers from 0 to 20::

    >>> nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

As before, we use an index of 0 to grab the first number in the list::

    >>> nums[0]
    0

And an index of -1 to obtain the last number::

    >>> nums[-1]
    19

We can grab the first 3 numbers by using a stop value in addition to the start::

    >>> nums[0:3]
    [0, 1, 2]

If we want to slice from the start you can miss the zero out::

    >>> nums[:3]
    [0, 1, 2]

Similarly, we can miss off the stop index if we want to slice to the end.  For example, to get the last 5 numbers type the following::

    >>> nums[-5:]
    [15, 16, 17, 18, 19]

To get all the even numbers, we can use the step value all by itself::

    >>> nums[::2]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

All the multiples of 3::

    >>> nums[::3]
    [0, 3, 6, 9, 12, 15, 18]

All the multiples of 3, offset by 1::

    >>> nums[1::3]
    [1, 4, 7, 10, 13, 16, 19]

Reverse gear
------------

If you wish to slice a sequence in reverse (backwards), then you simply need to use a negative step.  However, in this case, you must ensure the end index lower than the start index, otherwise it will return an empty sequence.  Type in these examples:

    >>> letters = 'abcde'
    >>> letters[4:0:-1]
    'edcb'
    >>> letters[4::-1]
    'edcba'
    >>> letters[::-1]
    'edcba'
    
The first slice goes from the 4th element (the letter 'e') to the beginning (up to, but not including, the letter 'a'), with a step of -1 every time.

If we wish to include the beginning as well, we can miss out the number for the end position - it will then stop when the sequence stops.  This is the approach we take with the second example.  Since we wish to go from the end all the way back to the beginning, we don't really need the start position either - let Python fill in those numbers for us.  To copy the whole sequence, you would simply type ``letters[:]`` as it encompasses both the beginning and the end, inclusive, so adding a step of ``-1`` will slice from the end all the way back to the beginning, including both ends as it does so.

.. tip:: If you simply want to reverse a sequence of items, then use the built-in function ``reversed``.  For example, ``''.join(reversed('abcde'))``, will print out ``edcba`` - the call to the ``join`` function is to join the list back together again, each separated by an empty string!

Cut the string
--------------

As strings are sequences as well as lists, this means we can slice them too.  As before, if we want the first letter of someone's name, we can index it as follows::

    >>> name = "Isaac Newton"
    >>> name[0]
    'I'

First three letters::

    >>> name[:3]
    'Isa'

First name::

    >>> name[:5]
    'Isaac'
    >>> name[:-7]
    'Isaac'

Surname::

    >>> name[6:]
    'Newton'
    >>> name[-6:]
    'Newton'

Initials::

    >>> name[::6]
    'IN'

.. note::

    The above three examples are better done by::
        
        >>> name.split()
        ['Isaac', 'Newton']
        >>> name.split()[0]
        'Isaac'
        >>> name.split()[1]
        'Newton'
        >>> name.split()[0][0]
        'I'
        >>> name.split()[1][0]
        'N'
        >>> name.split()[0][0] + name.split()[1][0]
        'IN'
        
    This will work regardless of the length of the first name and surname.

Given the alphabet::

    >>> alphabet = "abcdefghijklmnopqrstuvwxyz"
    >>> len(alphabet)
    26

We can find various things::

    >>> alphabet[:3]
    'abc'
    >>> alphabet[::2]
    'acegikmoqsuwy'
    >>> alphabet[1::2]
    'bdfhjlnprtvxz'
    >>> alphabet[-3:]
    'xyz'
    >>> alphabet[5:8]
    'fgh'
    
Exercises
---------

#. Write a program called :file:`sentence.py` that inputs a sentence, and then prints out every other letter (i.e. prints even letters, but misses out odd ones) and also in reverse.  Use both a ``while`` loop and slicing to achieve this, so that each print occurs twice.

#. Write a program called :file:`daysofweek.py` which defines a list containing the days of the week (assume that Sunday is the first day).  Ask the user for a number between 1 and 7, and print out the appropriate day of the week.  For example, if the user types in ``1``, then print out ``Sunday``.  If the user types in ``7``, then print out ``Saturday``.  Note, you will have to take 1 off what the user has typed in before you use it as an index into your days of the week list.

#. Write a program called :file:`planets.py` which defines a list with the 8 major planets of our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune (each one will be a string).  Ask the user whether he wants either the rocky or gaseous planets.  For the former, print out the first four planets; for the later, print out the last four planets - use slicing to do this.

#. Write a program called :file:`colors.py` which defines the colors of the rainbow as red, orange, yellow, green, blue, indigo and violet.  Your program should print out the primary colors of red, green and blue as a slice of your color list.

#. Write a program called :file:`seasons.py`, which defines a list containing three sub-lists, for example:

   .. code::
    
       seasons = [['December', 'January', 'February'],
                  ['March', 'April', 'May'],
                  ['June', 'July', 'August'],
                  ['September', 'October', 'November']]
        
   Ask the user which season, for example, "winter", "spring", "summer" or "autumn".  If the user has entered "spring", then print out the first item in the seasons list, if "summer", then print out the second item, and so on.  Bonus: use ``', '.join(seasons[index])`` to print out the month names nicely, with a comma between each and missing out the brackets.

Things to remember
------------------

#. Lists and strings are :term:`sequences`, and so can be indexed and sliced.

#. The first item in a sequence has the :term:`index` ``0``, the second ``1``, the third ``2``, and so on.  Think of the index as the offset from the beginning.

#. Negative indices can be used, counting from the end of the sequence. The last item is ``-1``, the second from last -2, and so on.

#. If a sequence has more than one level (i.e. is multi-dimensional like a matrix), then you index from the outside in, with each index using the ``[]`` notation.

#. :term:`Slicing` is done by ``sequence[start:stop:step]``.
