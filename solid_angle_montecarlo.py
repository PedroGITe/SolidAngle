def solid_angle_montecarlo(r_0,r_m,L,plot,nEvents):
    from mpl_toolkits import mplot3d
    import numpy as np
    import matplotlib.pyplot as plt
    from math import pi, cos, sin, sqrt
    import itertools

    #Function to generate a random 3D vector.
    def random_three_vector():
        """
        Generates a random 3D unit vector (direction) with a uniform spherical distribution
        Algo from http://stackoverflow.com/questions/5408276/python-uniform-spherical-distribution
        :return:
        """
        phi = np.random.uniform(0,np.pi*2)
        costheta = np.random.uniform(-1,1)
        theta = np.arccos( costheta )
        x = np.sin( theta) * np.cos( phi )
        y = np.sin( theta) * np.sin( phi )
        z = np.cos( theta )
        return (x,y,z)

    #Initialize the variables
    'r_o - Horizontal distance from the photosensor center to the desired point: '
    'Circle (photosensor) radius: '
    'Vertical distance from the photosensor to the desired point: '
    r_0=float(r_0)
    r_m=float(r_m)
    L=float(L)
    nEvents=int(nEvents)
    plot=int(plot)


    #Initialize the meaningfull vectors
    vecttot=[]
    vectfalse=[]
    vecttrue=[]

    #Create a list of random vectors
    for i in np.linspace(0, 1, nEvents):
         a=(random_three_vector())
         vecttot.append(a)


    #Normalisation (The largest distance from the circle to the point is 1)
    norm=sqrt((r_0+r_m)**2+L**2)
    r=r_m/norm
    c1=r_0/norm
    c2=0
    c3=L/norm
    a1=1
    a2=0
    a3=0
    b1=0
    b2=1
    b3=0

    #Calculation of which vectors hit the circle projection on the unit sphere
    theta = np.linspace(0, 2*pi, 10000)
    X=[]
    Y=[]
    Z=[]
    X1=[]
    Y1=[]
    Z1=[]
    for vec in vecttot:
        for i in theta:
            x = c1+r*cos(i)*a1 + r*sin(i)*b1
            y = c2+r*cos(i)*a2 + r*sin(i)*b2
            z = c3+r*cos(i)*a3 + r*sin(i)*b3
            a=1/sqrt(x**2+y**2+z**2)
            if vec[0]>=a*x and vec[1]>=a*y and vec[2]>=a*z:
                    vecttrue.append(vec)
                    break
    #Find which ones did not hit
    vectfalse=[elem for elem in vecttot if elem not in vecttrue]

    #Printing stuff
    print('Total Number',len(vecttot))
    print('Hits',len(vecttrue))
    print('No hits', len(vectfalse))
    Omega=len(vecttrue)/len(vecttot)
    print ('Solid Angle: ', Omega*(4*pi))
    print ('Solid Angle (relative): ',Omega)

    #plotting stuff
    if plot == 1:

        for i in theta:
            x = c1+r*cos(i)*a1 + r*sin(i)*b1
            y = c2+r*cos(i)*a2 + r*sin(i)*b2
            z = c3+r*cos(i)*a3 + r*sin(i)*b3
            a=1/sqrt(x**2+y**2+z**2)
            X.append(x)
            Y.append(y)
            Z.append(z)
            X1.append(a*x)
            Y1.append(a*y)
            Z1.append(a*z)

        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(X, Y, Z, 'gray',label='Circle (Photosensor)')
        ax.plot3D(X1, Y1, Z1, 'green',label='Circle projection on the unit sphere')
        ax.scatter(0,0,0,edgecolor="r", facecolor="r",label='Emission point')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        ax.legend()
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.plot3D(X1, Y1, Z1, 'green',label='Circle projection on the unit sphere')
        X=[]
        Y=[]
        Z=[]
        X1=[]
        Y1=[]
        Z1=[]
        for i in vecttrue:
            X.append(i[0])
            Y.append(i[1])
            Z.append(i[2])
        for i in vectfalse:
            X1.append(i[0])
            Y1.append(i[1])
            Z1.append(i[2])

        ax.scatter(X,Y,Z, edgecolor="r", facecolor="gold",label='Hits')
        ax.scatter(0,0,0,edgecolor="r", facecolor="r",label='Emission point')
        ax.scatter(X1,Y1,Z1, edgecolor="g", facecolor="limegreen",label='no Hits')
        ax.legend()
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
        plt.show()
    return(Omega*(4*pi))
