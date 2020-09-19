
import numpy as np
import scipy as sp
import matplotlib  
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle

import matplotlib.transforms as transforms


def rectagular_obstacle(left_corner_x,left_corner_y,width,height,ax,angle=0.0,facecolor='none',**kwargs):
    addrectangle = Rectangle((left_corner_x,left_corner_y),width=width,height=height,angle=angle,facecolor=facecolor, **kwargs) 
    return ax.add_patch(addrectangle)

def circular_obstacle(x, y, radius, ax, facecolor='none', **kwargs):
    
    """
    Create a plot of the obstacle.

    Parameters
    ----------
    x, y : is the center of the obstacle
        Input data.

    ax : matplotlib.axes.Axes
        The axes object to draw the ellipse into.

    Returns
    -------
    matplotlib.patches.circle

    Other parameters
    ----------------
    kwargs : `~matplotlib.patches.Patch` properties
    """
    center_x = x
    center_y = y 
    add_circle = Circle((center_x,center_y),radius,facecolor=facecolor, **kwargs) 
    return ax.add_patch(add_circle)

    