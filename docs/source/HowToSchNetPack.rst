=================
How to SchNetPack
=================

``JKML`` uses the SchNetPack (https://schnetpack.readthedocs.io) for training the neural network potential. 

.. note::

   When setting up JKCS, you should use :guilabel:`-nn` in order to install SchNetPack, e.g.:
   
   .. code::
   
      sh setup.sh -r grendel -nn

Please, see the QML section or the JKQC section in order to understand how to prepare the input pickle files.

NN parameters
-------------

Let us first list all possible parameters required for training/testing/prediction with NN:

:guilabel:`-help, -help_nn, -help_adv`
    see help text as it is so far the most decriptive when it comes to the arguments

:guilabel:`-nn, -painn`
    to switch for PaiNN architecture of the NN (incompatible with :guilabel:`-qml`). Other architectures (e.g. :guilabel:`-schnet` and :guilabel:`-so3net`) also are available.

:guilabel:`-train <HIGH.pkl> [<LOW.pkl>]`
    the training database. In the case you want to use delta learning, use also a low-level-of-theroy database which corresponds to the high level of theory when it comes to file naming. Often you perform training (using GPU) and then you run new jobs where you use the trained model, which can be called as :guilabel:`-trained <model.pkl>`.

:guilabel:`-test <HIGH.pkl> [<LOW.pkl>]`
    the test database. In the case you use delta learning, provide also a low-level-of-theroy database which corresponds to the high level of theory when it comes to file naming.

:guilabel:`-monomers <HIGH.pkl> [<LOW.pkl>]`
    the database with one representative monomer for each specie (this could be also atoms if you want to use atomization energies; however, the file naming must be modified accordingly). In the case you use delta learning, provide also a low-level-of-theroy database which corresponds to the high level of theory when it comes to file naming.

:guilabel:`-eval,-opt,-md <STR.pkl/xyz> [<LOW.pkl>]`
    the database of structures for which you want to predict the properties, which you want to optimize, or for which you want to run MD (when :guilabel:`-spkmd` is used, provide xyz file). In the case you use delta learning, provide also a low-level-of-theroy database which corresponds to the high level of theory when it comes to file naming. See :guilabel:`-help_adv` for additional argument for tuning the optimization/MD.

Several arguments related to training:

:guilabel:`-epochs <int>`
    Number of iterations/loops/epoch you want to use for the training.

:guilabel:`-batch_size,-bs <int>`
    Number of structures within one batch (subpackage) used for training at the time. In each epoch, NN loops over all batches. Use preferably number which are power of 2.

See other parameters, such as :guilabel:`-nn_train` (overall portion used for training), :guilabel:`-nn_ESpatience` (early stop in case no improvement happens for several epochs), etc. in the :guilabel:`-help_adv`




a simple example of JKML usage with for training NN:


In the `QML` section, we showed the theory behind delta-learning
