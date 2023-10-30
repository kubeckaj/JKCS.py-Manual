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

Some arguments related to the NN architecture:

:guilabel:`-nn_ab <int>`
    Size of the feature vector for each atom type. Training of very large feature vectors might take more time.

:guilabel:`-nn_int <int>`
    Depth of the NN, i.e. how many interaction layers are used. 

:guilabel:`-nn_rb <int>`
    Radial basis size, i.e. how many point from the atom to the cutoff distance are taken.

:guilabel:`-nn_cutoff, -cutoff <float>`
    The interaction distance.

.. note::

   See the Cluster submission section for understanding how to submit the jobs. Eventually, you can modify `program_SBATCH` function in the `~/.JKCSusersetup.txt`.

Examples
--------

Let us take some DFT data, shuffle them, and split them into two halves:

.. code::
   
   JKQC DFT.pkl -shuffle -out DFT_shuffled.pkl
   JKQC DFT_shuffled.pkl -split 2
   mv DFT_shuffled_v1.pkl DFTtrain.pkl 
   mv DFT_shuffled_v2.pkl DFTtest.pkl
   JKQC DFT.pkl -sort el -select 1 -extract 1sa,1w,1am -out DFTmonomers.pkl 

Direct training of electronic energies (dicouraged), where 4 CPU (hence, the number of workers, :guilabel:`-nw`, is also 4) and 1 GPU is used on the `qgpu` partition. Let us do also short training just for a test:

.. code::
   
   JKML -nn -train DFTtrain.pkl -par qgpu -cpu 4 -nw 4 -epochs 10

The result `model.pkl` can be then used for testing:

.. code::
   
   JKML -nn -trained model.pkl -test DFTtest.pkl -par q64 -cpu 1 
   tail -f output

The result will be most likely terrible. Hence let us train on el. binding energies instead (the monomers must be obsly calculated at the same method). I will now combine it with the test too.

.. code::
   
   JKML -nn -train DFTtrain.pkl -monomers DFTmonomers.pkl -test DFTtest.pkl -par qgpu -cpu 4 -nw 4 -epochs 10

This should give better results but still most likely not acceptable. So just increase the epochs, training set size, or generaly tune the hyperparameters of the NN architecture above (we have code for it but yet it is not automated).

In the `QML` section, we showed the theory behind delta-learning. We can do the same with NN: 

.. code::
   
   JKML -nn -train HIGHtrain.pkl LOWtrain.pkl -monomers HIGHmonomers.pkl LOWmonomers.pkl -par qgpu -cpu 4 -nw 4 
   JKML -nn -trained model.pkl -test HIGHtest.pkl LOWtest.pkl -monomers HIGHmonomers.pkl LOWmonomers.pkl -par q64 -cpu 1 
   JKML -nn -trained model.pkl -eval str.pkl LOWstr.pkl -monomers HIGHmonomers.pkl LOWmonomers.pkl -par q64 -cpu 1 

Last line corresponds to prediction of binding energies of new structures.

.. hint::

   You can train any other property by using :guilabel:`-column <str> <str>`:

   .. code::

      JKQC DFT.pkl -info
      JKML -nn -train DFT.pkl -column "log" "zero_point_energy" -par qgpu -cpu 4 -nw 4 

   Other properties can be added to the pickle file by using `-add <column> <file>` from a file that contains two columns: file basename and the property of interest:

   .. code::

      JKQC DFT.pkl -add mobility mobility_file.txt -out DFT_mob.pkl
      JKML -nn -train DFT.pkl -eval str.pkl -column "extra" "mobility" -par qgpu -cpu 4 -nw 4 

FORCES
------

If we collected the forces as well (`JKQC -folder DFT -collect log -forces -out DFTwithforces.pkl`), we can the very same as above and forces will be automatically included in the training. The cost function is by default defined as 1:9 energy and force mean absolute errors (MAEs). You can turnoff trainig of the forces by using :guilabel:`-noforces`. The output will then contain MAE of both energies and forces too. 

.. note::

   The cutoff value can be specified for both training and OPT/MD. I have no clue what happens if you specify different value for both of them. 

The structure (TODO: so far applicable only for one structure) can be optimized as:

   .. code::

      JKML -nn -trained model.pkl -opt str.pkl -par q64 -cpu 1 

.. note::

   See other parameters of the optimizer or for MD by using :guilabel:`-help_adv`.

You can run also MD as:

.. code::

   JKML -nn -trained model.pkl -md str.pkl -par q64 -cpu 1 -md_timestep 0.2 -md_steps 1000 -md_temperature 300

This will initialize velocities with respect to Maxwell Boltzmann distribution and then run MD through ASE with the Langevin thermostat. Well this part is not much tuneable yet as we sticked to the spkmd script within SchNetPack. This one you can initialize as:

.. code::

   JKML -spkmd -trained model.pkl -md 3sa3w.xyz -par q64 -cpu 1 -md_timestep 0.2 -md_steps 1000 -md_temperature 300 -langevin

The results can be afterwards easily visulised as:

.. code::

   JKpython
   python analyse.py

Other predefined options can be found in the :guilabel:`-help_adv` or see https://schnetpack.readthedocs.io/en/latest/userguide/md.html for more details on the spkmd commands. You add several of these command by using :guilabel:`-spkmd_extra <string>`.
