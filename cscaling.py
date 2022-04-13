"""
Module :mod:`openquake.hazardlib.scalerel.cscaling` implements
:class: `cscaling3_70`
:class: `cscaling3_75`
:class: `cscaling3_80`
:class: `cscaling3_85`
:class: `cscaling3_90`
:class: `cscaling3_95`
:class: `cscaling4_00`
:class: `cscaling4_05`
:class: `cscaling4_10`
:class: `cscaling4_15`
:class: `cscaling4_20`
:class: `cscaling4_25`
:class: `cscaling4_30`
:class: `cscaling4_35`
:class: `cscaling4_40`
"""
from openquake.hazardlib.scalerel.base import BaseMSR
"""
A set of classes that implement simple mag-area scaling: log10(A) = Mw -C
with coefficient C ranging from 3.70 to 4.40 (with step of 0.05).
These classes are named with suffix that corresponds to the C. For example, 'Cscale3_70'.
"""

class cscaling3_70(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 3.70)) 

class cscaling3_75(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 3.75)) 

class cscaling3_80(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 3.80)) 

class cscaling3_85(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 3.85)) 

class cscaling3_90(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 3.90)) 

class cscaling3_95(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 3.95)) 

class cscaling4_00(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 4.00)) 

class cscaling4_05(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 4.05)) 

class cscaling4_10(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 4.10)) 

class cscaling4_15(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 4.15)) 

class cscaling4_20(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 4.20)) 

class cscaling4_25(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 4.25)) 

class cscaling4_30(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 4.30)) 

class cscaling4_35(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 4.35)) 

class cscaling4_40(BaseMSR):
   def get_median_area(self, mag, rake):
       return (10 ** (mag - 4.40)) 
