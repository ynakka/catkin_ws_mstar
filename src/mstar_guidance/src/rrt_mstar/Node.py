#!/usr/bin/env python3

"""
Author: Ellie Cho
Maintainer: Yashwanth Nakka
"""
import numpy as np

class Node:
        """
        RRT Node
        """
        def __init__(self, state):
        	# x is the state vector (x, y, theta, dotx, doty, dottheta)
            self.state = state
            self.path = [] 
            self.parent = None
            self.cost = 0.0
            self.time = 0.0
            self.u = np.zeros(8)
        