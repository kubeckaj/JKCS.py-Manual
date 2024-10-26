=========
JKCS3_run
=========

JKCS3_run utilizes 3rd-party programs to optimize clusters and evaluate their properties (e.g., electronic energy or free energies). 
The script either uses the output structures in the folder from previous step (e.g., ``XTB``, ``ABC``, ``DFT_opt``) or those listed in a file (e.g., ``resultsXTB.dat``). 

.. hint::

   For help use:
   
   .. code:: bash
   
      JKCS3_run -help

For instance, if you want to run XTB calculations on structures from ``ABC`` folder, you run (of = old folder):

.. code::

   JKCS3_run -of ABC
   JKCS3_run          #this would do the same
   
If you did collect (and filter) structures into a file (e.g., ``resultsXTB.dat``), to use those run (rf = results file):

.. code::
  
   #JKCS4_collect XTB
   JKCS3_run -p G16 -m "# wb97xd 6-31++g** opt=verytight" -nf DFT_opt -rf XTB 
   JKCS3_run -p G16 -m "# wb97xd 6-31++g** opt=verytight" -nf DFT_opt -rf resultsXTB.dat #this would do the same

If you did extra-filter the data and ``resultsXXX_FILTERED.dat`` exists, it will be used instead of ``resultsXXX.dat``:

.. code::
  
   #JKCS4_collect XTB
   #JKCS5_filter -d 10  #selects only the 10 lowest kcal/mol
   JKCS3_run -p G16 -m "# wb97xd 6-31++g** opt=verytight" -nf DFT_opt -rf XTB 
   JKCS3_run -p G16 -m "# wb97xd 6-31++g** opt=verytight" -nf DFT_opt -rf resultsXTB_FILTERED.dat #this would do the same
   
.. hint::

   You can check if your calculations are still running by using:
   
   .. code::
     
      JKcheck
      JKcheck XTB
      
.. note::

   Charges and multiplicities are handled by JKCS based on ``parameters.txt``

XTB examples
------------

After ABC exploration, you can directly run XTB by:

.. code::
  
   JKCS3_run
   JKCS3_run       -p XTB        -of ABC        -nf XTB      -m "-opt vtight" #this would do the same
   JKCS3_run -program XTB -oldfolder ABC -newfolder XTB -method "-opt vtight" #this would do the same
   
Some other options:

.. code::
  
   JKCS3_run -p XTB -of ABC -nf XTB      -m "-opt vtight --gfn 1"
   JKCS3_run -p XTB -rf XTB -nf XTB_freq -m "-ohess -temp 298.15"

.. note::

   If you did pickle structures after ABC exploration, you should use -JKQC command also now:

   .. code::
   
      #JKCS2_explore -gen 200 -pop 1000 -lm 3000 -JKQC
      JKCS3_run -JKQC
      
Gaussian examples
-----------------

JKCS is well working with Gaussian16 = G16. Although, it should work with other versions as well. The commands are similar to those in XTB. Examples:

.. code::

   JKCS3_run -p G16 -rf XTB     -nf DFT_sp   -m "# HF 6-31+g*"
   JKCS3_run -p G16 -rf XTB     -nf DFT_opt  -m "# wb97xd 6-31++g** opt=verytight"
   JKCS3_run -p G16 -rf DFT_opt -nf DFT_freq -m "# wb97xd 6-31++g** freq"
   JKCS3_run -p G16 -rf XTB     -nf DFT      -m "# wb97xd GEN Pseudo=Read Opt Int=UltraFine Freq MaxDisk=32GB" -bc I -mem 12GB -cpu 16

ORCA examples
-------------

This is not that well tested as people usually use their own scripts for ORCA, however, you should be able to run it as well. Examples:

.. code::

   JKCS3_run -p ORCA -rf XTB      -nf OPT   -m "! PBE0 def2-TZVP TIGHTSCF Opt D3BJ"
   JKCS3_run -p ORCA -rf DFT_freq -nf DLPNO -m "! DLPNO-CCSD(T) aug-cc-pvtz aug-cc-pvtz/C GRID4 nofinalgrid TightPNO TightSCF NOPOP NOPRINTMOS"

Arguments
---------

:guilabel:`-JKQC`
     after the run, the structures are pickled into a single file (``database.pkl``, see JKQC for more details). 
     This saves memory and significantly reduces number of files.
    
:guilabel:`-nf, -newfolder <string>`
    name of the new (calculation) folder. [default = "XTB"]
    
:guilabel:`-of, -oldfolder <string>`
    name of the old (calculation) folder. Do not combine with -rf. [default = "ABC"]
    
:guilabel:`-rf, -resultsfile <string>`
    name of the results file (e.g., XTB, resultsXTB.dat, resultsXTB_FILTERED.dat) containing list of structures for further calculation.
    When -rf "NAME" is used and ``resultsNAME_FILTERED.dat`` is available, it is used instead of ``resultsNAME.dat``. Do not combine with -of.

:guilabel:`-m, -method <string>`
    method used by 3rd-party program [default for XTB = "-opt vtight"]
 
:guilabel:`-bs, -add, -addbase <atom>` 
    insert basis set for heavy atoms to the end of file (only for Gaussian) and yet only for atoms like I or Br
  
