=====================
Database Manipulation
=====================

You can call JKQCpickle.py in one of the following format:

.. code:: bash

   JKpython
   python <FULL-PATH>JKQCpickle.py <Files> <Database> <Options/Parameters> 
   
   JKpython
   JKQCpickle <Files> <Database> <Options/Parameters> 
   
   JKgaussstat <Files> <Database> <Options/Parameters> 

Print (name and) electronic energy from files/database:

.. code:: bash
   
   JKgaussstat *.log -b -el
   JKgaussstat database.pkl -b -el //significantly faster
   
Extract (name and) electronic energy for a specific cluster(s):

.. code:: bash
   
   JKgaussstat -in mydatabase.pkl -extract 1sa2w -b -el
   JKgaussstat -in mydatabase.pkl -extract 3sa,1sa0-10w -b -el

Extract (name and) gibbs free energy corrected for SP DLPNO-CCSD(T) energy (Orca) !!! NOT FUNCTIONAL YET !!!:

.. code:: bash
   
   JKgaussstat -in mydatabase.pkl -b -GD
   
Extract (name and) enthalpy and entropy:

.. code:: bash
   
   JKgaussstat -in mydatabase.pkl -b -h -s
   
Calculate formation Gibbs free energy (global minimum approximation) !!! NOT FUNCTIONAL YET !!!:

.. code:: bash
   
   JKgaussstat -in mydatabase.pkl -extract 1sa,2sa -b -GD -formation
   

Database manipulation
---------------------
 
:guilabel:`<Files>`  
  
input files can be any .log, .out, and .xyz files, or

:guilabel:`--in database.pkl`
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

:guilabel:`--out database.pkl`
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
:guilabel:`--b,--basename`
  base name of the given files (e.g. for \data\1sa1am.log -> 1sa1am)
  
QC-data
-------
:guilabel:``--el,--elec`
  electronic energy (total energy in the case of XTB and ABCluster)
:guilabel:`--g,--gibbs`
  Gibbs free energy (**NOT YET** adjustable by QC-corrections)
  
QC-corrections
--------------
:guilabel:`--t,--temp *<real>*`
  temperature

--- TO BE FILLED LATER --- For now you can see the rest of documentation here:

.. code:: bash

    JKgaussstat -help
