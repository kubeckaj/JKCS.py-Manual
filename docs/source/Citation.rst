=========
Citations
=========

Please, if you use any code, try to check if you have cited all literature.

JKCS
----

When you use any JKCS command, please, cite please the following:

 kubecka19
   Kubečka, J.; Besel, V.; Kurtén, T.; Myllys, N.; Vehkamäki, H. Configurational Sampling of Noncovalent (Atmospheric) Molecular Clusters: Sulfuric Acid and Guanidine. *J. Phys. Chem. A* **2019**, *123*, 6022–6033. https://doi.org/10.1021/acs.jpca.9b03853

.. code:: none

   @article{kubecka19,
     author = {J. Kube{\v c}ka and V. Besel and T. Kurt{\'e}n and N. Myllys and H. Vehkam{\"a}ki}, 
     title = {Configurational Sampling of Noncovalent (Atmospheric) Molecular Clusters: Sulfuric Acid and Guanidine},
     journal = {J. Phys. Chem. A}, 
     year = {2019}, 
     volume = {123}, 
     pages = {6022--6033}, 
     doi = {https://doi.org/10.1021/acs.jpca.9b03853},
   }

JKQC
----

JKQC come together with our first machine learning methods, hence cite please: 

kubecka22
   Kubečka, J.; Christiansen, A. S.; Rasmussen, F. R.; Elm, J. Quantum Machine Learning Approach for Studying Atmospheric Cluster Formation. *Environ. Sci. Technol. Lett.* **2022**, *9(3)*, 239–244.

.. code:: none

   @article{kubecka22,
     author = {J. Kube{\v c}ka and A. S. Christensen and F. R. Rasmussen and J. Elm}, 
     title = {Quantum Machine Learning Approach for Studying Atmospheric Cluster Formation},
     journal = {Environ. Sci. Technol. Lett.}, 
     year = {2022}, 
     volume = {9}, 
     pages = {239--244}, 
     number = {3},
     doi = {https://doi.org/10.1021/acs.estlett.1c00997},
   }

JKML
----

When you use JKML, please cite:

kubecka22
   Kubečka, J.; Christiansen, A. S.; Rasmussen, F. R.; Elm, J. Quantum Machine Learning Approach for Studying Atmospheric Cluster Formation. *Environ. Sci. Technol. Lett.* **2022**, *9(3)*, 239–244.

QML
===

If you use kernel ridge regression (KRR) with the FCHL19 molecular representation, cite also the following:

qml
   Christensen, A. S.; Faber, F. A.; Huang, B.; Bratholm, L. A.; Tkatchenko, A.; Muller, K. R.; von Lilienfeld, O. A. QML: A Python Toolkit for Quantum Machine Learning. **2017**; https://github.com/qmlcode/qml (*accessed February 7, 2023*).

christiansen20
   Christensen, A. S.; Bratholm, L. A.; Faber, F. A.; von Lilienfeld, O. A. FCHL Revisited: Faster and More Accurate Quantum Machine Learning. *J. Chem. Phys.* **2020**, *152*, 044107.
 

.. code:: none

   @article{kubecka22,
     author = {J. Kube{\v c}ka and A. S. Christensen and F. R. Rasmussen and J. Elm}, 
     title = {Quantum Machine Learning Approach for Studying Atmospheric Cluster Formation},
     journal = {Environ. Sci. Technol. Lett.}, 
     year = {2022}, 
     volume = {9}, 
     pages = {239--244}, 
     number = {3},
     doi = {https://doi.org/10.1021/acs.estlett.1c00997},
   }
   @misc{qml,
     author = {A. S. Christensen and F. A. Faber and B. Huang and L. A. Bratholm and A. Tkatchenko and K. R. Muller and O. A. von Lilienfeld},
     title = {{QML}: {A} {P}ython Toolkit for Quantum Machine Learning},
     year = {2017},
     note = {\url{https://github.com/qmlcode/qml} (accessed February 7, 2023)}
   }
   @article{christensen20,
     author = {A. S. Christensen and L. A. Bratholm and F. A. Faber and O. A. {von Lilienfeld}}, 
     title = {{FCHL} Revisited: {F}aster and More Accurate Quantum Machine Learning},
     journal = {J. Chem. Phys.}, 
     year = {2020}, 
     volume = {152}, 
     pages = {044107}, 
     doi = {https://doi.org/10.1063/1.5126701},
   }

NN
==

TBC

JKacdc
------

You should cite the Pearl code itself:

mcgrath12
   McGrath, M. J.; Olenius, T.; Ortega, I. K.; Loukonen, V.; Paasonen, P.; Kurtén, T.; Kulmala, M.; Vehkamäki, H. Atmospheric Cluster Dynamics Code: a flexible method for solution of the birth-death equations. *Atmos. Chem. Phys.* **2012**, *12(5)*, 2345–2355.

and also the repository of T. Olenius which codes were modified and inspiried by within JKacdc code:

acdc
   Olenius T. ACDC: Atmospheric Cluster Dynamics Code. **2023**; https://github.com/tolenius/ACDC (*accessed February 7, 2023*).

.. code:: none 

   @article{mcgrath12,
     author = {McGrath, M. J. and Olenius, T. and Ortega, I. K. and Loukonen, V. and Paasonen, P. and Kurt{\'e}n, T. and Kulmala, M. and Vehkam{\"a}ki, H.},
     title = {Atmospheric Cluster Dynamics Code: a flexible method for solution of the birth-death equations},
     journal = {Atmos. Chem. Phys.},
     volume = {12},
     year = {2012},
     number = {5},
     pages = {2345--2355},
     doi = {https://doi.org/10.5194/acp-12-2345-2012}
   }
   @misc{acdc,
     author = {T. Olenius},
     title = {ACDC: Atmospheric Cluster Dynamics Code},
     year = {2023},
     note = {\url{https://github.com/tolenius/ACDC} (accessed February 7, 2023)}
   }
