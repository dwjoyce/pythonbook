:orphan:

Operators
=========

.. quote::
    :author: J.R.R. Tolkien
    :source: The Hobbit

    Do you wish me a good morning, or mean that it is a good morning whether I want it or not; or that you feel good this morning; or that it is a morning to be good on?

The most commonly used operators in Python.

Arithmetic operators
--------------------

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
--------------------

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
--------------------

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
-----------------

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
-----------------

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
--------------------

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
-------------------

The following table summarizes the operator precedences in Python, from lowest precedence (least binding) to highest precedence (most binding). Operators in the same box have the same precedence.

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
