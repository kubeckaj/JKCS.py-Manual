===========================
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
 * communication with 3rd-party computational programs such as Gaussian, ORCA, ABCluster,
and XTB (and for advanced users: CREST, IMoS)
 * automated handling of jobs and submissions to (super)computer clusters
 * it is coupled with JKQC and the pickled file/structures databases can be easily forwarded to JKML for machine-learning purposes

Basic example
-------------

Let us do a simple test on our local/login computer. This test can also help you to verify that you did setup JKCS/JKQC correctly. Go to a working directory and start your first CS test, e.g.:

.. code:: bash

   cd <working-dir>
   JKCS0_copy sa w
   cat input.txt
   JKCS1_prepare sa w
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
