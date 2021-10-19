Usage
=====

.. _installation:

RUNNING
-------

To run JKQC use:

.. code-block:: console

   $ python JKQC.py

DATABASE
--------

To add some clusters to the Database folder, you can use the :sh:func:`sh addJKQC.sh` command.

!!! I strongly recommend to check the :sh:func:`JKname` parameters

For example (sulfuric acid--ammonia):

>>> sh ../addJKQC.sh -sf results_A+SA_positivemode/ -df Besel19 -arg "-mol N1H3 am -mol H2S1O4 sa -mol H1S1O4 sam"

