============
JKCS5_filter
============

JKCS5_filter provides different methods to filter the large number of structures in
the configurational sampling. As input, JKCS5_filter takes ``collectionXXX.txt`` or ``resultsXXX.dat`` (unless otherwise specified) created by
JKCS4_collect. After the filtering has been applied, the remaining structures are written into ``resultsXXX_FILTERED.dat``. 
We distinguish different filtering operations:

*  Uniqueness filtering (produces only unique structures)
*  Filtering of failures (removing for instance reacted or exploded structures)
*  Threshold filtering (removes structures which for instance has values greater then specified value)
*  Sampling/selection (even when many structures remains, only several are uniformly selected so that they maximally represent the remaining set)

.. hint::

   For help use:

   .. code::
   
      JKCS5_filter -help
      
Uniqueness filtering
--------------------

Uniqueness filtering removes structures that are too similar to other structures. When calling
JKCS4_collect, a uniqueness filter is automatically applied on ``collectionXXX.txt`` and the results are stored in ``resultsXXX.dat``. 
This filter assumes two structures with energy difference less than 0.001 hartree and gyration radius (Rg) difference less than 0.01 Angstrom to be the same. 
Users can run the JKCS5_filter uniqueness filter to fine-tune these uniqueness thresholds. 
Otherwise, users do not have to bother with uniqueness.

