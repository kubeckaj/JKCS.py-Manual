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
      
You can run a test of a sort simulation (gen = 5) with very small population (pop = 5) on local (or login) computer. Save a few lowest minima (lm 3) and examine the subfolders. Example code:

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

For proper configurational sampling, you should not run simulations shorter than 100 generations. Use also adeqate size of population and save enough 
of local minima. Remember that configurational spaces increases with cluster size, and thus you should use greater parameters for larger clusters.

.. code:: 

   JKCS2_explore -gen 200 -pop 1000 -lm 3000
   JKCS2_explore -gen 100 -pop 300*M -lm 3000/NoC
   

