Python as a Calculator
======================

Let us start our journey by taking inspiration from something we all know well - your pocket calcualtor.

To perform a sum on a calculator, such as 10 plus 20, you could simply hit the following buttons:

    10 + 20

and then hit the = (equals) button.  The result, 30, will then appear on your screen.  We could do other operations as well, such as subtraction, division and multiplication, like so:

    10 + 20 - 4 ÷ 2 x 3

and then finally hitting the equals sign, you will get a result of 39 displayed on the calculator's screen, performing the calculation as it goes along, one step at a time.

So given their name, we should be able to use "computers" to do some "computing", that is, working with numbers.  Particularly, we should be able to use our new programing language, Python, to do this for us.

Using the first example, the Python code is very simple.

Bring up your Python interactive shell, as described in chapter 0, and type the following:

    print(10 + 20)

and press the Return or Enter key on your keyboard.  You should see the number 30 displayed below.

What is the word "print" for?  In Python, it is calling a piece of code named "print", that calculates the sum you have given it, and displays the result on the screen.  By using brackets after its name, you are actually using the print code, otherwise it will not work as you expect.

How about the second example.  Let us try this:

    print(10 + 20 - 4 / 2 * 3)
    
Firstly, what is this "/" and "*" symbols?  Well, the "÷" doesn't actually appear on your computer keyboard, so we use another symbol "/" instead.  And the "x" is too much like the letter "x", so we use the asterix "*" symbol instead.

Type in it, press Return and see what the result is.  Is it 39 like when we used the calculator?  No, it is 24!  Why?

Well, unlike a calculator, but like proper Maths, a computer language does not work out the sum from left to right - it gives priority - precedence - to some operations over others.  It actually performs the divide first (4 divided by 2, equalling 2), then the multiply (2 times 3, equalling 6), then the addition (10 plus 20 equalling 30) and finally the subtraction (30 minus 6 equalling 24).

To enforce a different order, you can use brackets.  Just like in Maths.  Put a set of brackets around each part of the sum you want done separately.  So if we want to do the above sum in the order of the calculator, we have to do the following:

    print(((10 + 20) - 4) / 2 * 3)

Exercise
========

1. Type the Python line to work out 3 plus 5 divided by 2.
2. Type the Python line to work out 4 times 2 minus 7.
3. To convert from celsius to fahrenheit temperature, you multiply the celsius by 9 divided by 5, and add 32.  If the Celsius is 40, what is the fahrenheit reading?


Things to remember
==================

1. Use numbers with arithmetic operators such as + (addition), - (subtraction), / (division) and * (multiplication).
2. Use brackets to force Python to do a calculation in a particular order
3. Use the print function to display something on the screen.
