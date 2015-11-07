:orphan:

Glossary
========

.. quote::
    :author: Sherlock Homes

    Elementary, my dear Watson

.. Please keep entries under the chapter they were first introduced. They will be alphabetically sorted on build.

.. glossary::
    :sorted:

    .. Starting with Python's IDLE

    pseudo-code
        A description of how your program works in simple English, without any unnecessary details of how it will be written.

    IDLE
        IDLE is the Python IDE.

    integrated development environment
        An integrated development environment (IDE) is a program that allows you to write, run and debug your code.  Some IDE programs provide extra tools to allow you to write the code faster such as code highlighting and automatic code completion.

    interactive shell
        A simple, interactive computer programming environment that takes user inputs (e.g. a single line of code or a loop), evaluates them, and returns the result to the user.

    run
    execute
        To perform the actions represented by the code.
        
    statement
        A line of code or a code block that performs an action.  A compound statement is a statement that performs a block of code selectively or iteratively (e.g. belonging to an ``if`` or ``while`` statement).


    .. Python as a Calculator

    expression
        A combination of actual values, variables, operators, calls to functions and even sub-expressions, to form a value that is computed or evaluated into its simplest form.  For example, the expression ``10 + 4 * 3 / 2`` is evaluated to form the value ``16.0``.

    operator
        A symbol that represents an action, such as addition, assignment or equality.

    integer
        A whole number such as ``18``. These numbers never have a fractional part.

    float
        A floating point number is a number that has a fractional part, such as ``1.78``, even if the fractional part is zero.

    integer division
    floor division
        An division where the result is rounded down to the nearest whole number.

    modulus
        The remainder when the first number is divided by the second.

    type
    class
        A set of values having the same behaviour (but typically differing in state), or a template defining such a set.  A type is a particular class of data, such as integers, lists or files.


    .. Naming your data
    
    assignment
        The process of defining a variable with a set value, e.g. ``my_name = 'Fred'``.

    variable
        A named memory location in which a program can store intermediate results and from which it can read and modify them.
        
    evaluation
        The process of computing a result.


    .. Functions and Maths

    call
        Execute or run a :term:`function` with the necessary :term:`arguments`.

    function
        A section of code given a name that implements a task and :term:`returns` a value, even if that value is empty.

    built-in function
        A function that comes with Python, so you do not need to implement it yourself, such as ``round``, ``print`` and ``input``.

    argument
        A value, or reference to a value, passed into a :term:`function`.

    return value
        The data passed back from a called :term:`function`.


    .. Drawing Turtles
    
    import
        Including or making available one module inside another module.


    .. Getting help

    module
        A module is a file containing Python definitions and statements, e.g. a program that can be used by others.

    dir
        A :term:`built-in function` that provides a directory listing of what is contained inside an object such as a module.


    .. First program

    .py
        The file extension that all python files should use.

    editor
        A program for creating and making changes to files, especially text files.
        
    comment
        A piece of text acting as annotation or a description of the code.  It is intended to be read by other people, and is ignored by Python from the ``#`` character to the end of the line.


    .. Print that out!
    
    string
        A sequence of characters such as letters, digits or symbols stored in encoded form.

    string concatenation
        The operation of joining multiple strings into one string.


    .. Asking questions



    .. Performing selection
    
    selection
        The process of executing one piece (block) of code over another selectively.

    code block
        A block is a piece of Python code that is executed as a unit.

    indentation
        Beginning a line with one or more spaces. Used to distinguish code blocks.


    .. Decisions, decisions

    boolean
        A data type that can only have the values ``True`` and ``False``.


    .. Combining decisions together

    boolean operator
    logical operator
        An operator, such as ``and`` that always results in a :term:`boolean` result, or boolean-convertible result.  For example, ``a == 10`` or ``a < 0 or a > 100``.


    .. Going loopy
    
    iteration
        The process where a set of instructions or data are repeated.
        
    keyword
        A word with a special meaning.  Python has many reserved keywords that it uses for its own purposes, such as ``if``, ``while``, ``for``, ``def``, etc., which you cannot use for any other purpose.  To see Python's full list of keywords, then import the ``keyword`` module and type ``keyword.kwlist`` in the interactive shell.

    increment
        Increase the value of a variable.  For example: ``num = num + 1``, or ``num += 1`` for short.
        
    .. Escaping the cycle

    infinite loop
        A loop which continues indefinitely.


    .. Going random

    random
        Unpredictable in value.


    .. Grouping data together

    list
        A sequence of items, boxed together using the ``[]`` notation.  The items can be of any type, such as integers, strings or even other lists.

    matrix
        A two-dimensional list or list of lists, such as::

            matrix = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]

        Elements can be accessed by :term:`indexing` twice::

            >>> matrix[2][2]
            9


    .. Slicing sequences

    slice
        A portion or section of a sequence.

    index
        Accessing a single item of a sequence, where ``0`` is the first item.


    .. Walking along data
    
    decrement
        Decrease the value of a variable.  For example: ``num = num - 1``, or ``num -= 1`` for short.



    .. Naming code

    function definition
        A statement which creates a :term:`function`, such as::

            def add(a, b):
                return a + b
                
    parameter
        Data as received in by a function, given a name in-between the function definition's parentheses, which is local to the function itself.


    .. More on functions

    positional argument
        An :term:`argument` identified by its position in the list of arguments.

    keyword argument
        An :term:`argument` identified by a name e.g. ``f(x=12, y=24)``.


    .. Reading files
    
    file
        A resource for storing information, based on some kind of duration storage.  It is usually persistent, so retains its state when the computer is turned off.


    .. Writing files



    .. Catching errors

    exception
        An interruption in normal processing, especially as caused by an error.
        
    syntax error
        Where the code is breaking the rules of the language, such as misspelling the word ``while``, or missing the colon ``:`` off the end of a ``if`` statement.
        
    logical error
        Where a program behaves in an unexpected or illogical way producing an undesired result, such as an adding program subtracting or a sorting program jumbling up the data.
        
    runtime error
        An error that occurs during the execution of the program, such as a program crashing with unexpected data (e.g. converting non-numerical value into an integer).


    .. Python summary



    .. Extra exercises



    .. Operators



    .. Program flow



    .. Common mistakes



    .. Zen


Some definitions taken from :url:`https://en.wiktionary.org` and :url:`https://www.python.org/`.
