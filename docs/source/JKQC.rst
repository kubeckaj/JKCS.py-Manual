JKQC
====

Jammy Key for Quantum Chemistry data of molecular clusters.

RUNNING
-------

To run JKQC use:

   $ python JKQC.py

DATABASE
--------

To add some clusters to the Database folder, you can use the `sh addJKQC.sh` command.

!!! I strongly recommend to check the `JKname` parameters

For example (sulfuric acid--ammonia):

>>> # -sf = source folder name
>>> # -df = database folder name (use the cite format)
>>> # -arg = JKname arguments
>>> sh addJKQC.sh -sf results/ -df Besel19 -arg "-mol N1H3 am -mol H2S1O4 sa -mol H1S1O4 sam"

MOLECULE NAMES IN THE DATABASE
------------------------------

> p - proton
> am - ammonia
> sa - sulfuric acid
> sam - bisulfate
> dma - dimethylammine
> gd - guanidine
