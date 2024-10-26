============================================
Equilibration
============================================

.. contents:: Table of Contents
   :depth: 2

Why
===

Equilibration is essential before running Molecular Dynamics (MD) simulations because it brings the system to a stable, realistic state, matching the desired temperature, pressure, and density. This step removes high-energy artifacts and prepares the system for accurate and reliable results by ensuring physically meaningful interactions and reproducibility. Skipping equilibration could lead to unphysical dynamics and inaccurate outcomes in the MD simulation.

How
===

If you run NVT simulation the goal is to equilibrate the slowest process in the system. In most cases it is the temperature but it could also be e.q. some structural behaviour of a large system if we are far from the equilibrium. We recommend using Langevin thermostat in the equilibration step as it equilibrate the vibrational, rotational, and translational temperatures faster than e.g. Nóse-Hoover or Berendsen thermosta. Otherwise, it is as simple as performing MD simulation:

.. code-block:: bash

   JKMD system.pkl -langevin 0.01 -dt 1 -ns 10000 -dump 0 -nf EQUILIBRATION -loc

This would perform equilibration on the local computer for tha last structure stored in system.pkl.
It will produce EQUILIBRATION folder with one equilibrated structures stored in the simcalc-LM.pkl. The log file from the simulation will be stored in EQUILIBRATION/calc-LM/output.

Verify
======	

If you want to be sure you have really equilibrate your system well, then it is worth monitoring the temperatuere on the way. It is quite simple just from grepping the results from the output file, where you are now interested in the T_[K] Tt[K] Tr[K] Tv[K] columns:

.. code-block:: bash

   grep JKMD: output | awk '{print $9, $10, $11, $12}' > temps.txt
   #module load gnuplot/5.4.3
   gnuplot <<< "set log x; p 'temps.txt' u 1 t 'T', '' u 2 t 'Tt', '' u 3 t 'Tr', '' u 4 t 'Tv'; pause 10"  

.. image:: equilibration.png
      :alt: filesstructure
      :width: 200
      :align: center


