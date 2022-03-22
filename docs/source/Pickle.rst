====================
Pickle
====================

When you need to pickle some JKCS subfolders, use JKCS4_collect command with -JKCS argument

.. code:: bash

   JKCS4_collect DFT_opt -JKQC
   JKCS4_collect DFT_opt -JKQCclean       #removes unnecessary files
   JKCS4_collect DFT_opt -JKQCcleanfull   #removes DFT_opt folder afterwards
   
.. note:
  
    Once you use JKCS4_collect -JKQC, a pickled file is also created in the subfolders. If you want to recollect data completely again, removes those pickled files:
    
    .. code: bash
    
       rm DFT_opt/*/*.pkl
       JKCS4_collect DFT_opt -JKQC
       
Collect data from .log (and .xyz, .out) files and pickle them into a database:

.. code:: bash
   
   python JKQCpickle.py *.log -out local_database.pkl
   
Add data into database:

.. code:: bash
   
   python JKQCpickle.py *.log -in local_database.pkl -out local_database.pkl
   
Connect two databases:

.. code:: bash
   
   python JKQCpickle.py -in database1.pkl -in database2.pkl -out joined_database.pkl
   python JKQCpickle.py database1.pkl database2.pkl -out joined_database.pkl
   
Extract part of a database 

.. code:: bash
   
   python JKQCpickle.py -in mydatabase.pkl -extract 1sa2w -out 1sa2w_database.pkl
