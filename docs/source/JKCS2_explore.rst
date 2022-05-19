=============
JKCS2_explore
=============

JKCS2_explore employs ABCluster (http://www.zhjun-sci.com/software-abcluster-download.php) to search for the global and local minima of 
clusters. ABCluster implements the Artificial Bee Colony (ABC) algorithm which was first proposed by Karaboga in 2008.
For every cluster combination, the ABCluster program creates a specified number of guess structures (pop = population) by adding the monomers 
of that cluster combination together at random orientations with respect to each other. The structures are optimized and evaluated using 
predefined energy potentials. Further, each new structure is formed by using weighted information 
of several structures combined (+ it is again optimized). Therefore, the population evolves as the new structures replace the old ones. 
This evolution run for a specified number of steps (gen = generations). If the potential energy of a specific guess structure does not change for more than 
a specified number of steps (sc = scout bee), the structure is replaced by a new random guess structure. This ensures that the algorithm does not get stuck 
in any local minimum for too long. At the end of all the optimization/generation steps, you can decide how many lowest minima are saved printed out (lm = local minima).

.. hint::

   For help use:
   
   .. code:: bash
   
      JKCS2_explore -help
      
You can run a test of a sort simulation (gen = 5) with a very small population (pop = 5) on local (or login) computer. Save a few lowest minima (lm 3) and examine the subfolders. Example code:

.. code:: 

   cd SYS_1sa_1am
   JKCS2_explore -gen 5 -pop 5 -lm 3 -loc
   cd ABC
   ls
   cd ABC_1_0_0_0_1_0
   ls
   vim calc.out
   cd calc-LM
   ls
   molden 1sa1am-100010_1_1.xyz

You should not run simulations shorter than 100 generations for proper configurational sampling. Remember that configurational spaces increase with cluster size, and thus you should use greater parameters for larger clusters. Use also adequate size of population and save enough 
of local minima.

.. code:: 

   JKCS2_explore -gen 200 -pop 1000 -lm 3000
   JKCS2_explore -gen 100 -pop 300*M -lm 3000/NoC
   
.. note::

   You can use variables "NoC" and "M" to define the parameter as a function of "Number Of (monomer) Combinations" or "(total) number of Molecules".

.. hint::

   Some variables are by default defined as functions of the ‘number of Molecules’ (M) and the ‘Number of Combinations’ (NoC). This is particularly useful when working with several clusters. Smaller cluster do not need such extensive exploration as larger clusters. M and NoC allow for the scaling of the exploration according to the cluster size and complexity. You can use these symbols as well to define arguments.
   
   It is important to note that when a lot of conformers are taken into account for a certain monomer, NoC can become very large. As a result, M/NoC becomes very small. Therefore, always be mindful of the result that using M and NoC might have for the exploration of all your studied systems. When dealing with large NoC, we believe that better performance of configurational sampling is reached when doing a small exploration on all combinations, rather than an exhaustive exploration of only a few selected combinations.
   
Arguments
---------

:guilabel:`-JKQC`
    after the run, the structures are pickled into a single file (``database.pkl``, see JKQC for more details). This saves memory and significantly reduces number of files. The subsequent commands should then use the -JKQC command as well. Example:
    
.. code:: 

   JKCS2_explore -gen 200 -pop 1000 -lm 3000 -JKQC
   JKCS3_run -JKQC
   JKCS4_collect XTB

:guilabel:`-pop, -i, -init <integer>`
    population size (or also number of initial guesses). The size of the colony that evolves over generations. [default = 300*M]
    
:guilabel:`-g, -gen <integer>`
    number of (ABC) generations (loops). [default = 100]
    
:guilabel:`-l, -lm <integer>`
    (maximal) number of the lowest local minima to be saved. [default = 300*M/NoC]
    
:guilabel:`-s, -sc <integer>`
    lifetime = maximum generations, i.e. number of loops before replacing unchanged structure. The best is to keep this parameter as 2-5. [default = 4]
    
:guilabel:`-box <float|integer>`
    simulation box size. When you use small or large (compared to sulfuric acid) molecules, you should modify the box size otherwise the resultant clusters could contain evaporated molecules or the configuration exploration would not be thourough enough. [default = 7+M]

:guilabel:`-repeat <integer>`
    each simulation is repeated (in parallel) X-times

.. code:: 

   JKCS2_explore -gen 200 -pop 300 -lm 1000 -sc 3 -box 2+M
   
The coupling between ABC and XTB
--------------------------------

This method is usefull for running flexible molecules. Note that in `input.txt` you should point to pure xyz (not the abc-xyz). You can create example input file also with JKCS0_copy

.. code:: 
   
   JKCS0_copy -helpxyz
   JKCS0_copy XYZna XYZbuoh
   <modify input.txt>
   JKCS1_prepare
   
Ok, time to run JKCS2_explore with the ABC_XTB coupling:

.. code::

   JKCS2_explore -helpxtb
   JKCS2_explore -abcxtb -gen 2000 -repeat 2 -cpu 8
   
ABC_XTB arguments
-----------------

:guilabel:`-abcxtb`
    switch to the ABC_XTB version

:guilabel:`-g, -gen <integer>`
    number of (ABC) generations (loops). [default = 100] (i.e. number XTB runs)
    
:guilabel:`-box <float|integer>`
    simulation box size from -X to X. When you use small or large (compared to sulfuric acid) molecules, you should modify the box size otherwise the resultant clusters could contain evaporated molecules or the configuration exploration would not be thourough enough. [default = 7+M]
    
:guilabel:`-repeat <integer>`
    each simulation is repeated (in parallel) X-times
    
:guilabel:`-gfn <integer>`
    defines GFN1-xTB or GFN2-xTB [def=1]
