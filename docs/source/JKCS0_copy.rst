==========
JKCS0_copy
==========

JKCS0_copy automatically creates ``input.txt`` based on the monomers given as arguments.
JKCS contains optimized structures for the different conformers and conjugated acids/bases of some
of the most prominent monomers in atmospheric clusters (such as sa = sulfuric acid, am = ammonia, na = nitric acid
or w = water). When calling JKCS0_copy with the name of some monomers as arguments, an input.txt
file will be created containing the paths to the optimized structures of the conformers and conjugated
acids/bases of all the requested monomers in the "structure of building monomers" part of the file.

It is once again important to note that even when creating ``input.txt`` through JKCS0_copy,
it is likely that some parameters, like the composition, still need to be altered. JKCS0_copy will
write two example compositions for the chosen monomers. These of course do not necessarily have
to coincide with the desired cluster composition. Therefore, always check ``input.txt`` before
proceeding.

.. hint::

    For help use:
    
    .. code:: bash
    
       JKCS0_copy -help
       
Here are few examples:
 
.. code:: bash
 
   JKCS0_copy sa am       #creates input.txt with links to sulfuric acid and ammonia
   JKCS0_copy msa am dma  #creates input.txt with links to methansulfonic acid, ammonia, and dimethylamine
   JKCS0_copy -all        #created input.txt with links to all available structures
    
.. note::
 
   If your structure is not available in JKCS database, see the section: New ABCluster structures for more details
    
