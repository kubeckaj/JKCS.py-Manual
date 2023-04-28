=================
How to QML
==========

``JKML`` uses QML (https://www.qmlcode.org/index.html) for kernel ridge regression (KRR) applied on molecular representation (FCHL) to predict molecular system properties. 

.. note::

   When setting up JKCS, you should use :guilabel:`-qml` in orger to install QML, e.g.:
   
   .. code::
   
      sh setup.sh -r grendel -qml

I show examples for electronic energy but other molecular properties can be modelled, too. Training directly on electronic energy of a cluster 

.. math::
   E_{cluster}^{DFT}

is only alright if you train/test on its conformers (i.e. no large difference between modelled molecules are present).  

Otherwise, it is better to model, for instance, binding energies of the studied clusters

.. math::
   \Delta E^{DFT} = E_{cluster}^{DFT} - \sum E_{monomer}^{DFT},

or eventually atomization energies in the case of molecules.

Quite many studies showed that one can perform a cheaper but faster QC calculation (e.g., at XTB level) and then only model the small differences between high level and low theory (both calculated for the same structure geometries):

.. math::
   \Delta E^{DFT} = E_{cluster}^{DFT} - \sum E_{monomer}^{DFT}
.. math::
   \Delta E^{XTB} = E_{cluster}^{XTB} - \sum E_{monomer}^{XTB}
.. math::
   \Delta\Delta E^{DFT|XTB} = \Delta E^{DFT} - \Delta E^{XTB}

The delta-ML does perform significantly better and low level theory calculations are usually cheap to perform.

The structures should be provided in a pickled database.pkl file (see ``JKQCpickle`` manual). The file naming must have specific format (you can try, i.e. with caution, to use ``JKname`` to rename your files). See examples:

.. code::
   
   $USER: ls
   1sa.log 1w.log 1sa1w.log 1sa1w-1.log 1sa1w-2_32.log
   1sa.xyz 1w.xyz 1sa1w.xyz 1sa1w-1.xyz 1sa1w-2_32.xyz
   ....
   $USER: JKgaussstat *.log -out full_DFT.pkl

.. note::

   It is assumed that XTB and G16 outputs have extension `.log`. Generally, ORCA output is assumed to have `.out` extension that you can combine it as SP calculation with G16. However, for JKML, please change the extension to `.log` and use :guilabel:`-orcaext log` for ``JKgaussstat``, e.g.:
   
   .. code::
      
      JKgaussstat *.log -orcaext log -out full_DFT.pkl

.. hint::

   It is strongly recommended to separate monomers into a single file. Additionally, JKQCpickle (can be called by JKgaussstat command) can be used to prepare other pickled files, e.g.:
   
   .. code::
   
      JKgaussstat full_DFT.pkl -extract 1sa,1w    -out monomers_DFT.pkl 
      JKgaussstat full_DFT.pkl -extract 0-3sa0-5w -out train_DFT.pkl
      JKgaussstat full_DFT.pkl -extract 4sa0-5w   -out test_DFT.pkl 
      
``JKML`` is used similarly as other ``JKCS`` commands

.. code::

   JKML -help
   JKML -loc -method direct -train train_DFT.pkl -test test_DFT.pkl -monomers monomers_DFT.pkl
   JKML -par test -time 10:00 -mem 5GB -cpu 2 -method direct -train train_DFT.pkl -test test_DFT.pkl -monomers monomers_DFT.pkl 
   JKML -loc -print 2 -train train_DFT.pkl train_XTB.pkl -test test_DFT.pkl test_XTB.pkl -monomers monomers_DFT.pkl monomers_XTB.pkl

.. hint::

   See ``Cluster submission`` (under ``JKCS``) to understand how to tune cluster parameters.

.. note::
 
   You can first train and then test separately, e.g.:
   
   .. code::
   
      JKML -method direct -train train_DFT.pkl -loc
      JKML -method direct -trained vars.pkl -test test_DFT.pkl -monomers monomers_DFT.pkl -loc
      
The results can be found in output or in ``predicted_QML.pkl``, e.g.:

.. code::

   JKgaussstat predicted_QML.pkl -b -el
   
.. note::

   Do not forget to optimize hyperparameters if you use different systems.



