================
About & Examples
================

JKCS presents a systematic approach for configurational sampling (CS) of molecular clusters. To perform
CS on a chosen cluster, JKCS starts from the individual monomers that comprise the cluster. Of these monomers, all possible conformers are taken into account. This is done because the optimal structure of an individual monomer is not necessarily the optimal structure for
this monomer inside the cluster. Also, relevant deprotonated and protonated conjugates of monomers
are considered, as proton transfer can occur between components in the cluster. JKCS will find all
possible combinations of these monomer conformers that fulfil the chosen cluster composition and
total charge. Of each of these combinations, a large number of guess structures are created by adding
the conformers together at random orientations. The guess structures of all possible combinations
are subsequently optimized through quantum chemistry calculations at progressively higher levels of
theory. After each optimization, unlikely structures are removed. The filtering out of these structures
allows the next calculation at a higher level of theory to run at a reasonable computational cost. At
the end of the configurational sampling, we end up with just a few appropriate structures that are
optimized at a high level of theory.

It is important to note that there is no guarantee that the global minimum of the cluster is actually found through configurational sampling. It becomes more probable if we include all monomer conformers, use a large number of guess structures and optimize more structures at higher levels of theory, but absolute certainty that the global minimum is found will never be achieved.

JKCS PROVIDES:

 * a collection of scripts which can be used for CS with a large set of structures and files
 * communication with 3rd-party computational programs such as Gaussian, ORCA, ABCluster, and XTB (and for advanced users: CREST, IMoS)
 * automated handling of jobs and submissions to (super)computer clusters
 * it is coupled with JKQC and the pickled file/structures databases can be easily forwarded to JKML for machine-learning purposes

Basic example
-------------

Let us do a simple test on our local/login computer. This test can also help you to verify that you did setup JKCS/JKQC correctly. Go to a working directory and start your first CS test, e.g.:

.. code:: bash

   cd <working-dir>
   JKCS0_copy sa w
   cat input.txt
   JKCS1_prepare
   cd SYS_1sa_1w
   JKCS2_explore -pop 5 -gen 5 -lm 3 -loc
   JKCS4_collect ABC -loc
   cat resultsABC.dat
   molden movieABC.xyz
   JKCS3_run -p XTB -of ABC -loc
   JKCS4_collect XTB -oc -loc
   JKQC collectionXTB.pkl -movie
   mv movie.xyz movieXTB.xyz
   molden movieXTB.xyz
   JKQC collectionXTB.pkl -sort el -select 1 -ePKL -el > resultsXTB_FILTERED.dat
   cat resultsXTB_FILTERED.dat
   JKCS3_run -rf resultsXTB_FILTERED.dat -p XTB -nf XTB_freq -m "--ohess -gfn 1" -loc
   JKCS4_collect XTB_freq -oc -loc
   JKQC collectionXTB_freq.pkl -b -el -g
   
This procedure will prepare input file for CS of sulfuric acid and water dimer. Performs short (and bad) configurational space exploration using ABCluster. Collects the results and visulazize them with molden. Then performs XTB optimization, and again, collects the results and visulazize them with molden. Afterwards, only one lowest XTB energy structure is taken for vibrational frequency analysis again at XTB level. The final file basename, energy, and Gibbs free energy is printed out.

For more details see the other sections of JKCS manual.
For help with individual programs continue reading on this page.

Advanced example
----------------

Here is more advanced example:

.. code:: bash

   JKCS2_explore -pop 3000 -gen 200 -lm 2000/NoC -cpu 1 -time 3-00:00:00 -exploded -par q64,q48,q40,q28,q24,q20
   JKCS3_run -of ABC -nf XTB -m "--gfn 1 --opt" -cpu 1 -time 1-00:00:00 -par q64,q48,q40,q28,q24,q20
   JKCS4_collect XTB -oc -time 1-00:00:00
   JKQC collectionXTB.pkl -unique rg,el,dip -out filteredXTB0.pkl
   sbatch -n 1 JKsend 'JKQC filteredXTB0.pkl -reacted -sort el -select 1000 -noex -out filteredXTB.pkl -ePKL > TO_DO_DFT.dat' | awk '{print $4}' >> .jobs.txt
   JKCS3_run -p G16 -rf TO_DO_DFT.dat -nf DFT_SP -m "# wb97xd 6-31++g**" -time 2:00:00 -cpu 8 -maxtasks 10000 -arraymax 25
   JKCS4_collect DFT_SP -oc -time 1-00:00:00
   JKQC collectionDFT_SP.pkl -sort el -select 100 -noex -ePKL > runDFT.dat
   JKCS3_run -p G16 -rf runDFT.dat -nf DFT_opt -m "# wb97xd 6-31++g** opt" -time 3-00:00:00 -cpu 8 -maxtasks 10000 -arraymax 25
   JKCS4_collect DFT_opt -oc -time 1-00:00:00
   JKQC collectionDFT_opt.pkl -noex -ePKL > runDFTO.dat
   JKCS3_run -p G16 -rf runDFTO.dat -nf DFT_freq -m "# wb97xd 6-31++g** freq" -time 1-00:00:00 -cpu 8 -maxtasks 10000 -arraymax 25
   JKCS4_collect DFT_freq -time 1-00:00:00 -oc
   JKQC collectionDFT_freq.pkl -pass lf 0 -sort g -fc 100 -v 0.996 -select 5 -noex -ePKL > runDLPNO.dat
   JKCS3_run -p ORCA -rf runDLPNO.dat -nf DLPNO -m "! aug-cc-pVTZ aug-cc-pVTZ/C cc-pVTZ-F12-CABS DLPNO-CCSD(T) TightSCF" -time 2-00:00:00 -cpu 8 -mem 20gb
   JKCS4_collect DLPNO -time 1-00:00:00 -orca -oc

