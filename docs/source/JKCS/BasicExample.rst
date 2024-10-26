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
   JKQC filteredXTB0.pkl -reacted -sort el -select 1000 -noex -out filteredXTB.pkl -ePKL > TO_DO_DFT.dat
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
   # the end pickled and remove to save memory. Structures 
   # with large radius are completely removed.
   JKCS2_explore -pop 3000 -gen 200 -lm 2000/NoC -cpu 1 -time 3-00:00:00 -exploded -par q64,q48,q40,q28,q24,q20
   
   #Performs XTB optimization with the same folder architecture
   # as in the ABC folder, i.e. one job is submitted for each
   # conformer combination and optimizing 2000/NoC structures
   JKCS3_run -of ABC -nf XTB -m "--gfn 1 --opt" -cpu 1 -time 1-00:00:00 -par q64,q48,q40,q28,q24,q20
   
   #This will Only Collect the pickle file: collectionXTB.pkl
   JKCS4_collect XTB -oc -time 1-00:00:00
   
   #Here we get rid of those structrues that converged to the same 
   # minima, i.e. having the same configuration. For that we compare
   # similarity between electronic energy, gyration radius and dipole
   # at the same time. You could use e.g. -arbalign <float> instead
   JKQC collectionXTB.pkl -unique rg,el,dip -out filteredXTB0.pkl
   
   #well this one will work for you only if your JKsend is set properly.
   # Nevertheless, the JKQC command will remove structures that reacted 
   # during XTB optimization (it does compare the non-hydrogen skelets),
   # then the 1000 electronic-energy lowest structures are saved for 
   # next calculation. (-noex = do not print example)
   JKQC filteredXTB0.pkl -reacted -sort el -select 1000 -noex -out filteredXTB.pkl -ePKL > TO_DO_DFT.dat
   
   #Run Gaussian SP calculation from the Result File TO_DO_DFT.dat. It 
   # does submit 8-cpu job for each line in that file. The jobs is always
   # an array, but now only 25 calculations will run at a time. The
   # maxtasks value says that we guarantee that no more than 1000 lines
   # is saved in the results file (prevents submitting to many jobs)
   JKCS3_run -p G16 -rf TO_DO_DFT.dat -nf DFT_SP -m "# wb97xd 6-31++g**" -time 2:00:00 -cpu 8 -maxtasks 1000 -arraymax 25
   
   #Again we collect the data
   JKCS4_collect DFT_SP -oc -time 1-00:00:00
   
   #Now we select only 100 lowest energies
   JKQC collectionDFT_SP.pkl -sort el -select 100 -noex -ePKL > runDFT.dat
   
   #and submit them again for Gaussian calculation
   JKCS3_run -p G16 -rf runDFT.dat -nf DFT_opt -m "# wb97xd 6-31++g** opt" -time 3-00:00:00 -cpu 8 -maxtasks 100 -arraymax 25
   
   #Again we collect the data
   JKCS4_collect DFT_opt -oc -time 1-00:00:00
   
   #We just prepare next calculation
   JKQC collectionDFT_opt.pkl -noex -ePKL > runDFTO.dat
   
   #Now we calculate vibrational frequencies. Theoretically, you could 
   # combine it with the previous step but this is very practical as
   # some of the optimization do not finish do to presence of shallow minima
   JKCS3_run -p G16 -rf runDFTO.dat -nf DFT_freq -m "# wb97xd 6-31++g** freq" -time 1-00:00:00 -cpu 8 -maxtasks 10000 -arraymax 25
   
   #Again we collect the data
   JKCS4_collect DFT_freq -time 1-00:00:00 -oc
   
   #We filter out all data for which the lowest vibrational frequency 
   # is less than 0 (i.e. imaginary). Then we select 5 lowest Gibbs free
   # energy structure after we correct for the low vibrational frequencies
   # with threshold of 100 cm-1
   JKQC collectionDFT_freq.pkl -pass lf 0 -sort g -fc 100 -v 0.996 -select 5 -noex -ePKL > runDLPNO.dat
   
   #Now we submit ORCA calculation. We add an extra memory
   JKCS3_run -p ORCA -rf runDLPNO.dat -nf DLPNO -m "! aug-cc-pVTZ aug-cc-pVTZ/C cc-pVTZ-F12-CABS DLPNO-CCSD(T) TightSCF" -time 2-00:00:00 -cpu 8 -mem 20gb
   
   #Again we collect the data
   JKCS4_collect DLPNO -time 1-00:00:00 -orca -oc

Large clusters
--------------

This is what we (H. Wu and G. Hasan) typically use for large clusters (freshly-nucleated particles) where only one conformer combination (ionic) is used. 

