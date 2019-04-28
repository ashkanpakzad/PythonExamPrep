import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser

def julia_value(zx,zy,Cx,Cy,Color_precision):
    i = Color_precision
    t=True
    while t==True:
        if zx*zx+zy*zy>=4:
            t=False
        if i<=1:
            t=False
        zx_plus1=zx*zx-zy*zy+Cx
        zy=2.0*zx*zy+Cy
        zx=zx_plus1
        i=i-1
    return i

def julia_set(xcanvas=800, ycanvas=600, Cx=-0.7, Cy=0.27015, 
                  Color_precision =255, xscale=3, yscale=2):
    Canvas = np.zeros([ycanvas,xcanvas])
    for x in range(xcanvas):
        for y in range(ycanvas):
            zx=xscale*(x-xcanvas/2)/(xcanvas)
            zy=yscale*(y-ycanvas/2)/(ycanvas)
            Canvas[y][x] = julia_value(zx,zy,Cx,Cy,Color_precision)
    return Canvas

if __name__ == "__main__":
    parser = ArgumentParser(description="Generate ""filled in"" Julia set,"
                            "results saved as julia.png")
    parser.add_argument('Cx',nargs='?',default=-0.7 ,type=float)
    parser.add_argument('Cy',nargs='?',default=0.27015,type=float)
    parser.add_argument('--xcanvas',nargs='?', default=800,type=float)
    parser.add_argument('--ycanvas',nargs='?',default=600,type=float)
    parser.add_argument('--xscale', nargs='?',default=3.0,type=float)
    parser.add_argument('--yscale', nargs='?',default=2.0,type=float)
    parser.add_argument('--color_precision',nargs='?', default=255,type=int)
    parser.add_argument('--filename',nargs='?', default='julia.png',type=str)


    args= parser.parse_args()
    Cx = args.Cx
    Cy = args.Cy
    xcanvas = args.xcanvas
    ycanvas = args.ycanvas
    color_precision = args.color_precision
    xscale = args.xscale
    yscale = args.yscale
    
    image = julia_set(Cx=Cx, Cy=Cy, xcanvas=xcanvas, ycanvas=ycanvas, 
                      Color_precision=color_precision, xscale=xscale, 
                      yscale= yscale)
    plt.imshow(image)
    plt.savefig(args.filename)


## REFACTORING:
# Changed import * to np
# Defined variables for canvas size
# Defined variables for max iterations
# Simplified gridding of vanvas
# Defined variables for scaling grid on canvas
# Identified C real and C imag, made them variables.
# Created seperate function to find value on grid
# Converted creation of juliaset into a function with default values. 
# Converted variables with meaningless names (A and a)