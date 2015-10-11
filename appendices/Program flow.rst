Program flow
============

Sequence
--------

+----------------------------------------+-----------------------------------------+
|                                        |                                         |
| |seq-image|                            | .. code-block:: py3con                  |
|                                        |                                         |
|                                        |     name = input('What is your name? ') |
|                                        |     print('Hello there', name)          |
|                                        |     print('Here is a sum', 10 + 20)     |
|                                        |                                         |
+----------------------------------------+-----------------------------------------+

.. |seq-image| image:: /images/flow/seq.png
    :height: 168pt
    :align: bottom

Selection
---------

+----------------------------------------+-----------------------------------------+
|                                        |                                         |
| |sel-image|                            | .. code-block:: py3con                  |
|                                        |                                         |
|                                        |     num = int(input('Number please: ')) |
|                                        |     if num < 0:                         |
|                                        |         print('Negative!')              |
|                                        |     else:                               |
|                                        |         print('Positive')               |
|                                        |     print('Off we go again...')         |
|                                        |                                         |
+----------------------------------------+-----------------------------------------+

.. |sel-image| image:: /images/flow/selec.png
    :height: 168pt
    :align: bottom


Iteration
---------

+----------------------------------------+-----------------------------------------+
|                                        |                                         |
| |itr-image|                            | .. code-block:: py3con                  |
|                                        |                                         |
|                                        |     num = 0                             |
|                                        |     while num < 10:                     |
|                                        |         print(num)                      |
|                                        |         num = num + 1                   |
|                                        |     print('Off we go again... ')        |
|                                        |                                         |
+----------------------------------------+-----------------------------------------+

.. |itr-image| image:: /images/flow/iter.png
    :height: 168pt
    :align: bottom
