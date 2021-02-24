from solid_angle_numerical import solid_angle_numerical
from solid_angle_montecarlo import solid_angle_montecarlo
import numpy as np
from math import pi, sqrt, atan
while True:
    Nevents=0

    #Program to calculate the solid angle subtended by a point off and on axis in a circle
    #Suitable for photosensor solid angle calculations.


    #Solid Angle Calculation for a  Circular Disk F, PAXTON Nuclear Power Department, Research Division, Curtiss-Wright Corporation, Quehanna, Pennsylvania (Received April 14, 1958; and in final form, December 31,1958)

    # r_o - Horizontal distance from the photosensor center to the desired point.
    #r_m - Circle (photosensor) radius
    #L= Vertical distance from the photosensor to the desired point.

    #Numerical calculation in solid_angle_numerical
    print("Warning - Use the same units dor all measurements")
    while True:
        r_0 = input('r_0 - Horizontal distance from the photosensor center to the desired point: ')
        try:
            x = float(r_0)
            break
        except ValueError:
            print ("Oops!  That was no valid number.  Try again ...")
    while True:
        r_m = input('Circle (photosensor) radius: ')
        try:
            x = float(r_m)
            break
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")
    while True:
        L = input('Vertical distance from the photosensor to the desired point: ')
        try:
            x = float(L)
            break
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")

    while True:
        MC = input('Do you want Monte Carlo (0-False, 1-True): ')
        try:
            x = float(MC)
            break
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")

    if int(MC)==1:
            while True:
                nEvents=input('Number of events (could take some time for values > 10000): ')
                plot = input('Plotting data for the monte Carlo Solution 0-False, 1-True: ')
                try:
                    x = int(nEvents)
                    x = float(plot)
                    break
                except ValueError:
                    print ("Oops!  That was no valid number.  Try again...")

            if int(plot)==1 and int(nEvents)>5000:
                while True:
                    plot=input('For this number of data the plot could not be very usefull. Are you sure? 0=No; 1=yes')
                    try:
                        x = float(plot)
                        break
                    except ValueError:
                        print ("Oops!  That was no valid number.  Try again...")

    print('Horizontal distance: ',r_0,'Vertical distance: ',L,'Circle Radius: ', r_m,'Monte Carlo',MC)
    print('Solid Angle: ', solid_angle_numerical(r_0,r_m,L))
    print('Solid Angle (relative): ', solid_angle_numerical(r_0,r_m,L)/(4*pi))

    if int(MC)==1:
        solid_angle_montecarlo(r_0,r_m,L,plot,nEvents)
