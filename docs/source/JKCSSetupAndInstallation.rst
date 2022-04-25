====================
Setup & Installation
====================

JKCS
----

Clone the JKCS from github, (modify setup [see the hint below first]), and run ``setup.sh`` (this might take a while):

.. code:: bash

   git clone https://github.com/kubeckaj/JKCS2.1.git
   cd JKCS2.1
   #vim setup.sh
   sh setup.sh    #-qml  

.. note::
   
   :guilabel:`-qml` will install all libraries for quantum machine learning
   
.. hint::
 
   Users of some clusters (Puhti,Mahti,Grendel) can use predefined paths and python modules by typing:
   
   .. code:: bash
   
      sh setup.sh puhti   #for Puhti users
      sh setup.sh grendel #for Grendel users
      sh setup.sh mahti   #for Mahti users
      
.. note::

   If you need to resetup the JKCS use :guilabel:`-r` or :guilabel:`-r2`, e.g.:
   
   .. code:: bash
   
      sh setup.sh -r grendel   #reinstall python lins and rewrites ~/.JKCSusersetup.txt
      sh setup.sh -r2 grendel  #only rewrites ~/.JKCSusersetup.txt
      
If all paths are well setup in ``~/.JKCSusersetup.txt`` can be checked by:

.. code:: bash

   sh test.sh
   
If something fails, you must modify ``~/.JKCSusersetup.txt`` in order to use the JKCS feature.

When test is completed you go to a working directory and start your first configurational sampling test, e.g.:

.. code:: bash

   cd
   mkdir TEST
   cd TEST
   JKCS0_copy sa w
   JKCS1_prepare sa w
   JKCS2_explore -pop 5 -gen 5 -lm 3 -loc
   JKCS4_collect ABC
   cd SYS_1sa_1w
   cat resultsABC.dat
   molden movieABC.xyz
   
For more details see the other sections of JKCS manual.
For help with individual programs continue reading on this page.

ABCluster
---------

ABCluster can be obtained from http://www.zhjun-sci.com/software-abcluster-download.php
The online manual is available at http://www.zhjun-sci.com/abcluster/doc/ 
Modify the following lines in the ``~/.JKCSusersetup.txt``:

.. code:: bash

   PATH_ABC="[-ABCluster-folder-path-]"      #e.g.: "/users/kubeckaj/ABCluster-2.0-Linux/"
   MODULE_ABC="module load gcc"              #e.g.: "module load gcc/8.2.0" || "module load GCC/8.2.0-2.31.1"
   
If you want to use the ABCluster program by yourself, put the following lines to your ``~/.bashrc`` file:

.. code:: bash

   export PATH=$PATH:[-ABCluster-folder-path-]
   export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:[-ABCluster-folder-path-]
   
then you should be able to use ABCluster, e.g.:

.. code:: bash

   #source ~/.bashrc
   module load gcc
   bee
   ...

XTB
---

The Linux version can be obtained from https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/xtb/xtb
The online manual is available at https://xtb-docs.readthedocs.io/en/latest/contents.html
Modify the following line in the ``~/.JKCSusersetup.txt``:

.. code:: bash

   PATH_XTB="[-XTB-folder-path-]"            #e.g.: "/user/kubeckaj/XTB6.4" 
   
If you want to use the XTB program by yourself, either use the full path directory to the excecutables or put the following lines to your ``~/.bashrc`` file:

.. code:: bash

   export PATH=[-XTB-folder-path-]/bin:$PATH #e.g.: "/user/kubeckaj/XTB6.4/bin"
   export XTBHOME=[-XTB-folder-path-]        #e.g.: "/user/kubeckaj/XTB6.4"

then you should be able to run XTB, e.g.:

.. code:: bash

   #source ~/.bashrc
   xtb file.xyz --opt vtight 
   
Gaussian
--------

I hope that you know how to call gaussian jobs. If not ask a God person around you how to do it. 
Usually you load gaussian from a module, e.g.:

.. code:: bash

   module load gaussian
   
then you can figure out where is gaussian located, e.g.:

.. code:: bash

   $USER: > which g16
   /appl/soft/chem/gaussian/G16RevC.01_new/g16/g16
 
based on that modify the following lines in the ``~/.JKCSusersetup.txt``:
 
.. code:: bash

   PATH_G16="/appl/soft/chem/gaussian/G16RevC.01/"
   MODULE_G16="module load gaussian/G16RevC.01"    #"module load Gaussian"
   
If you want to run Gaussian by yourself, use some predefined scripts (something like ``subg16`` etc.)

How to setup Jupyter
--------------------

Activate JKCS-python environment for Jupyter

.. code-block:: console

   (.venv) $ pip install --user ipykernel
   (.venv) $ python -m ipykernel install --user --name=jkcs
