""""
Module :mod:`openquake.hazardlib.scalerel.Cscale' implements
:class: 'Cscale3_70'
:class: 'Cscale3_75'
:class: 'Cscale3_80'
:class: 'Cscale3_85'
:class: 'Cscale3_90'
:class: 'Cscale3_95'
:class: 'Cscale4_00'
:class: 'Cscale4_05'
:class: 'Cscale4_10'
:class: 'Cscale4_15'
:class: 'Cscale4_20'
:class: 'Cscale4_25'
:class: 'Cscale4_30'
:class: 'Cscale4_35'
:class: 'Cscale4_40'
""""
from openquake.hazardlib.scalerel.base import BaseMSRSigma, BaseASRSigma
""""
A set of classes that implement simple mag-area scaling: log10(A) = Mw -C
with coefficient C ranging from 3.70 to 4.40 (with step of 0.05).
These classes are named with suffix that corresponds to the C. For example, 'Cscale3_70'.
""""

class Cscale3_70(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 3.70)) 

class Cscale3_75(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 3.75)) 

class Cscale3_80(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 3.80)) 

class Cscale3_85(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 3.85)) 

class Cscale3_90(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 3.90)) 

class Cscale3_95(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 3.95)) 

class Cscale4_00(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 4.00)) 

class Cscale4_05(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 4.05)) 

class Cscale4_10(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 4.10)) 

class Cscale4_15(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 4.15)) 

class Cscale4_20(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 4.20)) 

class Cscale4_25(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 4.25)) 

class Cscale4_30(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 4.30)) 

class Cscale4_35(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 4.35)) 

class Cscale4_40(BaseMSRSigma, BaseASRSigma):
     def get_median_area(self, mag, rake):
            return (10 ** (mag - 4.40)) 
