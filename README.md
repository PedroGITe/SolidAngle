# SolidAngle
Code to calculate de absolute and relative solid angle of an off and on axis source point subtended by a circular disk

Disk Radius = r_m
Offset from the disk axis = r_0
Distance from the source point to the desk in the disk axis direction = L


For faster results use the fast_num.py and change the variables directly


RUN run.py after installing dependencies:

    from scipy.special import ellipk
    from scipy.special import ellipe
    from scipy.special import ellipkinc
    from scipy.special import ellipeinc
    import numpy as np
    from math import pi, sqrt, atan
    
 For monte Carlo:

    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt
    from math import pi, cos, sin, sqrt
    import itertools



!!The interpolation is an old code interpolated from the values given by the numerical computation!!

The interpolation is only valid for values offset from axis below 2 times the radius of the circular disk and for values of the distance of the source point to the disk from half to two time the value for the desk radius!! 

-->0 <= ra/rm <= 2--<
-->0.5 <= L/rm <= 2 --<
