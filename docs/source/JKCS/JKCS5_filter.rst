============
JKCS5_filter
============

.. note:: 

   Please, be aware, that JKCS5_filter script is available only due to historical development of JKCS. Currently, JKCS4_collect is coupled with JKQC and all filtering and structure processing is done via JKQC. Nevertheless, I will still keep the old JKCS5_filter script available.

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
      
Uniqueness
----------

Uniqueness filtering removes structures that are too similar to other structures. When calling
JKCS4_collect, a uniqueness filter is automatically applied on ``collectionXXX.txt`` and the results are stored in ``resultsXXX.dat``. 
This filter assumes two structures with energy difference less than 0.001 hartree and gyration radius (Rg) difference less than 0.01 Å to be the same. 
Users can run the JKCS5_filter uniqueness filter to fine-tune these uniqueness thresholds. 
Otherwise, users do not have to bother with uniqueness.

Outliers
--------

Outlier filtering removes structures that have properties too far away from that of the current lowest
energy structure. This operation takes as an argument the threshold for specific properties above
which a structure is considered an outlier. This filter uses both relative and absolute thresholds for
the el. energy. We could ask for a rel. el. energy threshold (e.g., ‘-d 3.5’). Any structure that has
an el. energy more than 3.5 kcal/mol higher than the lowest energy structure will be removed. Or
we could define an abs. el. energy threshold ‘-en’ (e.g., ‘-en 100’), and structures with energy higher than -100 Hartree will be removed. For the gyration radius, only absolute thresholds can be applied (e.g., ‘-rg 6’) removes all structures with gyration radius higher than 6 Å.

Selection
---------

Sampling (or selection) uniformly (covering PES uniformly) picks a specified number of structures
from the ``resultsXXX.dat`` file after applying outlier filtering. This is useful when there are too many
structures left for calculations on a higher level of theory. Hence, to reach a reasonable computational cost, we take only very different conformers. As sampling omits some minima, it might result in losing the global minimum structure, but due to the uniform sampling, the global minimum should not be far from one of the other selected minima.

These three filter operations can also be combined. You can thus call JKCS5_filter to apply an
uniqueness and outlier filter on a resultsXXX.dat file and then uniformly pick a sample of the remaining structures.
