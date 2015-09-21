Operators
=========

The most commonly used operators in Python.

Arithmetic operators
--------------------

========  ======================================
Operator    Name                                  
========  ======================================
``+``       Addition                              
``-``       Subtraction                           
``/``       Division                              
``*``       Multiplication                        
``**``      Power                                 
``//``      Floor division (Whole number division)
``%``       Modulus (remainder)                   
 ==============================================

Examples::

    >>> 10 + 20 * 2
    50
    >>> a = 9
    >>> a % 4
    1
    >>> 2 ** 8 + 1
    257

Comparison operators
--------------------

========  ======================================
Operator    Name                                  
========  ======================================
``==``      Equal to                              
``!=``      Not equal to                          
``<``       Less than                             
``>``       Greater than                          
``<=``      Less than or equal to                 
``>=``      Greater than or equal to              
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
Operator    Name                                  
========  ======================================
``<<``      Shift bits to the left
``>>``      Shift bits to the right
``&``       Bitwise and (set to 1 when both are 1) the bits together
``|``       Bitwise or (set to 1 when either are 1) the bits together
``~``       Return compliment - all the 1's and 0's are flipped
``^``       Bitwise exclusive or the bits together, unless both are 1 when the result is 0
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
Operator    Name                                                         
========  =============================================================
``and``     If both operands are true, then condition is true            
``or``      If either of the operands is true, then the condition is true
``not``     Reverses the condition                                       
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
Operator    Name                                                                   
========  =======================================================================
``in``      Condition is true if the value or variable is contained in a sequence  
========  =======================================================================

Examples::

    >>> a = 10
    >>> a in [5, 10, 15, 20]
    True
    >>> a in [0, 20, 40, 60]
    False
