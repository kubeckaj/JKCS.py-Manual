====================
Setup & Installation
====================

Jammy Key for Quantum Chemistry data of molecular clusters.

These scripts converts the quantum chemistry output files (.log,.out,.xyz) into database (.pkl), which is takes significantly less memory and accelerates the data post-processing (e.g., printing energies, including various corrections, and calculation formation properties for ACDC). This script is not parralelized (at least yet), and thus, using more CPU has a minimal gain. Depending on the files sizes/cluster sizes/types, the pikling takes approximately from 15 seconds/1000 structures to 3 minutes/1000 structures. Nevertheless, the post-processing usually takes from -immidiately- to a few seconds.

.. contents::

Simple examples
===============

Database manipulation
---------------------

Collect data from .log (and .xyz, .out) files and pickle them into a database:

.. code:: bash
   
   python JKQC.py *.log -out local_database.pkl
   
Add data into database:

.. code:: bash
   
   python JKQC.py *.log -in local_database.pkl -out local_database.pkl
   
Connect two databases:

.. code:: bash
   
   python JKQC.py -in database1.pkl -in database2.pkl -out joined_database.pkl
   python JKQC.py database1.pkl database2.pkl -out joined_database.pkl
   
Extract part of a database !!! NOT FUNCTIONAL YET !!!:

.. code:: bash
   
   python JKQC.py -in mydatabase.pkl -extract 1sa2w -out 1sa2w_database.pkl

Quantum chemistry data
----------------------

Extract (name and) electronic energy from files/database:

.. code:: bash
   
   python JKQC.py *.log -b -el
   python JKQC.py database.pkl -b -el //significantly faster
   
Extract (name and) electronic energy for a specific cluster(s) !!! NOT FUNCTIONAL YET !!!:

.. code:: bash
   
   python JKQC.py -in mydatabase.pkl -extract 1sa2w -b -el
   python JKQC.py -in mydatabase.pkl -extract 3sa,1sa0-10w -b -el

Extract (name and) gibbs free energy corrected for SP DLPNO-CCSD(T) energy (Orca) !!! NOT FUNCTIONAL YET !!!:

.. code:: bash
   
   python JKQC.py -in mydatabase.pkl -b -GD
   
Extract (name and) enthalpy and entropy:

.. code:: bash
   
   python JKQC.py -in mydatabase.pkl -b -h -s
   
Calculate formation Gibbs free energy (global minimum approximation) !!! NOT FUNCTIONAL YET !!!:

.. code:: bash
   
   python JKQC.py -in mydatabase.pkl -extract 1sa,2sa -b -GD -formation
   

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
    * - 1tma = trimethylamine
      - 1tma1p = trimethylammonium
      -
    * - 1eda = ethylamine
      - 1eda1p = ethylammonium
      - 
    * - 1gd = guanidine
      - 1gd1p = guanidium
      -
    * - 1w = water
      - 1w1p = hydronium
      - 1oh = hydroxide

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

   python JKQC.py <Files> <Database> <Parameters> 

Database manipulation
---------------------
 
  <Files> 
  
input files can be any .log, .out, and .xyz files, or

--in database.pkl
  input .pkl database (the --in command is actually not necessary)

.. list-table:: Input data
    :widths: 30 30
    :header-rows: 1
    
    * - Specified
      - Description
    * - NOTHING
      - takes in all .log files working in folder
    * - FILES
      - takes in all specified .log, .out, .xyz files
    * - DATABASES
      - takes in all specified (-in) .pkl databases
    * - COMBINED
      - FILES and DATABASES combined 

--out database.pkl
  output .pkl database (the --out command is necessary)
  
.. list-table:: Output database
    :widths: 30 30
    :header-rows: 1
    
    * - Specified
      - Description
    * - NOTHING
      - in classified conditions: mydatabase.out
    * - DATABASE
      - saves all input data into -out specified .pkl database

INFO
----
--b,--basename
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




