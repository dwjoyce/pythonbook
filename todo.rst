TODO
====

.. todolist::

     
Test Area
=========

Inline code: ``[str(i) + "#" for i in range(0, len(dir(__builtins__))) if i < 24.6]``

.. attention:: attention
.. caution:: caution
.. danger:: danger
.. error:: error
.. hint:: hint
.. important:: important
.. note:: note
.. tip:: tip
.. warning:: warning


More code::

    print('one')
    print('two')

    x = 3
    to_b = True

    if x == 1:
        print('one')

    cond1 = x and x or x and not x
    cond2 = to_b or not to_b
    if cond1 and cond2:
        # do something or just
        pass

.. pythontest:: off

.. code:: python

    this will break

.. pythontest:: on

.. code:: python

    this_will_not_break = 1



.. code-block:: python
    :pythontest: off

    this will also break!
