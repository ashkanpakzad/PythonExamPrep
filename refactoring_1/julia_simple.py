import numpy as np
import matplotlib.pyplot as plt

def julia_value(zx,zy,Cx,Cy,Color_precision):
    '''
    Determines value assignment for given complex number (z = zx+ zyi) with 
    constant (C = Cx + Cyi). Color precision by default set to 8 bit.
    '''
    i = Color_precision
    t=True
    while t==True:
        if zx*zx+zy*zy>=4: # Check if z has started to approach infty.
            t=False
        if i<=1: # Check If z will not approached infty at all.
            t=False
        zx_plus1=zx*zx-zy*zy+Cx # set up next iteration of zx
        zy=2.0*zx*zy+Cy # set up next iteration of zy
        zx=zx_plus1
        i=i-1
    return i

def julia_set(Cx=-0.7, Cy=0.27015, xcanvas=800, ycanvas=600,
                  Color_precision =255, xscale=3, yscale=2):
    '''
    Creates julia set image for grid of given size for fixed C of the iterative 
    complex quadratic equation Z_n+1 = Z_n^2 + C. Both z and C are complex 
    numbers split into their real (x) and imaginary (y) components.
    
    Where each point on the grid 
    is evaluated as Z_n, if Z_n remains below 4 during iteration then it is 
    considered part of the julia set and will be assigned a value of 0. 
    
    If Z_n>4 straight away, e.g. z_n = 4 + 5i then it is assigned 255 
    (by default).
    
    If Z_n starts below 4 but will iterate beyond it then it will be assigned a 
    value between 1 and 255.
    '''
    Canvas = np.zeros([ycanvas,xcanvas]) # Set up canvas
    for x in range(xcanvas):
        for y in range(ycanvas):
            # make centre of canvas the origin of grid.
            zx=xscale*(x-xcanvas/2)/(xcanvas)
            zy=yscale*(y-ycanvas/2)/(ycanvas)
            # Assign value for canvas depending on approach to infty.
            Canvas[y][x] = julia_value(zx,zy,Cx,Cy,Color_precision)
    return Canvas

# plot image
image = julia_set()
plt.imshow(image)
plt.colorbar()
plt.show()
