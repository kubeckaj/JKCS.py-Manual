==================
Cluster submission
==================

When working on a (super)computer cluster, all default parameters for submitting jobs are taken from the
file ``parameters.txt`` that is in each subfolder formed from ``input.txt`` with the JKCS1_prepare script. It is assumed that the computer system uses SBATCH to submit jobs. Hence, additional parameters for the SBATCH command could be eventually modified in the ``~/.JKCSusersetup.txt`` under the program_SBATCH function. When calling a JKCS script, it is also possible to overwrite the submission parameters by arguments shown on this page. 

Remember that only JKCS2_explore, JKCS3_run, and JKCS4_collect are scripts that would submit jobs to cluster as these scripts employ 3rd party programs that might demand considerable computational resources. Using the submission parameters for JKCS0_copy, JKCS1_prepare, and JKCS5_filter is not possible. 

Run localy
----------

If you want to run also JKCS2-4 on your local computer and not submit any jobs, you can use:

\-loc
Perform all tasks on computer you are now logged in.

.. code:: bash
  
   JKCS3_run -p XTB -m “--opt --gfn 1” -loc
   JKCS4_collect XTB -loc

.. note::

    It is completely fine to run some tests cluster login nodes BUT keep the tests very short (at maximum 1 or very few minutes) and you should also stay low with memory requirements. 

Submission arguments
--------------------

You can overwrite the default arguments by using these commands:

\-cpu  <integer>
   number of CPU(s) used for one calculation

\-par,\-partition <string>
   partition (queue) name (e.g., test, short, longrun, or hugemem). You should see all partitions by typing command ``info``

\-time <time_format>
   requested walltime (e.g., 72:00:00, 1-00:00:00 or 10:00)

\-taks,\-maxtasks <integer>
   max. number of tasks to be submitted (per cluster subfolder). I am worried that people sometimes do not properly calculate how many jobs they could submit with one command. Therefore, I did restricted your submission to max 100 jobs. You can easily raise the threshold by this argument. 

\-mem,\-memory <memory_string_format>
  size of memory allocated per CPU [e.g., 4000mb or 32gb]

\-jpt,\-jobs <integer>  
   number of calculation jobs gathered into 1 task (=1 submitted job). For instance, 100 Gaussian optimisations can be submitted as 20 jobs where each job will perform 5 calculations using 8 CPUs:

.. code:: bash
  
   JKCS3_run -rf XTB -nf DFT_opt -p G16 -m “ # wb97”

\-N,\-nodes <integer>
   number of nodes. It is by default 1. However, the functionality of this argument was not properly tested yet. See the greasy-multitask section on this page for more details

\-jpt  <integer>
  number of calculation jobs gathered into 1 task (=1 submitted job). For instance, 100 QC calculations can be submitted as 20 jobs where each job will perform 5 calculations using 8 CPUs:

.. code:: bash
   
   JKCSxxxxxxx  -jpt 5 -cpu 8

.. note::

    The order of the arguments is not important.

Greasy (multinodal) multitask single job
----------------------------------------

There is also an option to submit only one job that contain several tasks that will run parallely. It is greasy (=dirty) way of using multinodal clusters where submission of single jobs is not allowed or maximal number of submitted jobs is limitted.

\-greasy
   this will activate greasy mode

\-con,\-cores_on_node <integer>
   number of cores on node where you submit jobs. Default = 40; however, you should set the correct number of cores. You the ``sinfo`` command to see how much cores is on a partition-node.

\-N,\-nodes <integer>
   number of nodes. If the number of tasks requires more nodes, you should set it. If you set more than necessary, then the maximal necessary number of nodes will be used. Remember that there is also some maximal number of nodes per cluster partition.
   
OK, let us see some examples. 
What about 32 Gaussian calculations each using 8 CPUs while submitting to the "medium" partition with 128 cores per node:

.. code:: bash
   
   JKCS3_run -rf XTB -n DFT -m "# wb97xd 6-31++g** opt" -con 128 -cpu 8 -nodes 2 -greasy -par medium -time 12:00:00
   
I can also submit more jobs per each task. For instance, one greasy-worker will do 2 calculation jobs. I will run 64 calculations which will still fit to 2 nodes (2nodes * 128cores * 2jpt / 8cpu = 64jobs). I will increase the walltime though

.. code:: bash
   
   JKCS3_run -rf XTB -n DFT -m "# wb97xd 6-31++g** opt" -con 128 -cpu 8 -nodes 2 -greasy -par medium -time 24:00:00 -jpt 2

.. note::

    I did not test how durable is the argument -jpt. However, at least 3 jobs per task went through easily. 100 did not. Let me know if you find the limit.
