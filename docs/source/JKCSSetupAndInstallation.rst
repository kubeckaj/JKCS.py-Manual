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
   sh setup.sh
   
.. hint::
 
   Users of some clusters (Puhti,Mahti,Grendel) can use predefined paths and python modules by typing:
   
   .. code:: bash
   
      sh setup.sh         #for Puhti users
      sh setup.sh grendel #for Grendel users
      sh setup.sh mahti   #for Mahti users
      
.. note::

   If you need to resetup the JKCS use the :guilabel:`-r` argument, e.g.:
   
   .. code:: bash
   
      sh setup.sh -r grendel
      
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
   
For more details see the other sections of this manual.

XTB
---

The Linux version can be obtained from https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/xtb/xtb
When using the XTB program, either use the full path directory to the excecutables or put the following lines to your ``~/.bashrc`` file:

.. code:: bash

   export PATH=[-XTB-folder-path-]/bin:$PATH #e.g.: "/user/kubeckaj/XTB6.4/bin"
   export XTBHOME=[-XTB-folder-path-]        #e.g.: "/user/kubeckaj/XTB6.4"

and modify the following line in the ``~/.JKCSusersetup.txt``:

.. code:: bash

   PATH_XTB="[-XTB-folder-path-]"            #e.g.: "/user/kubeckaj/XTB6.4" 


How to setup Jupyter
--------------------

Activate JKCS-python environment for Jupyter

.. code-block:: console

   (.venv) $ pip install --user ipykernel
   (.venv) $ python -m ipykernel install --user --name=jkcs
