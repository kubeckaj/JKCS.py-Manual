====================
About & Installation
====================

What is JKQC?
-------------

Here, we introduce Jammy Key for Quantum Chemistry (JKQC) databases of molecular clusters.

These scripts converts the QC output files (.log,.out,.xyz) into a database (.pkl), which takes significantly less memory and accelerates the data post-processing (e.g., printing energies, including various corrections, and calculation formation properties for ACDC). Depending on the files sizes/cluster sizes/types, the pikling takes approximately from 15 seconds/1000 structures to 3 minutes/1000 structures. Nevertheless, the post-processing usually takes from -immidiately- to a few seconds. (Sorry, JKQC is not parralelizable (at least yet).)

Installation
------------

You can download JKQC from https://github.com/kubeckaj/JKQC.git

.. code:: bash

   git clone https://github.com/kubeckaj/JKQC.git
   cd JKQC
   vim install.sh #modify all necessary
   sh install.sh
   JKpython
   python JKQCpickle.py -help

However, if you are using JKCS, then it already contains JKQC in JKCS subfolders. You can use it in various ways.
The fastest evaluation is calling directly JKQCpickle:

.. code:: bash

   JKpython
   python FULLPATHTOJKCS/JKCS2.1/JKQC/JKQCpickle.py -help

However, simpler is calling:

.. code:: bash

   JKgaussstat -help
  
or

.. code:: bash

   JKQCpickle -help
   
or

.. code:: bash

   source ~/.JKCSusersetup.txt
   program_JKQCpickle -help

Finally, when using JKCS4_collect, you can use pickle as well (see more details in JKCS4_collect section):

.. code:: bash

   JKCS4_collect DFT_opt -JKQC
   JKCS4_collect DFT_opt -JKQCclean
   JKCS4_collect DFT_opt -JKQCcleanfull

File names
----------

These are strong recomendations for you file names:

.. list-table:: Nomenclature for molecules
    :widths: 30 30 30
    :header-rows: 1

    * - neutral
      - positive
      - negative
    * - 1sa = sulfuric acid
      - 
      - 1b = bisulphate
    * - 1msa = methanesulfonic acid
      - 
      - 1mb = methanebisulphate
    * - 1nta = nitric acid
      - 
      - 1nt = nitrate
    * - 1am = ammonia
      - 1am1p = ammonium
      -
    * - 1ma = methyammine
      - 1ma1p = methylammonium
      - 
    * - 1dma = dimethylamine
      - 1dma1p = dimethylammonium
      -
    * - 1tma = trimethylamine
      - 1tma1p = trimethylammonium
      -
    * - 1eda = ethylamine
      - 1eda1p = ethylammonium
      - 
    * - 1gd = guanidine
      - 1gd1p = guanidium
      -
    * - 1w = water
      - 1w1p = hydronium
      - 1oh = hydroxide

Any addtional comments can be separated by a dash: e.g. 1sa1am-123.log or 1as2dma-1_Ik_solid.log
In case of any troubles with naming, use -nonmame argument:

.. code::

   JKQCpickle *.log -noname -out mydatabase.pkl



