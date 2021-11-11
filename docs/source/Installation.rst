   
|Build Status| |pypi| |doi| |Beta|

Installation
============
.. toctree::

   JKCS
   XTB

JKCS
----

XTB
---

The Linux version can be obtained from https://www.chemie.uni-bonn.de/pctc/mulliken-center/software/xtb/xtb
When using the XTB program, either use the full path directory to the excecutables or put the following lines to your ``~/.bashrc`` file:

.. code::

   export PATH=[-XTB-folder-path-]/bin:$PATH #e.g.: "/user/kubeckaj/XTB6.4/bin"
   export XTBHOME=[-XTB-folder-path-]        #e.g.: "/user/kubeckaj/XTB6.4"

and modify the following line in the ``~/.JKCSusersetup.txt``:

.. code::

   PATH_XTB="[-XTB-folder-path-]"            #e.g.: "/user/kubeckaj/XTB6.4" 
