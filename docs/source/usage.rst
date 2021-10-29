Usage
=====

.. _installation:

Installation
------------

Activate JKCS python environment for Jupyter

.. code-block:: console

   (.venv) $ pip install --user ipykernel
   (.venv) $ python -m ipykernel install --user --name=jkcs

HOW TO
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: good job

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