The very same thing with comments:

.. code:: bash

   #configurational sampling that produces over all possible
   # monomer cominations only 2000 minima. The files are in 
   # the end pickled to save mo
   JKCS2_explore -pop 3000 -gen 200 -lm 2000/NoC -cpu 1 -time 3-00:00:00 -exploded -par q64,q48,q40,q28,q24,q20
   JKCS3_run -of ABC -nf XTB -m "--gfn 1 --opt" -cpu 1 -time 1-00:00:00 -par q64,q48,q40,q28,q24,q20
   JKCS4_collect XTB -oc -time 1-00:00:00
   JKQC collectionXTB.pkl -unique rg,el,dip -out filteredXTB0.pkl
   sbatch -n 1 JKsend 'JKQC filteredXTB0.pkl -reacted -sort el -select 1000 -noex -out filteredXTB.pkl -ePKL > TO_DO_DFT.dat' | awk '{print $4}' >> .jobs.txt
   JKCS3_run -p G16 -rf TO_DO_DFT.dat -nf DFT_SP -m "# wb97xd 6-31++g**" -time 2:00:00 -cpu 8 -maxtasks 10000 -arraymax 25
   JKCS4_collect DFT_SP -oc -time 1-00:00:00
   JKQC collectionDFT_SP.pkl -sort el -select 100 -noex -ePKL > runDFT.dat
   JKCS3_run -p G16 -rf runDFT.dat -nf DFT_opt -m "# wb97xd 6-31++g** opt" -time 3-00:00:00 -cpu 8 -maxtasks 10000 -arraymax 25
   JKCS4_collect DFT_opt -oc -time 1-00:00:00
   JKQC collectionDFT_opt.pkl -noex -ePKL > runDFTO.dat
   JKCS3_run -p G16 -rf runDFTO.dat -nf DFT_freq -m "# wb97xd 6-31++g** freq" -time 1-00:00:00 -cpu 8 -maxtasks 10000 -arraymax 25
   JKCS4_collect DFT_freq -time 1-00:00:00 -oc
   JKQC collectionDFT_freq.pkl -pass lf 0 -sort g -fc 100 -v 0.996 -select 5 -noex -ePKL > runDLPNO.dat
   JKCS3_run -p ORCA -rf runDLPNO.dat -nf DLPNO -m "! aug-cc-pVTZ aug-cc-pVTZ/C cc-pVTZ-F12-CABS DLPNO-CCSD(T) TightSCF" -time 2-00:00:00 -cpu 8 -mem 20gb
   JKCS4_collect DLPNO -time 1-00:00:00 -orca -oc

Tips & Tricks
-------------

**GLOBAL MINIMUM**

There is no guarantee that the global minimum of the cluster is actually found
through configurational sampling. It becomes more probable if we include all
monomer conformers, use a large number of guess structures and optimize more
structures at higher levels of theory, but absolute certainty that the global
minimum is found will never be achieved.

**DETAIL OF OUTPUT**

The amount of printed output can be adjusted by using command ‘-print NUM’:

 * -print 0 .... basically just error messages
 * -print 1 .... [DEFAULT] traditional output
 * -print 2 .... enlarged output, all algorithm steps are commented
 * -print 3 .... very very detailed output
 
**PREVIOUS COMMANDS**

The JKCS/JKQC/JKML commands are saved into the 'output' file. You can examine them by:

.. code::

   grep COMMAND output

**CALLING JKCS COMMANDS**

Each JKCS command can be performed inside a specific subfolder ‘SYS_{system}’,
or from your ‘parent directory’ where the subfolders are located. In this case
the algorithm enters each directory and performs the command there.

If you wish to perform a command from your ‘mother directory’, but only for
some specific subfolders, you can give the subfolder as an argument:

.. code:: 

   JKCS2_explore SYS_3SA SYS_4SA -gen 100
   JKCS2_explore SYS_1SA_1-5AM -pop 2000 -gen 150
   
**JKcheck**

JKcheck can be used to check how many calculations have been finished.

**ORDER OF ARGUMENTS**

The order of arguments does not matter.

**COLORS & SYMBOLS IN PRINTED OUTPUT**

The colors and symbols in the printed output of JKCS commands can be turned off in 2 ways:

* Change Qsymbol or Qcolours in ~/.JKCSusersetup.txt to "no"
* COLORING TEXT: use -nocolors argument to have text without colors
* KISSING SYMBOL: use -nosymbol to remove the symbol in the begging of output

**‘M’ & ‘NoC’ SYMBOLS**

These symbols can be used with many JKCS commands to make values dependent on
the ‘number of Molecules’ or ‘Number of Combinations’. When a lot of conformers
are taken into account for a certain monomer, ‘NoC’ can become very large.
Therefore, always be mindful of the result that using ‘M’ and ‘NoC’ might have
for the exploration of all studied systems. Example: 

.. code:: bash
    
   JKCS2_explore -pop 1000*M -gen 100 -lm 4000/NoC
   
**BOSS AND MANAGER**

Manager can run multiple JKCS commands and wait until these are finished. The commands to be executed are read from a txt file. Each command should be put on a separate line. Boss can handle several managers. Since these are already complicated command with self-submission, I will not provide manual for those and only if you consider yourself an experienced user, contact J. Kubečka and he will provide the manual. 
   
