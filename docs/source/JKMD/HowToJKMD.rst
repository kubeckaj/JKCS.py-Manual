============================================
About & Usage
============================================

.. contents:: Table of Contents
   :depth: 2

Installing JKMD
===============

You just need some Python libraries that is also required by JKQC and the Python calculators such as XTB, TBlite, ORCA. Hence, if you during setup of the JKCS did not use :guilabel:`-calculators` or :guilabel:`-all`, you must update (:guilabel:`-up`) those:

.. code-block:: bash

   cd JKCS2.1
   sh setup.sh -up -calculators

.. hint::
   
   If you are doing your first setup, you are not only setting up JKCS and installing Python libraries. Using :guilabel:`-all` libraries might be quite heavy, so try to specify just what do you want to use and eventually add your group name if I predefined some paths for you:
 
  .. code-block:: bash

     sh setup.sh -calculators grendel

.. note::	

   For ORCA, you also need the ORCA excecutables. Thus setup properly MODULE_ORCA and PATH_ORCA in the `~/.JKCSusersetup.txt` file.  

Introduction
============

JKMD use ASE to generater MD simulations. It is a submitable script, so unless you use argument :guilabel:`-loc` it is going to be submitted via SLURM to the cluster. 

JKMD has its own help, so always try to follow that one:

.. code-block:: bash

   JKMD -help

The in which arguments follow are important here. There several categories to setup:
- The system, specie by specie and their properties and constraints
- The simulation and thermostat setup
- The :guilabel:`-follow` argument to separate two subsequent simulations
- The -loc argument or cluster submission arguments 

.. note::

   The simulation are performed in the SIM<int> folder unless you specified the folder name by :guilabel:`-nf`. 

Setting up the system
=====================

I will just present several examples, where I will calcualte only SP calculation (-ns 0) using the default XTB calculator:

.. code-block:: bash

   #Loading XYZ structure
   JKMD str.xyz -ns 0 -loc 

   #Loading last structure from pickle file
   JKMD strs.pkl -ns 0 -loc

   #Loading the 10th structure from pickle file (Python counts from 0)
   JKMD -index 9 strs.pkl -ns 0 -loc

   Loading the 10th structure and last structure while shifting them in space
   JKMD -index 9 strs.pkl -recenter strs.pkl -moveto [10,0,0] -ns 0 -loc

   #The same but setting initial velocity to the second structure
   JKMD -index 9 strs.pkl -recenter strs.pkl -moveto [10,0,0] -vel [-1,0,0] -ns 0 -loc

   #Setting app charge (total charge is what matters in QC)
   JKMD -index 9 strs.pkl -recenter strs.pkl -moveto [10,0,0] -chrg -1 -ns 0 -loc

   #Initiating velocities from Maxwell Boltzmann distribution but removing translation
   JKMD str.xyz -mb 300 -setvel 0 -ns 0 -loc

   #Placing an external force field to prevent cluster from evaporating
   JKMD cluster.xyz -recenter -EF_h_A 10 -ns 0 -loc

Setting up the simulation
=========================

Unless you use Velocity Verlet algorithm (:guilabel:`-vv`), you can run NVT with thermostat like Langevin, CSVR, and Nóse-Hoover. These use some constant of coupling. For instance, the CSVR constant of 25 fs can indeed bring some systems in 25 fs to equilibrium but for other systems you must you stronger coupling to achieve the same goal. At the same time you should define other simulation parameters (:guilabel:`-ns`, :guilabel:`-dt`, :guilabel:`-dump`) and the calculator (:guilabel:`-xtb1`, :guilabel:`-xtb2`, :guilabel:`-orca`). Let us see few examples:

.. code-block:: bash

   #Using Langevin thermostat, storing data every 50 fs and running 10 ps overall.
   JKMD str.xyz -mb 300 -langevin 0.01 -dt 1 -ns 10000 -dump 50 -nf RUN -loc

   #Using temperature of 200 K and fixing the COM
   JKMD str.xyz -recenter -mb 300 -langevin 0.01 -dt 1 -ns 10000 -dump 50 -nf RUN -temp 200 -fix_COM -loc

   #Performing 3 separate simulations
   JKMD str.xyz -mb 300 -langevin 0.01 -dt 1 -ns 10000 -dump 50 -nf RUN -repeat 3 -par q40 -time 10:00:00

The -follow argument
====================

You can combine two simulations, typically equilibration and MD. You can run it like this:

.. code-block:: bash

   JKMD str1.xyz -mb 200 -langevin 0.01 -xtb2 -dump 0 -ns 10000 -follow -csvr 25 -dump 50 -ns 20000 -par q40 -time 20:00:00 -nf EQ-RUN

The cluster submission
======================

You can also submit the job to the cluster. In that case the argument :guilabel:`-loc` is not necessary. The job will be submitted to the cluster and will be executed there. See the `Cluster submission <https://jkcs.readthedocs.io/en/latest/JK/ClusterSubmission.html>`_ for more details. 

In the case of the :guilabel:`-repeat` argument, an array of jobs will be submitted. You can also use "--" to express a range of variables. For instance:

.. code-block:: bash

   #Running 11 different temperatures (not 281) each 3 times
   JKMD str.xyz -temp 270--281 -langeving 0.01 -par q40 -time 10:00:00 -repeat 3 

   #Testing how the thermostat coupling affects the equilibration
   JKMD str.xyz -langevin 0.005--0.005--0.025 -par q40 -time 10:00:00

This is btw used also in the `Umbrella sampling <https://jkcs.readthedocs.io/en/latest/JKMD/UmbrellaSampling.html>`_
 




