==================
Cluster submission
==================

When working on a (super)computer cluster, all default parameters for submitting jobs are taken from ``parameters.txt`` in each subfolder formed from ``input.txt`` by JKCS1_prepare. It is assumed that the computer system uses SBATCH to submit jobs. Hence, additional parameters for the SBATCH command could be eventually modified in the ``~/.JKCSusersetup.txt`` under the program_SBATCH function. When calling a JKCS script, it is also possible to overwrite the submission parameters by the arguments shown on this page. 

Remember that only JKCS2_explore, JKCS3_run, and JKCS4_collect are scripts that would submit jobs to cluster as these scripts employ 3rd party programs that might demand considerable computational resources. Using the submission parameters for JKCS0_copy, JKCS1_prepare, and JKCS5_filter is not possible (they run locally). 

Run locally
-----------

If you want to also run JKCS2-4 on your local computer and not submit any jobs, you can use:

-loc
    Perform all tasks on computer you are now logged in.

.. code:: bash
  
   JKCS3_run -p XTB -m “--opt --gfn 1” -loc
   JKCS4_collect XTB -loc
   JKCS4_collect DFT_freq -gibbs -loc

.. note::

    It is completely fine to run some tests cluster login nodes BUT keep the tests very short (at maximum 1 or very few minutes), and you should also stay low with memory requirements. 

Submission arguments
--------------------

To submit jobs to queue the sbatch command of the following format is automatically used by JKCS (you can modify it in ``~/.JKCSusersetup.txt`` under the program_SBATCH function):

.. code:: bash

   sbatch -J "Job_name" -p "Partition_name" --time "Walltime" -N 1 --mem-per-cpu "Memory" script.sh

You can overwrite the default arguments by using these commands:

-cpu  <integer>
    number of CPUs used for one calculation. If you specify only the number of CPUs, the rest of submission arguments (e.g., walltime, partition name) are still taken from ``parameters.txt``
   
.. code:: bash
  
   JKCS3_run -p G16 -rf XTB -nf DFT_opt -m "# wb97xd 6-31++g** opt" -cpu 8   

-par, -partition <string>
    partition (queue) name (e.g., test, short, longrun, or hugemem). You should see all partitions by typing the command: ``sinfo``

-time <time_format>
    requested walltime (e.g., 72:00:00, 1-00:00:00 or 10:00). If you need to submit a simple/fast test on the test partition, run:
   
.. code:: bash
  
   JKCS2_explore -pop 2 -gen 2 -lm 2 -par test -time 10:00
   JKCS4_collect ABC -par test -time 10:00

-mem, -memory <memory_string_format>
    size of memory allocated per CPU [e.g., 4000mb or 32gb]

-jpt <integer>  
    number of calculation jobs gathered into 1 task (=1 submitted job). For instance, 100 Gaussian optimizations can be submitted as 20 jobs where each job will perform 5 calculations using 8 CPUs:

.. code:: bash
  
   JKCS3_run -rf XTB -nf DFT_opt -p G16 -m "# wb97xd 6-31++g** opt" -jpt 5 -cpu 8
   
If you have many conformer combinations, you can reduce the configurational search for each of them and run them in series. If you have 300 combinations, you can submit only 30 jobs using (+ you can do the same with the subsequent XTB optimization):

.. code:: bash
  
   JKCS2_explore -pop 50 -gen 50 -lm "6000/NoC" -jpt 10
   JKCS3_run -jpt 10
   
-taks, -maxtasks <integer>
    max. number of tasks to be submitted (per cluster subfolder). I am worried that people sometimes do not adequately calculate how many jobs they could submit with one command. Therefore, I did restrict your submission to max 100 jobs. You can easily raise this threshold by this argument. 

-N, -nodes <integer>
    number of nodes. It is by default 1. However, the functionality of this argument was not properly tested yet. See the greasy-multitask section on this page for more details.

.. note::

    The order of the arguments is not important.

Greasy (multinodal) multitask single job
----------------------------------------

There is an option to submit only single job that contains several tasks that will run parallely. It is greasy (=dirty) way of using multinodal clusters where submission of single jobs is not allowed or maximal number of submitted jobs is limitted. Since the submitted job has to wait for all tasks to be finished (also the slowest one), it leads to waste of computational resources where CPUs are not used. Hence, it is called greasy.

-greasy
    this will activate greasy mode

-con, -cores_on_node <integer>
    number of cores on node where you submit jobs. Default = 40; however, you should set the correct number of cores. Use the ``sinfo`` command to see how much cores is on a partition-node.

-N, -nodes <integer>
    number of nodes. If the number of tasks requires more nodes, you should set it. If you set more than necessary, then the maximal necessary number of nodes will be used (so feel free to e.g. set -nodes 20 if you do not want to worry about that). Remember that there is also some maximal number of nodes per cluster partition.
   
OK, let us see some examples. 
What about 32 Gaussian calculations each using 8 CPUs while submitting to the "medium" partition with 128 cores per node:

.. code:: bash
   
   JKCS3_run -p G16 -rf XTB -n DFT -m "# wb97xd 6-31++g** opt" -con 128 -cpu 8 -nodes 2 -greasy -par medium -time 12:00:00
   
I can also submit more jobs per each task. For instance, one greasy-worker will do 2 calculation jobs. I will run 64 calculations which will still fit to 2 nodes (2nodes * 128cores * 2jpt / 8cpu = 64jobs). I will increase the walltime though

.. code:: bash
   
   JKCS3_run -p G16 -rf XTB -n DFT -m "# wb97xd 6-31++g** opt" -con 128 -cpu 8 -nodes 2 -greasy -par medium -time 24:00:00 -jpt 2

.. note::

    I did not test how durable is the argument -jpt. However, at least 3 jobs per task went through easily. 100 did not. Let me know if you find the limit.
    
.. note::

    Yet, the greasy option works only for JKCS3_run.
