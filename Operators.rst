Operators
=========

Arithmetic operators
--------------------

======================================  ========
Name                                    Operator    
======================================  ========
Addition                                ``+``
Subtraction                             ``-``
Division                                ``/``
Multiplication                          ``*``
Power                                   ``**``
Floor division (Whole number division)  ``//``
Modulus (remainder)                     ``%``
======================================  ========

Examples::

    >>> 10 + 20 * 2
    50
    >>> a % 4
    2
    >>> 2 ** 8 + 1
    257

Comparison operators
--------------------

======================================  ========
Name                                    Operator    
======================================  ========
Equal to                                ``==``
Not equal to                            ``!=``
Less than                               ``<``
Greater than                            ``>``
Less than or equal to                   ``<=``
Greater than or equal to                ``>=``
======================================  ========

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

Logical operators
-----------------

=============================================================  ========
Name                                                           Operator    
=============================================================  ========
If both operands are true, then condition is true              ``and``
If either of the operands is true, then the condition is true  ``or``
Reverses the condition                                         ``not``
=============================================================  ========

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

=======================================================================  ========
Name                                                                     Operator    
=======================================================================  ========
Condition is true if the value or variable is contained in a sequence    ``in``
=======================================================================  ========

Examples::

    >>> a = 10
    >>> a in [5, 10, 15, 20]
    True
    >>> a in [0, 20, 40, 60]
    False

