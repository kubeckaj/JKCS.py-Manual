=============
JKCS4_collect
=============

After JKCS2_explore or JKCS3_run submitted jobs are finished, JKCS4_collect script collects all data within the calculation folder. 

.. hint: 

   Use the following commands to check if the calculations are finished:
   
   .. code::
   
      JKcheck
      JKcheck XTB
      
JKCS4_collect utilises JKQC to go through all the output files within specified calculation folder. 

.. code::

   JKCS4_collect XTB
   JKCS4_collect DFT_freq
   
The main outcome of the JKCS4_collect is, e.g., ``collectionXTB.pkl`` file. However, some other readable files are produced, too: ``collectionXTB.txt`` (list of files, gyration radii *Rg*, and energies *E*), ``resultsXTB.dat`` (the same file but after filtering based on *[Rg,E]* with thresholds of *[0.01,0.001]*, and structures are sorted with respect to energy), and ``movieXTB.xyz`` (list of xyz concatenated within one file). For instance, the ``collectionXTB.txt`` could contain: 

.. code:: 

   /path/SYS_2sa_2am/XTB_2_2_0_0_0_0_2_1_0/2sa2am-220000_1_0.xyz	2.675910073831769   -56.7011189
   /path/SYS_2sa_2am/XTB_2_2_0_0_0_0_2_1_0/2sa2am-220000_1_100.xyz	2.4146549048885455  -56.6972184
   /path/SYS_2sa_2am/XTB_2_2_0_0_0_0_2_1_0/2sa2am-220000_1_101.xyz	2.643341483522292   -56.6990367
   ...

.. note::

   When collecting data with vibrational frequency calculations, the structures in, e.g., ``resultsDFT_freq.dat`` will be then sorted with respect to the 4th column = Gibbs free energy.

.. hint::

  The ``movieXTB.xyz`` can be easily visualize with Molden: 

  .. code::

     molden movieXTB.xyz

If you find the ``collectionXTB.txt``, ``resultsXTB.dat``, and ``movieXTB.xyz`` files unecessary, you can only collect (:guilabel:`-oc`) the pickle:

.. code::

   JKCS4_collect XTB -oc

.. hint::

   I strongly recommend checking JKQC manual for structure post-processing and manipulation of, e.g., ``collectionXTB.pkl`` file.
   
The JKCS4_collect is submission script. If you used JKCS2_explore or JKCS3_run with the :guilabel:`-of` argument, then X+1 jobs will be submitted, i.e. one for each subfolder and one for collecting all pickles into one with post-processing (unless the :guilabel:`-oc` argument (only collect) is used). In other case, 1+1 jobs are submitted. You can use all submission argument to control the submission (see the submission section), e.g.:

.. code::

   JKCS4_collect XTB -oc -tpj 2 -cleanfull
   JKCS4_collect DFT_freq -loc
   JKCS4_collect ABC -par q64 -cpu 1 -time 1-00:00:00 -arraymax 2
   JKCS4_collect DLPNO -oc -par qtest -time 10:00


## API

:guilabel:`<string>`
    name of the folder which should be analysed (e.g. XTB)
    
:guilabel:`-clean`
    after collecting, removes all unnecessary files (.xyz|.log|.out|.com|.cmd). This saves memory and significantly reduces number of files.
    
:guilabel:`-cleanfull`
    after collecting, completely removes the analysed folder. This saves memory and significantly reduces number of files.
    
:guilabel:`-JKQCrecollect`
    if it happens that something fails, or you did collect folder when the jobs were still running, then the pickle files in subfolders are already created and you must force to recollect the QC outputs by this argument. (Equivalent to `rm XTB/*/*/*.pkl XTB/*/*.pkl` on init.)

