------
 JKQC
------

Jammy Key for Quantum Chemistry data of molecular clusters.

.. contents::

Requirements
============

Input files
-----------

.. list-table:: Nomenclature for molecules
    :widths: 30 30 30
    :header-rows: 1

    * - neutral
      - positive
      - negative
    * - 1sa = sulfuric acid
      - 
      - 1b = bisulphate
    * - 1msa = methanesulfonic acid
      - 
      - 1mb = methanebisulphate
    * - 1am = ammonia
      - 1am1p = ammonium
      -
    * - 1ma = methyammine
      - 1ma1p = methylammonium
      - 
    * - 1dma = dimethylamine
      - 1dma1p = dimethylammonium
      -
    * - 1gd = guanidine
      - 1gd1p = guanidium
      -
    * - 1eda = ethylamine
      - 1eda1p = ethylammonium
      - 

Rename files
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
   
JKQCprint.py
============

.. code:: bash

   python JKQC.py <Database> <Parameters> #e.g.: python JKQC.py mydatabase.pkl -b -el

INFO
----
--b
  base name of the given files (e.g. for \data\1sa1am.log -> 1sa1am)
  
QC-data
-------
--el,--elec
  electronic energy (total energy in the case of XTB and ABCluster)
--g,--gibbs
  Gibbs free energy (**NOT YET** adjustable by QC-corrections)
  
QC-corrections
--------------
--t,--temp *<real>*
  temperature

+-----------------+----------+----------+----------+----------+----------+
| **<Parameter>** | **G16**  | **XTB**  | **ORCA** | **ABC**  | **XYZ**  |
+-----------------+----------+----------+----------+----------+----------+
| -b,-basename    |   YES    |   YES    |   YES    |   YES    |   YES    |                                            
+-----------------+----------+----------+----------+----------+----------+
| -el,-elec       |   YES    |          |          |          |          |                        
| -g              |   YES    |          |          |          |          | 
+-----------------+----------+----------+----------+----------+----------+
| -t *<real>*     |          |          |          |          |          |  
+-----------------+----------+----------+----------+----------+----------+




