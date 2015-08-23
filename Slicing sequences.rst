Slicing sequences
=================

Unidentified Food Object
------------------------

The aliens have landed on Earth, and they have brought pizza! However, for us humans to join in and eat pizza, we have to learn their language. Here is an alien pizza:

.. image:: alien_pizza/unnumbered.pdf
    :height: 100 pt
    :align: center

The aliens like to be efficient when telling other aliens. They number each cut, starting from 0. The pizza slice's number is the number directly to its left:

.. image:: alien_pizza/numbered.pdf
    :height: 100 pt
    :align: center

So, if an alien wants the red pizza slice, he says 0, and if he wants the blue slice, he says 4. However, the aliens have giant pizzas, and asking for the slice before 0 on a 100 slice pizza means saying a very large number (99). So the aliens also number their pizzas using negative numbers:

.. image:: alien_pizza/negnumbered.pdf
    :height: 100 pt
    :align: center

Instead of saying 99, he can say -1.

An alien army marches on its stomach
------------------------------------

Some aliens are greedy, and want more than one slice, but they are also lazy, and cannot be bothered to say every single number. So they say a range. For example, if an alien wants the red and yellow slice, he can say he wants all the slices between cuts 0 and 2. The serving alien takes piece 0, and adds one, taking piece 1. If he adds 1 again, he gets 2, so he has got all the pieces, and gives pieces 0 and 1 to the alien:

.. image:: alien_pizza/slice02.pdf
    :height: 100 pt
    :align: center

Aliens also do negative slices. An alien wants -4 to -1, which is the same as 2 to 5 so adding 1 gives the slices 2, 3 and 4.:

.. image:: alien_pizza/slice-4-1.pdf
    :height: 100 pt
    :align: center

The opposite does not work, as you cannot add ones to 5 to get 2. 1 to -1 is the same as 1 to 5, so the slices are 1, 2, 3, and 4:

.. image:: alien_pizza/slice1-1.pdf
    :height: 100 pt
    :align: center

I'll pass
---------

What if an alien only likes red, green and blue? Well, he can ask for every second piece from 0 to 5. The serving alien takes 0, adds two, so takes 2, and adds 2 again and takes 4. Adding two again will mean that he takes slice 6, but 6 is greater than 5, so he stops:

.. image:: alien_pizza/slice052.pdf
    :height: 100 pt
    :align: center

Every third slice from 1 to -1? That's the same as every third slice from 1 to 5, which is 1 and 4:

.. image:: alien_pizza/slice1-13.pdf
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

.. todo:: Exercises for Slicing sequences

Things to remember
------------------

1. Lists and strings are sequences, and so can be indexed and sliced.
2. The first item in a sequence has the index ``0``.
3. Negative indexes can be used, counting from the back of the sequence. The last item is ``-1``.
4. Slicing is done by ``sequence[start:stop:step]``.
5. Aliens love pizza.
