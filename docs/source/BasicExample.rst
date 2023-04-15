=============
Basic example
=============

When test is completed you go to a working directory and start your first configurational sampling test, e.g.:

.. code:: bash

   cd <working-dir>
   JKCS0_copy sa w
   JKCS1_prepare sa w
   JKCS2_explore -pop 5 -gen 5 -lm 3 -loc
   JKCS4_collect ABC
   cd SYS_1sa_1w
   cat resultsABC.dat
   molden movieABC.xyz
   
For more details see the other sections of JKCS manual.
For help with individual programs continue reading on this page.
