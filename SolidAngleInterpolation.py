from scipy import interpolate
import matplotlib.pyplot as plt
import numpy as np
from math import pi
from scipy.interpolate import fitpack
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import os
import sys

#Input and test variables

while True:
    try:
        rm=float(input("Photosensor radius (rm)"))
        ra=float(input("Point of origin distance from the axis of the photosensor along the rm direction (ra)"))
        L=float(input("Distance from  the photosensor in the photosensor axis direction (L)"))
        plotvar=int(input("Show the plot (true or false) -> (1 or 0)"))
        fac1=ra/rm
        fac2=L/rm
        test=[rm, ra, L, plotvar, fac1, fac2]
        for i in test:
            if i < 0:
                sys.exit("ra, rm and L must be over 0")
            if not (0) <= test[4] <= (2):
                sys.exit("ra/rm between 0 and 2")
            if not (0.5) <= test[5] <= 2:
                sys.exit("L/rm between 0.5 and 2")
            if test[3] !=0 and test[3] !=1:
                sys.exit("Plot is on or off (1 or 0)")
        break
    except ValueError:
        print ("Oops!  That was no valid number.  Try again...")


#open file to interpolate and interpolation

x=[]
y=[]
z=[]
with open('ValuesSolidAngle.txt') as f:
    for line in f:
        line = line.split()
        x.append(float(line[0]))
        y.append(float(line[1]))
        z.append(float(line[2]))


tck = interpolate.bisplrep(x,y,z,s=1)

#print results

fac3=interpolate.bisplev(fac1,fac2,tck)
print ("Ângulo sólido absoluto =",fac3)
print ("Ângulo sólido relativo(fracção de 4*""$\pi$)"" =", fac3/(4*pi))

#Plot point and "surface"
xnew = np.arange(0, 2, 0.01)
ytriste=np.arange(0.5, 2, 0.01)
znew=[]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for a in ytriste:
    ynew=[]
    znew=[]
    for i in xnew:
        ynew.append(a)
        znew.append(interpolate.bisplev(i,a,tck))
    ax.plot(xnew,ynew,znew)
ax.set_xlim(0, 2)
ax.set_ylim(0.5, 2)
ax.set_zlim(0, 4)
ax.plot([fac1],[fac2],[fac3],marker='o', markersize=10, color="red")
ax.quiver([1], [1.25], [4], [-1*(1-fac1)],[-1*(1.25-fac2)],[-1*(4-fac3)], length=1, normalize=False)
ax.scatter(x,y,z, marker = '^')
ax.set_xlabel('ra/rm')
ax.set_ylabel('L/rm')
ax.set_zlabel('$\Omega$')
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
textstr = '\n'.join((
    r'$\Omega=%.4f$' % (fac3, ),
    r'$\Omega (relative)=%.4f$' % (fac3/(4*pi), )))
ax.text(10, 10, 12, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top',horizontalalignment='right', bbox=props)
if plotvar == 1:
    plt.show()
f.close()
