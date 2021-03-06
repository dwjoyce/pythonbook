Starting with Python's IDLE
===========================

.. quote::
    :author: Linus Torvalds

    Most of the good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program.

Introduction
------------

Welcome to our guide on learning Python!

Programming is the art of logical thinking.  It is the process of breaking down a problem or task into simple steps so even a dumb computer can follow them.  These steps are written down according to a set notation, so that a computer can translate them into its own machine code.  Thankfully, people no longer have to program in machine code themselves, made up of numbers, but in a higher form, constructed mainly from English words.  Computer languages are different from human languages in that they are formal and unambiguous.  The formal aspect means they are specified in advance with a set notation and the use of keywords.  They are unambiguous so that the program will always do the same thing every time, given the same circumstances.

Knowing how to program a computer is a great skill to have, even if you are not a professional programmer.  You can program in almost any field of work - especially when you need to transform data (the basis of information) from one form to another.  It means you are not simply using other people's work, but you have the ability create for new programs by yourself.  If you can never program a computer, it is like living in a world that you can only read other people's writing, unable to write for yourself.  Programming is very much a creative process - you are instructing a computer to follow your what you are thinking, down to the letter!

Python is a fantastic first computer language to learn.  It is easy to pick up, but at the same time is very useful to computer professionals so is not just a beginner's language.  It is used by large companies such as NASA, Disney, Google, YouTube, Microsoft, Yahoo and Dropbox.  It is also used by many educational institutions when learning programming, such as Cambridge University.  It also has the advantage of being free and open source software, so you can download it at home free of charge.  This also means you can study how it works.

It was created in the early 1990s by the Dutch programmer Guido van Rossum.  It has been updated many times since then, and in this book we will be using Python 3.  The exact version of Python 3 does not matter so much, as long as your version is Python 3.something.  This is for when you are trying to program at home.

Code written in Python is very readable.  It lacks much of the cryptic notation that other languages use to express themselves.  It almost reads like :term:`pseudo-code` - a description of how a program should operate as written in lines of plain English.

Python is also very interactive.  This means that you can experiment with the language, getting to know it better, without a cumbersome process getting in the way.  Although we will write proper programs later (from :ref:`chapter 6` - First Program), initially we will use Python's interactive interpreter to start off.  It is called an :term:`interactive interpreter` because you type lines of code (known as :term:`statements`) and get the answer straight away, i.e. interactively.  It is an interpreter because it translates the lines of Python into a form that the computer can understand directly.

What we will be learning
------------------------

We will be learning the basics of the Python language, just enough for us to write interesting and challenging programs (and have a bit of fun).

We will cover data types, organising our data and code, opening and reading files on disk, handling errors.  We introduce the three ways code can flow - sequentially, selectively and iteratively.  We will not cover more advanced features in any detail such as object orientated programming, dictionaries, list comprehensions, lambdas, generators, decorators, and the like.  We may use some of these features, but not code them ourselves.  In fact, what we do teach will not be covered in great depth, only enough for you to start programming yourself.  Not only do we not have time for this, but these topics are not entirely necessary to do the programming we want to achieve.

This book unfolds in a way that should be familiar to school children.  We first use Python to perform calculations and call functions, just as you have learnt in your maths class.  The arithmetic is calculated in a way familiar to those using proper scientific calculators, not basic ones.  We use the language to store values in memory, again just like a calculator, but in more flexible manner.  Only then do we move onto writing complete programs and using concepts that are less familiar to those following a high school curriculum.  We use the Raspberry Pi as our hardware platform, as reflected in the pictures, but any computer could be used instead, particularly at home.

It is encouraged to use this book as a starting point, and then use other resources to continue your practice in the art of programming.  Remember, it is all about being creative and getting computers to follow our instructions!

How to get going
----------------

We first use the interactive interpreter to start with Python.  Even when introducing more advanced language features, we will still use this shell to experiment before moving onto a proper program.  A proper program is one typed into its own file, and then the program is started separately.  This is similar to how we use other programs (e.g. LibreOffice or Firefox) - we use the final result.  This is known as :term:`running` or executing the program.  However, at this stage, we only use the interactive interpreter.

Python's interactive interpreter is known as :term:`IDLE`.  This name comes from the acronym :term:`IDE`, which stands for Integrated Development Environment - a program that allows you to develop or create other programs.  It contains an editor, used to type your code, and a way of running your programs.  IDLE also contains the interactive interpreter that allows us to experiment line by line.

To start IDLE, either click on the IDLE icon on the desktop or select the IDLE program from the Applications menu in the bottom left:

.. image:: /images/screenshots/desktop.png
    :width: 90%
    :align: center

IDLE will then start, and you will have a window on your screen which looks like this:

.. image:: /images/screenshots/idle_blank.png
    :width: 90%
    :align: center

You are now ready to go.

Later, in :ref:`chapter 6` on your First Program, you will position this IDLE window slightly differently in order for you to see both the program you are writing and the interactive interpreter at the same time.  Until then, this is all you need to know about starting Python's shell.  Next chapter - typing in some code and seeing what happens!

Things to remember
------------------

#. Click on the IDLE desktop or panel icon to start Python's interactive interpreter.

#. Type away in the interactive interpreter and see what results you get.  Don't be afraid to experiment, you can't break the computer that easily.  Fortune rewards the brave!

#. To recall something already typed in, use the up arrow to move the cursor onto the line you wish to use.  Press the :button:`Return` or :button:`Enter` key - this brings it down onto your current line.  You can modify what has been copied down.  To run the line again, press the :button:`Return` or :button:`Enter` key a second time.  This will save you lots of typing!

#. Read these *Things to remember* sections in each chapter very carefully and remember what they say!
