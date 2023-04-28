# About & Installation

## What is JKQC?

Jammy Key for Quantum Chemistry (JKQC) databases of molecular clusters makes manipulation with quantum chemistry (QC) output files and data (stored in pandas dataframe) available for easy post-processing (e.g. filtering, averaging).

The QC output files (.log,.out,.xyz) into a database (.pkl), which takes significantly less memory and accelerates the data post-processing (e.g., printing energies, including various corrections, and calculation formation properties for ACDC). Depending on the files sizes/cluster sizes/types, the pikling takes approximately from 15 seconds/1000 structures to 3 minutes/1000 structures. Nevertheless, the post-processing usually takes from -immidiately- to a few seconds. (Sorry, JKQC is not parralelizable (at least yet) but I am working on it.)

.. hint::

   See JKQC help to get idea what everything it can do:
   
   ..code:: bash
   
   JKQC -help

## Installation


Altough there are several ways how to utilize only JKQC, the most easiest is anyway installing JKCS. JKQC comes with it for free ;-). See https://jkcs.readthedocs.io/en/latest/JKCSSetupAndInstallation.html



