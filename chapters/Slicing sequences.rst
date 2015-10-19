Slicing sequences
=================

.. quote:: Bill Bryson

    A computer is a stupid machine with the ability to do incredibly smart things, while computer programmers are smart people with the ability to do incredibly stupid things. They are, in short, a perfect match.

Dipping in
----------

In the previous chapter we learnt how to group a sequence of items together under a single name.  These are all sequences in Python::

    >>> names = ['tom', 'dick', 'harry']
    >>> numbers = [0, 1, 2, 3, 4, 5]
    >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> jumble = [10, 'fred', 17.25, True, ['username', 123456789]]
    
However, there is another type of sequence that we are already familiar with - strings.  As we know, strings are sequences of characters, whether letters, digits or symbols, and can be treated as sequences in terms of slicing as we shall see in this chapter.  The main difference is that you cannot modify the contents of a string, but you can form new strings from old ones.

We have been able to refer to the group as a whole, but what if we need to select individual items out of the group - how do we dip into the sequence and reference a single item?  Firstly, type this in so we start off with a simple string as our sequence to use::

.. pythontest:: nooutput

    >>> letters = 'abcdef'
    
We can refer to the whole sequence of letters, such as ``print(letters)``, and even randomly select an item as we did the previous chapter.  But how would we get at just one of those letters?  Firstly, think of this string as a sequence of boxes, each of which contains a single letter:

.. image:: /images/alien_pizza/indexing-middle.pdf
    :width: 200 pt
    :align: center

To "dip in" and fetch a single letter, we need to index the item as an offset from the start of the sequence.  To picture this, think of a hotel, like so:

.. image:: /images/alien_pizza/hotel.pdf
    :height: 170 pt
    :align: center

In the UK at least, we do not number the floors from the 1st floor and count up - the floors are numbered as how far up they are.  Effectively, the floor number is an *offset* from the ground, i.e. 1st floor up, 2nd floor up, etc.

In Python, sequences are very similar - the number of each item is how far from the beginning it is - the offset from the first item:

.. image:: /images/alien_pizza/indexing-top.pdf
    :width: 200 pt
    :align: center

To use the offset of a particular item inside a sequence, you need to use square brackets in the form ``[offset]``, just like how have leant how to box up a list of items.  This is placed directly after the name of the sequence itself.  We can now practice this in the interactive shell::

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

Practice again in the interactive shell::

    >>> print(letters[-1])
    >>> print(letters[-2])
    >>> print(letters[-3])
    >>> print(letters[-4])
    >>> print(letters[-5])
    >>> print(letters[-6])
    
This should print off each letter in turn, this time from the end or the right of the sequence.  Notice when we used positive numbers, we start from 0 and ended up at an item offset by 5 (one less than the length of the sequence itself).  When we use negative numbers, we start from -1 (as 0 is the the beginning), and end up at -6.

All of this is relevant for any type of list, whether they contain characters, strings, numbers, sub-lists or anything else.  Let us use one from the previous chapter::

    >>> names = ['fred', 'bob', 'harry', 'tom']
    >>> print(names[0])
    >>> print(names[3])
    >>> print(names[-1])
    >>> print(names[-4])

Be careful that you open and close the brackets correctly, if you are having problems!  Moreover, if you use an offset that is off the end (or the past the beginning) of the sequence, Python will complain.

.. pythontest:: all

Unidentified Food Object
------------------------

The aliens have landed on Earth, and they have brought pizza! However, for us humans to join in and eat pizza, we have to learn their language. Here is an alien pizza:

.. image:: /images/alien_pizza/unnumbered.pdf
    :height: 100 pt
    :align: center

The aliens like to be efficient when telling other aliens. They number each cut, starting from 0. The pizza slice's number is the number directly to its left:

.. image:: /images/alien_pizza/numbered.pdf
    :height: 100 pt
    :align: center

So, if an alien wants the red pizza slice, he says 0, and if he wants the blue slice, he says 4. However, the aliens have giant pizzas, and asking for the slice before 0 on a 100 slice pizza means saying a very large number (99). So the aliens also number their pizzas using negative numbers:

.. image:: /images/alien_pizza/negnumbered.pdf
    :height: 100 pt
    :align: center

Instead of saying 99, he can say -1.

An alien army marches on its stomach
------------------------------------

