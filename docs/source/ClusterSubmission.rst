==================
Cluster submission
==================

Here goes how you should submit to cluster

\-jpt  <int>
  number of calculation jobs gathered into 1 task (=1 submitted job). For instance, 100 QC calculations can be submitted as 20 jobs where each job will perform 5 calculations using 8 CPUs:

.. code:: bash
   
   JKCSxxxxxxx  -jpt 5 -cpu 8
  

Greasy
------

.. code:: bash
   
   python JKQC.py -in mydatabas
