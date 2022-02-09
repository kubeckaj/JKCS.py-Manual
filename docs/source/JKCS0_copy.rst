==========
JKCS0_copy
==========

JKCS0_copy automatically creates ``input.txt`` based on the monomers given as arguments.
JKCS contains optimized structures for the different conformers and conjugated acids/bases of some
of the most prominent monomers in atmospheric clusters (such as sa = sulfuric acid, am = ammonia, na = nitric acid
or w = water). Calling JKCS0_copy creates ``input.txt`` containing the paths to the optimized structures of the conformers and conjugated
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
 
   If your structure is not available in JKCS database, you have to create the ABCluster input by yourself. See ABCluster manual for more details.

.. code:: 

   w ............ water (H2O,OH-,H+)         cd .......... carbon dioxide (CO2)
   aq ........... water (H20)                m ........... methane (CH4)
                                             ar .......... argone (Ar)
   nta .......... nitric acid (HNO3)         ne .......... neone (Ne)
   sa ........... sulfuric acid (H2SO4)      he ........... helium
   msa .......... methanesulfonic acid
                                             h ............ proton (H+)
   am ........... ammonia (NH3)              na ........... sodium (Na+)
   gd ........... guanidine (CN3H5)          cl ........... chloride (Cl-)
   dma .......... dimethylamine (C2H7N)
   tma .......... trimethylamine (C3H9N)     ica ......... iodic acid (HIO3)
   urea ......... urea (CH4N2O)              isa ......... iodous acid (HIO2)
   buoh ......... butanol (C2H5OH)           ip .......... iodine pentoxide (I2O5)
    
EXAMPLE: Consider an example of a negatively charged cluster containing 1 ammonia and 2 sulfuric acid molecules. Type "JKCS0_copy sa am" to creat ``input.txt``. ``input.txt`` will already contain the information of cis- and trans-sulfuric acid, bisulfate, sulfate, ammonia and ammonium in the "structure of building monomers" section. The total charge and composition will however not be the same as our desired cluster. We will thus have to change the total charge to -1 and the composition to "2_1". 

If we would have called "JKCS0_copy A SA", ammonia and ammonium would first be mentioned in
the "structure of building monomers" section followed by the sulfuric acid monomers and conjugated
bases. In this case, we should write the composition as "1_2" to obtain our desired cluster.