Some aliens are greedy, and want more than one slice, but they are also lazy, and cannot be bothered to say every single number. So they say a range. For example, if an alien wants the red and yellow slice, he can say he wants all the slices between cuts 0 and 2. The serving alien takes piece 0, and adds one, taking piece 1. If he adds 1 again, he gets 2, so he has got all the pieces, and gives pieces 0 and 1 to the alien:

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

OK, now we know how to ask aliens for pizza, but what about if python has our pizza? Lets represent the pizza as a list of the slice colors::

    >>> pizza = ["red", "yellow", "green", "cyan", "blue", "magenta"]

Our ``pizza`` has all the colors of the alien pizza, in clockwise direction. How do we ask for a slice of pizza? We type ``pizza``, followed by an opening square bracket, ``[``, followed by our slice number, lets say ``1``, followed by a closing square bracket, ``]``::

    >>> pizza[1]
    'yellow'
    >>> pizza[4]
    'blue'

Python must have met the aliens too. What about negative indexes? Python learnt well::

    >>> pizza[-1]
    'magenta'
    >>> pizza[-3]
    'cyan'

That's great, but I'm hungry. I want all the slices from 0 to 2. How do I do that? First we type the first index, the start, like before: ``pizza[0``. Then we type a colon, ``:``, followed by our second index, ``2`` which is the stop, followed by the closing bracket, ``]``::

    >>> pizza[0:2]
    ['red', 'yellow']

See?, Python has given us a list of our slices! The other aliens would be happy::

    >>> pizza[-4:-1]
    ['green', 'cyan', 'blue']
    >>> pizza[1:-1]
    ['yellow', 'green', 'cyan', 'blue']

But what if our reg-green-blue loving alien turned up? We first type the start and stop index: ``pizza[0:5``. Then we type another colon, ``:``, then the number we add, or step. For every second slice, its ``2``, followed by the closing bracket, ``]``::

    >>> pizza[0:5:2]
    ['red', 'green', 'blue']

What about every third slice from 1 to -1? Easy::

    >>> pizza[1:-1:3]
    ['yellow', 'blue']

Slicing and dicing
------------------

OK, we have had enough pizza to satisfy us for a lifetime. But what we have just done is useful. It is called indexing when we use only one number, and slicing when we use more than one number. The general form is ``list_or_string[start:stop:step]``. Say we have all the numbers from 0 to 20::

    >>> nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

We can grab the first number::

    >>> nums[0]
    0

And the last number::

    >>> nums[-1]
    19

We can grab the first 4 numbers::

    >>> nums[0:3]
    [0, 1, 2]

If we want to slice from the start you can miss the zero out::

    >>> nums[:3]
    [0, 1, 2]

similarly we can miss off the stop index if we want to slice to the end. To get the last 5 numbers::

    >>> nums[-5:]
    [15, 16, 17, 18, 19]

To get all the even numbers, we can use the step::

    >>> nums[::2]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

All the multiples of 3::

    >>> nums[::3]
    [0, 3, 6, 9, 12, 15, 18]

All the multiples of 3 plus 1::

    >>> nums[1::3]
    [1, 4, 7, 10, 13, 16, 19]

Cut the string
--------------

Before I said ``list_or_string``. That means string work too! If we want the first letter of someone's name, use indexing::

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
        
    This will work regardless of the length of the first and surname.

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

1. Write a program called daysofweek.py which defines a list containing the days of the week (assume that Sunday is the first day).  Ask the user for a number between 1 and 7, and print out the appropriate day of the week.  For example, if the user types in ``1``, then print out ``Sunday``.  If the user types in ``7``, then print out ``Saturday``.  Note, you will have to take 1 off what the user has typed in, before you use it as an index into your days of the week list.

2. Write a program called planets.py which defines a list with the 8 major planets of our solar system: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune (each one will be a string).  Your program should print out the rocky planets (the first four), followed by the four gaseous planets - use slicing to do this.

3. Write a program called colours which defines the colors of the rainbow as red, orange, yellow, green, blue, indigo and violet.  Your program should print our the primary colours of red, green and blue as a slice of your color list.

Things to remember
------------------

1. Lists and strings are sequences, and so can be indexed and sliced.

2. The first item in a sequence has the index ``0``, the second ``1``, the third ``2``, and so on.

3. Negative indexes can be used, counting from the end of the sequence. The last item is ``-1``.

4. Slicing is done by ``sequence[start:stop:step]``.
