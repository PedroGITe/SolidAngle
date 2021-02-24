def solid_angle_numerical(r_0,r_m,L):

    from scipy.special import ellipk
    from scipy.special import ellipe
    from scipy.special import ellipkinc
    from scipy.special import ellipeinc
    import numpy as np
    from math import pi, sqrt, atan
    while True:


        #Solid Angle Calculation for a  Circular Disk F, PAXTON Nuclear Power Department, Research Division, Curtiss-Wright Corporation, Quehanna, Pennsylvania (Received April 14, 1958; and in final form, December 31,1958)

        # r_o é a distancia horizontal do centro do fotosensor até ao ponto desejado para a emissão dos fotões
        #r_m é o raio do fotosensor
        #L=distância vertical do fotosensor ao ponto desejado
        r_0=float(r_0)
        r_m=float(r_m)
        L=float(L)

        #k
        k=sqrt((4*r_0*r_m)/(L**2+(r_0+r_m)**2))
        #alpha²
        alphasq=((4*r_0*r_m)/(r_0+r_m)**2)
        #k'
        kdash=(1-k**2)**(1/2)
        #Rmax
        Rmax=sqrt(L**2+(r_0+r_m)**2)
        #Complete elliptic integral of the first kind K(k)
        K=ellipk(k**2)

        #Calculation of the solid angle for when r_0=r_m
        if r_0==r_m:
            Omega=pi-(2*L/Rmax)*K
            return(Omega)
            break


        #Complete elliptic integral of the second kind E(k)
        E=ellipe(k**2)

        #Calculate epsilon
        epsilon=atan(L/(abs(r_0-r_m)))

        #Incomplete elliptic integral of the first kind F(epsilon,k')
        Finc=ellipkinc(epsilon,kdash**2)

        #Incomplete elliptic integral of the second kind E(epsilon,k')
        Einc=ellipeinc(epsilon,kdash**2)


        #Calculation of the heuman's lambda function (HL)
        HL = 2/pi * (E*Finc + K*Einc - K*Finc)

        #Calculation of the solid angle (Omega)
        if r_0<r_m:
            Omega=2*pi-(2*L/Rmax)*K-pi*HL
        if r_0>r_m:
            Omega=-(2*L/Rmax)*K+pi*HL

        return(Omega)
        break
