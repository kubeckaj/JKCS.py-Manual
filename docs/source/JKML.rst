==========
How to QML
==========

``JKML`` uses QML (https://www.qmlcode.org/index.html) to predict energies of molecular structures.

.. note::

   When setting up JKCS, you should use :guilabel:`-qml`, e.g.:
   
   .. code::
   
      sh setup.sh -r grendel -qml

There are two ways of training, either you train directly on binding energy:

.. math::
   \Delta E^{DFT} = E_{cluster}^{DFT} - \sum E_{monomer}^{DFT}

or on difference between high level and low theory (both calculated for the same structure geometries):

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

   See ``Cluster submission`` (under ``JKCS``) to undertand how to tune cluster parameters.

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



