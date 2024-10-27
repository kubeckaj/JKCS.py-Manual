============================================
Pulling
============================================

.. contents:: Table of Contents
   :depth: 2

Introduction
============

Here, we will discuss how to pull various moulecules. As an example, I will take ``10w.xyz`` file and ``1cl.xyz`` file to construct chloride anion above water cluster:

.. code-block:: bash

   JKMD 10w.xyz -recenter 1cl.xyz -chrg -1 -moveto [6,0,0] -ns 0 -loc

This will take quite short time as only single-point calculation is performed. In the end you will get this:

.. image:: 10w1cl.png
      :alt: filesstructure
      :width: 600
      :align: center

This is the system we will work with. 

Pulling a specie
================

If you want to pull the chloride, it is quite easy because it is a separate file, i.e. a separate specie. Let us pull it towards the cluster:

.. code-block:: bash

   JKMD 10w.xyz -recenter 1cl.xyz -chrg -1 -moveto [6,0,0] -EF_c_COM [-1,0,0] -ns 1000 -loc

The force applied on the COM = center of mass is 1 kcal/mol/Angstrom in the direction of the cluster.

We could also go oppositely and pull the water cluster towards the chloride. By applying 1 kcal/mol/Angstrom on the cluster COM, the force gets redistributed over the cluster atoms to give all species the same acceleration. 

.. code-block:: bash

   JKMD 10w.xyz -recenter -EF_c_COM [1,0,0] 1cl.xyz -chrg -1 -moveto [6,0,0] -ns 1000 -loc

Pulling a fragment
==================

Well I have not built this yet. However, at some point I will. For now you can just simply split your xyz file into fragments on your own.

