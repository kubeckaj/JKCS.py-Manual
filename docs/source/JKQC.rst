JKQC
====

Jammy Key for Quantum Chemistry data of molecular clusters.


Nomenclature
------------

.. p - proton
.. am - ammonia
.. sa - sulfuric acid
.. sam - bisulfate
.. dma - dimethylammine
.. gd - guanidine

Requirements
------------

Your source folder has to contain calculations for all monomers!
Follow the nomenclature for renaming the file names.
To add some clusters to the Database folder, you can use the ``sh addJKQC.sh`` command.

!!! I strongly recommend to check the ``JKname`` parameters

For example (sulfuric acid--ammonia):

>>> # -sf = source folder name
>>> # -df = database folder name (use the cite format)
>>> # -arg = JKname arguments

.. code:: bash

   sh addJKQC.sh -sf results/ -df Besel19 -arg "-mol N1H3 am -mol H2S1O4 sa -mol H1S1O4 sam"

Pikle database
--------------

To run JKQC use (yet the file input and output has to be modified in the script):

.. code:: bash

   python JKQC.py



