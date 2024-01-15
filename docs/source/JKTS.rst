============================================
About & Usage
============================================

.. contents:: Table of Contents
   :depth: 2

Introduction
============

``JKTS`` is a tool designed to facilitate a streamlined and automatic process of generating and monitoring files integral for transition state search in atmospheric chemistry, through the use of quantum chemical programs ORCA and Gaussian16.
It implements the multiconformer transition state theory (MC-TST) to achieve realistic understanding and prediction of the kinetics in atmospheric chemical reactions between organic species and oxidants in the atmosphere. Currently, ``JKTS`` supports the  reaction of hydrogen abstraction by OH radical and OH radical addition to carbon-carbon double bonds. 
Furthermore, tunneling effects are accounted for using the Eckart tunneling correction factor, by fitting a unsymmetrical Eckart potential to the reactant complex, transition state, and product complex energies. In the case of reactions involving ligjt atoms, such as hydrogen, the tunneling correction has shown to be crucial.

When setting up JKTS, you should use :guilabel:`-TS` in order to install, e.g.:
   
.. code:: bash
   
      sh setup.sh -r grendel -TS

Workflow Overview
=================

The JKTS tool processes transition state molecules and reactants/products using distinct workflows:

Transition State Molecules Workflow
-----------------------------------

#. Conformer sampling with CREST.
#. Constrained optimization of the conformers.
#. Transition state optimization.
#. Final energy refinement with DLPNO-CCSD(T) calculations.

Reactants and Products Workflow
-------------------------------

#. Conformer sampling with CREST.
#. Geometry optimization of the conformers.
#. Final energy refinement with DLPNO-CCSD(T) calculations.

.. note::
   Insert a workflow diagram here.

Using JKTS
==========

JKTS can be configured with various options for different computational scenarios. As an example, to calculate the reaction dynamics of hydrogen abstraction from methane with the OH radical, use the following command:

.. code-block:: bash

    JKTS CH4.xyz -OH

This command will create three directories: **products**, **reactants**, and **CH4_H1**.

- The **products** directory includes the H2O molecule and configurations of products from hydrogen abstraction. For methane, there is only one product type since all hydrogens are equivalent.
- The **CH4_H1** directory is for the case of single hydrogen abstraction from methane. THe JKTS program tries to treat chemically equivalent hydrogens. A rather simple but efficient approach is used by storing the indexes of carbons with three (or more) hydrogens bonded to it during the generation of the initial guess for the TS state. These are assumed to correspond to the molecules methyl groups and that these hydrogens are chemically equivalent. This assumption is justified based on the initial use of the CREST program for the conformer sampling and therefore the subsequent sampling of the methyl groups.
- The **reactants** directory contains the methane molecule and the OH radical, following the workflow for reactants.

Adjusting Monitoring Time and Restarting Jobs
---------------------------------------------

For tasks that are not computationally intensive, such as the transition state search for methane, the monitoring duration can be tailored with the ``-time`` argument. To set the monitoring time to five hours, input the following:

.. code-block:: bash

    JKTS CH4.xyz -OH -time 5:00:00

If the monitoring were to end prematurely, for instance during constrained geometry optimization, the calculations are able to be restarted with the command:

.. code-block:: bash

    JKTS *.log

The wildcard symbol (*) matches all `.log` files in the directory. Logs from completed tasks are moved to **CH4_H1/log_files**, so running the command within **CH4_H1** targets only the `.log` files of incomplete tasks. JKTS will assess each `.log` file to determine the last completed step and will resume the workflow accordingly.

If we simply wanted to perform only constrained optimization without moving on to the transition state search, the `-auto false` option is available:

.. code-block:: bash

    JKTS *.log -auto false
    
    
Advanced Usage
--------------

To run JKTS with specific settings, like a custom level of theory:

.. code-block:: bash

    JKTS yourfile.xyz -OH --low_level "B97-3c" --high_level "B3LYP 6-31++g(d,p)"
    
Keep in mind the natural limitation of ORCA and Gaussian16 in relation to the basis set and method. Although ORCA supports most of the well-known methods and basis sets...

Monitoring of log files
~~~~~~~~~~~~~~~~~~~~~~~~~    

JKTS monitors the log file with certain intervals to avoid overwhelming communication between computers. By default the program allows this communication a `100` times with a certain time interval between each check determined by ``interval``. By default the time between checks is calculated based on the size of the input molecule. However, the maximum number of attempts to check the log files and the interval between them can be modified as:

.. code-block:: bash

    JKTS yourfile.xyz -OH -interval 500 -attempts 200 -initial_delay 2000
    
Resulting in an initial delay of 2000 seconds before the log files are checked with 500 seconds interval between each check and this check is performed up to 200 times.


Command Line Arguments
======================

``JKTS`` accepts various arguments to control its behavior:

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Input Commands
     - Description
   * - ``-h``, ``--help``
     - Print help page
   * - ``-auto``
     - Enable automated processing of predefined workflow. See ``Workflow`` for more. [def = True]
   * - ``-OH``
     - Perform H abstraction with OH radical
   * - ``-CC``
     - Perform addition to C=C bonds
   * - ``-OH_CC``
     - Perform OH addition to C=C bonds
   * - ``-G16``
     - Gaussian16 is used for QC calculations (default)
   * - ``-ORCA``
     - ORCA is used for QC calculations
   * - ``-constrain``
     - Constrain is integrated into relevant input file [def = True]
   * - ``-reactants``
     - Prepare folder for reactants [def = True]
   * - ``-products``
     - Prepare folder for products [def = True]
   * - ``-NEB``
     - Prepare input file for Nudged Elastic Band [def = False]
   * - ``-k``
     - Calculate Multiconformer Transition State rate constant def = [True]
   * - ``--high_level``
     - Specify the high level of theory for QC method TS optimization [def = wB97X-D aug-cc-pVTZ]
   * - ``--low_level``
     - Specify the low level of theory for preoptimization [def = wB97X-D 6-31+G(d,p)]
   * - ``-cpu``
     - Number of CPUs [def = 4]
   * - ``-mem``
     - Amount of memory allocated for job [def = 8000mb]
   * - ``-par``
     - Partition to use [def = qany]
   * - ``-time``
     - Specify how long time the manager monitors [def = 144 Hours]
   * - ``-interval``
     - Set time interval between checks of log files [def = based on molecule size]
   * - ``-initial_delay``
     - Set an initial delay before checking log files [def = based on molecule size]
   * - ``-attempts``
     - Set how many times a log files should be checked [def = 100]
   * - ``-max_conformers``
     - Set max number of conformers from CREST [def = 50]
   * - ``-freq_cutoff``
     - Set cutoff for TS imaginary frequency to [int] cm^-1 [def = -200]
   * - ``-reaction_angle``
     - Set the angle of the active site of transition state to [int] degrees [def = 175.0]
   * - ``-ewin``
     - Set energy threshold to [int] kcal/mol for CREST conformer sampling [def = 8]
   * - ``-info``
     - Print information of molecules in log files or .pkl file
   * - ``-XQC``, ``-YQC``, ``-QC``
     - (G16 only) Use specified SCF algortihm instead of Direct Inversion of Iterative Space (DIIS)
