=============
JKCS4_collect
=============

After JKCS2_explore or JKCS3_run submitted jobs are finished, JKCS4_collect script can
be used to collect all data within folder, order the output structures and their properties (such as electronic/free energies, gyration radius, and
dipole moment). 

.. hint: 

   Use the following commands to check if the calculations are finished:
   
   .. code::
   
      JKcheck
      JKcheck XTB
      
JKCS4_collect utilizes JKQC_pickle on all the output files in specified calculation folder. If specified it can also pickle the data to a single file, 
clean unnecessary files, or even remove the whole folder as it is not be required anymore (perhaps, do not remove the DFT folders if you want to check 
the calculations by yourself). Examples:

.. code::

   JKCS4_collect XTB
   JKCS4_collect XTB -JKQC          #creates also pickled files
   JKCS4_collect XTB -JKQCclean     #creates also pickled files + removes unnecesasry files
   JKCS4_collect XTB -JKQCcleanfull #creates also pickled files + removes XTB folder

In the case of ``XTB``, the properties [file-path gyration-radius XTB-energy] would be written into ``collectionXTB.txt``:

.. code:: 

   /path/0-3S0-3B/SYS_2sa_2am/XTB_2_2_0_0_0_0_2_1_0/2sa2am-220000_1_0.xyz    2.675910073831769   -56.7011189
   /path/0-3S0-3B/SYS_2sa_2am/XTB_2_2_0_0_0_0_2_1_0/2sa2am-220000_1_100.xyz  2.4146549048885455  -56.6972184
   /path/0-3S0-3B/SYS_2sa_2am/XTB_2_2_0_0_0_0_2_1_0/2sa2am-220000_1_101.xyz  2.643341483522292   -56.6990367
   ...

Furthermore, uniqueness filtering is performed based on gyration-radius (def. threshold = 0.01 Angstrom) and XTB-energy (def. threshold = 0.001 hartree).
After the filtering, ``resultXTB.dat`` is created, where redundant structures have been removed and files were sorted with respect to energy:

.. code:: 

   /path/0-3S0-3B/SYS_2sa_2am/XTB_2_2_0_0_0_0_2_1_0/2sa2am-220000_1_0.xyz    2.675910073831769   -56.7011189
   /path/0-3S0-3B/SYS_2sa_2am/XTB_2_2_0_0_0_0_2_1_0/2sa2am-220000_1_147.xyz  2.6631961557393793  -56.6997677
   /path/0-3S0-3B/SYS_2sa_2am/XTB_2_2_0_0_0_0_2_1_0/2sa2am-220000_1_139.xyz  2.6832760861366807  -56.6997551
   ...

.. note::

   When collecting data with vibrational frequency calculations, include -gibbs argument to collect also Gibbs free energies. 
   
   .. code::
     
      JKCS4_collect DFT_freq -gibbs
   
   ``resultsDFT_freq.dat`` would be then sorted with respect to the 4th column = Gibbs free energy.

.. hint::

   To reduce propability of removing 2 structures with the same gyration-radius and XTB-energy, include also dipole moment (def. threshold = 0.1 Dy):
   
   .. code::
    
      JKCS4_collect XTB -dip

Moreover, all XYZ structures are also printed to ``movieXTB.xyz``. Users can then easily visualize all the structures using for instance: 

.. code::

   molden movieXTB.xyz

Arguments
---------

:guilabel:`<string>`
    name of the folder which should be analysed (e.g. XTB)

:guilabel:`-JKQC`
    (if not yet) the structures are additionaly pickled into a single file (``collectionXXX.pkl``, see JKQC for more details). 
    
:guilabel:`-JKQCclean`
    same as :guilabel:`-JKQC` + removes unnecessary files (.xyz|.log|.out|.com|.cmd). This saves memory and significantly reduces number of files.
    
:guilabel:`-JKQCcleanfull`
    same as :guilabel:`-JKQC` + completely removes analysed folder. This saves memory and significantly reduces number of files.

:guilabel:`-dip`
    additionaly collects dipole moments
    
:guilabel:`-gibbs`
    additionaly collects Gibbs free energies

As JKCS4_collect uses JKQCpickle to collect the properties of all output files, the
same options can be used to request specific properties to be retrieved and written in ``collectionXXX.txt`` and 
``resultXXX.dat`` files. See more details in JKQC section of this manual. Here are only few interesting examples:

.. code::
 
   JKCS4_collect XTB -pXYZ -rg -el -dip               #the same as: JKCS4_collect XTB -dip
   JKCS4_collect XTB -ePKL -rg -el -JKQCcleanfull     #the same as: JKCS4_collect XTB -JKQCcleanfull
   JKCS4_collect DFT_opt  -pXYZ -rg -el -time         # + comp.time
   JKCS4_collect DFT_freq -pXYZ -rg -el -gibbs        # + Gibbs free energy
   JKCS4_collect DFT_freq -pXYZ -rg -el -gibbs -lf    # + the lowest vib. frequency (check if you are minimum)
   JKCS4_collect DFT_freq -pXYZ -rg -el -gibbs -temp 273.15 -fc 100 -v 0.996 # recalculates for dif. T and does anh. + low.vib.freq. corr.
