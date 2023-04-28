# JKQC Manipulation

.. hint::

   Use JKQC help to get idea what everything it can do:
   
   ..code:: bash
   
   JKQC -help
   
Generally, use JKQC in one of the following format:

.. code:: bash

   JKQC <File(s)> <Database(s)> <Options/Parameters>
   
However, I would first recommend to keep the file names in the below suggested format (automatically done within JKCS).

## File names

To get full funcitionality of JKQC, keep the file names in the follwing format:

.. code:: bash

   >> ls
   1sa.log 1am.log 2am3sa-1conf.log 2am3sa-2conf.log 2sa-12_23.log
   1sa.xyz 1am.xyz 2am3sa-1conf.xyz 2am3sa-2conf.xyz 2sa-12_23.xyz

This means that name has of formation of enumerated monomers composition and any addtional comments are separated by a hyphen.

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

.. hint::

   If you work with molecules and want to calculate, e.g., atomization energies, 
   use the following naming:
   
   .. code::
   
     >> ls
     1H.log 1C.log 3C8H.log 3C8H-stretched.log
     1H.xyz 1C.xyz 3C8H.xyz 3C8H-stretched.xyz
     
   Do not forget to use correct spin multiplicities, e.g.: H=2, C,O,S=3, N=4.
   
.. note::

   By defaul, it is assumed that structures are saved in ``*.xyz`` file, the Gaussian/XTB output is saved in ``*.log`` files, and ORCA outputs in ``*.out`` files. You can however modify that by, e.g.:
   
   .. code::
   
     JKQC -collect log -orcaext log -out collectedorca.pkl  

## Database manipulation

### Input
 
:guilabel:`<Files>`  
  
input files can be any .log, .out, and .xyz files. However, if you specify, e.g., ``*.log``, it will collect information from all files with the same name.

:guilabel:`database.pkl`
  loads ``database.pkl`` file. You can load several database into one 

.. list-table:: Input data
    :widths: 30 30
    :header-rows: 1
    
    * - Specified
      - Description
    * - NOTHING
      - takes in all .log files working in folder
    * - FILES
      - takes in all specified .log, .out, .xyz files
    * - DATABASES
      - takes in all specified (-in) .pkl databases
    * - COMBINED
      - FILES and DATABASES combined 

:guilabel:`--folder <PATH>`
  collects data from a given folder
  
:guilabel:`--collect <string>`
  collects data for 
  
### Output

:guilabel:`--out database.pkl`
  output ``database.pkl`` pickled file
  
.. list-table:: Output database
    :widths: 30 30
    :header-rows: 1
    
    * - Specified
      - Description
    * - NOTHING
      - in classified conditions: mydatabase.out
    * - DATABASE
      - saves all input data into -out specified .pkl database

You can print various properties (see the section below), e.g.:

.. code:: bash

  JKQC *.log -b -el    #[basename] [electronic_energy]

You can print various other files:

:guilabel:`-xyz`
  creates xyz files for all pickled files

:guilabel:`-movie`
  concatenate all xyz into ``movie.xyz``
  
:guilabel:`-imos_xlsx`
  Excell sheet input for IMoS
  
## Printing properties

See JKQC help ``JKQC -help`` for all various properties. For instance, you can print (name and) electronic energy from files/database:

.. code:: bash
   
   JKQC *.log -b -el        #[basename] [electronic_energy]
   JKQC database.pkl -b -el #significantly faster

## Processing
   
You can extract (name and) electronic energy for a specific cluster(s):

.. code:: bash
   
   JKQC in.pkl -extract 1sa2w -b -el
   JKQC in.pkl -extract 3sa,1sa0-10w -b -el

You sort your data with respect to el = electronic_energy/g = gibbs_free_energy

.. code:: bash

   JKQC in.pkl -sort el -b -el
   JKQC in.pkl -sort g -out out.pkl

Certainly utilize some filtering techniques (see JKQC help for greater detail):

 - Uniqueness: :guilabel:`-uniq rg,el` or :guilabel:`-arbalign 0.38` (CITE ArbAlign)
 - Low/High cutoff: :guilabel:`-pass lf 0` (removes structures with negative/imaginary frequencies), :guilabel:`-cut rg 10` (select structures with `Rg` less than 10 Angstrom), :guilabel:`-cutr el 10` (selects only 10 lowest kcal/mol structures)
 - Reacted: :guilabel:`-reacted` (compares all conformers and tries to remove some reacted/exploded structures) 

## Post-processing

This an example how to print binding free energies in kcal/mol while taking only the global free energy minimum

.. code:: bash
   
   JKQC clusters.pkl monomers.pkl -ct -g -glob -formation -unit -noex
   
and now with using treatment for low vibrational frequencies and anharmonity correction (CITE Grimme):

.. code:: bash
   
   JKQC clusters.pkl monomers.pkl -ct -g -glob -fc 100 -v 0.996 -formation -unit -noex
   
and now, assuming that the ``*.log`` files (Gaussian) were accompanied with ``*.out`` (ORCA) single-point corrections:

.. code:: bash
   
   JKQC clusters.pkl monomers.pkl -ct -gout -globout -fc 100 -v 0.996 -formation -unit -noex

and now, at different temperature:

.. code:: bash
   
   JKQC clusters.pkl monomers.pkl -ct -gout -globout -fc 100 -v 0.996 -formation -unit -noex -temp 270