.. code:: bash

   #Detail protocol is available here: https://doi.org/10.1021/acsomega.3c06794
   #ABCluster
   JKCS2_explore -pop 1280 -gen 320 -repeat 10 -sc 4 -lm 1000 -expl -cpu 8
   JKCS4_collect ABC -oc

   #XTB calculation
   JKCS3_run -p XTB -rf collectionABC.pkl -nf XTBopt -m "--opt --gfn 1" -maxtasks 1000 -cpu 2 -tpj 10 -mf 1000 -time 10:00:00 -arraymax 400
   JKCS4_collect XTBopt -oc
   JKQC collectionXTBopt.pkl -uniq rg,el,dip -out collectionXTBopt_filtered.pkl #-reacted (optional)

   #DFT single point calculation 
   JKCS3_run -p ORCA -rf collectionXTBopt_filtered.pkl -nf B97-3Csp -m "! b97-3c TightSCF" -time 1-00:00:00 -maxtasks 1000 -cpu 2 -tpj 10 -mf 1000 -mem 8GB -arraymax 400
   JKCS4_collect B97-3Csp -orca -oc
   JKQC collectionB97-3Csp.pkl -sort el -select 1000 -out collectionB97-3Csp_filtered.pkl

   #DFT Partial Geometry Optimization
   JKCS3_run -p ORCA -rf collectionB97-3Csp_filtered.pkl -nf B97-3Cpartopt -m "! b97-3c opt TightSCF" -time 12:00:00 -maxtasks 1000 -cpu 2 -mem 8GB -arraymax 150 -add maxiter 40
   JKCS4_collect B97-3Cpartopt -orca -oc
   JKQC collectionB97-3Cpartopt.pkl -unique rg,el,dip -sort el -select 100 -out collectionB97-3Cpartopt_filtered.pkl

   #DFT Full Geometry Optimization and vib. frequency calculation
   JKCS3_run -p ORCA -rf collectionB97-3Cpartopt_filtered.pkl -nf B97-3Coptfreq -m "! b97-3c opt TightSCF Anfreq" -time 12:00:00 -maxtasks 100 -cpu 8 -mem 12GB
   JKCS4_collect B97-3Coptfreq -orca -oc -loc

Enhanced exploration for organic clusters
-----------------------------------------

This is what Jakko Kahara uses for organic dimers (trimers...), which first tries to provide more reasonable structures to CREST by arranging some functional groups together

.. code:: bash

   JKCS2_explore -constraints "-nfiles 5000" -gen 5 -box 2 -exploded
   JKCS3_run -p XTB -rf ABC_XTB -nf XTB -m "--gfn 1 --opt tight" -par small -time 72:00:00 -tpj 1000 -maxtasks 10
   JKQC collectionXTB.pkl -ePKL -rg -el -sort el -cutr 15 -select 1000 -uniq -noex > resultsXTB.dat

   # First SP DFT
   JKCS3_run -rf XTB -nf DFT0 -m "# B97D3 Def2SVPP DensityFit pop=mkuff" -par small -time 72:00:00 -maxtasks 100 -tpj 100 -p G16
   JKQC collectionDFT0.pkl -ePKL -rg -el -sort el -cutr el 8 -select 100 -noex > resultsDFT0.dat

   # superfast CREST with reduced settings
   JKCS3_run -p CREST -rf DFT0 -nf CREST -m "--gfn1 --nci --len x0.1 --wscal 0.6 --mquick" -par small -time 72:00:00 -tpj 10
   JKQC collectionCREST.pkl -ePKL -rg -el -sort el -cutr 15 -select 1000 -uniq -noex > resultsCREST.dat

   # Second SP DFT
   JKCS3_run -rf CREST -nf DFTCREST -m "# B97D3 Def2SVPP DensityFit pop=mkuff" -par small -time 72:00:00 -maxtasks 100 -tpj 100 -p G16
   JKQC collectionDFTCREST.pkl collectionDFT0.pkl -ePKL -rg -el -sort el -cutr el 8 -uniq -select 100 -noex -out todo.pkl > resultsTODO.dat

   JKCS3_run -p G16 -rf TODO -nf DFT -m "# B97D3 Def2SVPP DensityFit opt=(loose,MaxCycle=250) pop=mkuff" -par small -time 72:00:00 -maxtasks 100 -tpj 10
   JKQC -folder DFT -R -forces -out collectionDFT.pkl -noex -ePKL -rg -el -sort el -uniq rg,el,dip > resultsDFT.dat

   JKCS3_run -p G16 -rf TODO -nf FREQ -m "# B97D3 Def2SVPP DensityFit opt=(tight,MaxCycle=250) freq pop=mkuff" -par small -time 72:00:00 -maxtasks 100 -tpj 10
   JKQC collectionFREQ.pkl -ePKL -rg -el -g -sort g > resultsFREQ.dat
   # reoptimize the best results at some higher level

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
   
