# mag-area-cscaling
Generate OQ script to implement classes for Mag-Area scaling 



We write a python script "cscaling.py" that implements a series of classes that extends the "scalerel" base in the OpenQuake package. Target location of the generated script is the folder: openquake/hazardlib/scalerel.

The magnitude-area scaling considered is in simple form with a single coefficent such that,

log10(A) = Mag-C

where C ranges from 3.7 to 4.4, with step of 0.05.

To add, the above follows a philosophy of self-similar scaling with slope = 1 in the log-linear equation. 
