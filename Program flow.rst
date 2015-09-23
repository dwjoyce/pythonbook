Program flow
============

Sequence
--------

+----------------------------------------+-----------------------------------------+
|                                        |                                         |
| |seq-image|                            | .. code:: python                        |
|                                        |                                         |
|                                        |     name = input('What is your name? ') |
|                                        |     print('Hello there', name)          |
|                                        |     print('Here is a sum', 10 + 20)     |
|                                        |                                         |
+----------------------------------------+-----------------------------------------+

.. |seq-image| image:: flow/seq.png
    :height: 140pt
    :align: bottom

Selection
---------

+----------------------------------------+-----------------------------------------+
|                                        |                                         |
| |sel-image|                            | .. code:: python                        |
|                                        |                                         |
|                                        |     num = int(input('Number please: ')) |
|                                        |     if num < 0:                         |
|                                        |         print('Negative!')              |
|                                        |     else:                               |
|                                        |         print('Positive')               |
|                                        |     print('Off we go again...')         |
|                                        |                                         |
+----------------------------------------+-----------------------------------------+

.. |sel-image| image:: flow/selec.png
    :height: 140pt
    :align: bottom


Iteration
---------

+----------------------------------------+-----------------------------------------+
|                                        |                                         |
| |itr-image|                            | .. code:: python                        |
|                                        |                                         |
|                                        |     num = 0                             |
|                                        |     while num < 10:                     |
|                                        |         print(num)                      |
|                                        |         num = num + 1                   |
|                                        |     print('Off we go again... ')        |
|                                        |                                         |
+----------------------------------------+-----------------------------------------+

.. |itr-image| image:: flow/iter.png
    :height: 150pt
    :align: bottom
