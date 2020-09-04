#!/usr/bin/env python3

import numpy as np
import roslib
import rospy
import sys

import math 
import time 

from navigation_talker import navigation_talker

def main():
    sampling_frequency = 20
    obstacle_name = ['sc2','asteroid']
    nav_talker = navigation_talker(sampling_frequency,obstacle_name)

if __name__=="__main__":
    main()