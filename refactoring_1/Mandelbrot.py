import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser

def mandel_value(k,Cx,Cy,Color_precision):
    i = Color_precision
    t=True
    z = complex(Cx,Cy)
    while t==True:
        if abs(z)>=2.0:
            t=False
        if i<=1:
            t=False
        z = z**k+complex(Cx,Cy)
        i=i-1
    return i

def mandel_set(k=2, xcanvas=800, ycanvas=600, 
                  Color_precision =255, xscale=3, yscale=2):
    Canvas = np.zeros([ycanvas,xcanvas])
    for x in range(xcanvas):
        for y in range(ycanvas):
            Cx=xscale*(x-xcanvas/2)/(xcanvas)
            Cy=yscale*(y-ycanvas/2)/(ycanvas)
            Canvas[y][x] = mandel_value(k, Cx,Cy,Color_precision)
    return Canvas

if __name__ == "__main__":
    parser = ArgumentParser(description="Generate ""filled in"" Julia set,"
                            "results saved as julia.png")
    parser.add_argument('k',nargs='?',default=2 ,type=int)
    parser.add_argument('--xcanvas',nargs='?', default=800,type=int)
    parser.add_argument('--ycanvas',nargs='?',default=600,type=int)
    parser.add_argument('--xscale', nargs='?',default=3.0,type=float)
    parser.add_argument('--yscale', nargs='?',default=2.0,type=float)
    parser.add_argument('--color_precision',nargs='?', default=255,type=int)
    parser.add_argument('--filename',nargs='?', default='mandel.png',type=str)


    args= parser.parse_args()
    k = args.k
    xcanvas = args.xcanvas
    ycanvas = args.ycanvas
    color_precision = args.color_precision
    xscale = args.xscale
    yscale = args.yscale
    
    image = mandel_set(k=k, xcanvas=xcanvas, ycanvas=ycanvas, 
                      Color_precision=color_precision, xscale=xscale, 
                      yscale= yscale)
    plt.imshow(image)
    plt.savefig(args.filename)
