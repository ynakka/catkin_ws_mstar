#!/usr/bin/env python3 

import numpy as np 
import roslib 
import rospy 
import math 
import sys

from mstar_navigation.msg import State6 as State6 # publish state message

from geometry_msgs.msg import TransformStamped, PoseStamped
from sensor_msgs.msg import Imu, MagneticField


class navigation_talker:
    def __init__(self,sampling_frequency,obstacle_name):

        # this needs to be unique for each sensor
        # for now we only have vicon and imu 
        self.sampling_frequency = sampling_frequency
        self.state_nav = State6()
        
        self.state_vicon = np.zeros(6)
        self.state_vicon_old = np.zeros(6)
        
        self.state_imu = np.zeros(6)

        self.obstacle_name = obstacle_name
        self.obstacle_state_nav = State6()
        self.obstacle_state = np.zeros(6)
        self.num_obstacles = len(obstacle_name)

        # intialize the navigation node 
        rospy.init_node('navigation_node',anonymous=True, log_level=rospy.DEBUG)
        spacecraft_name = sys.argv[1]

        # robot
        self.state_publisher_topic = spacecraft_name + '/nav/state_msg'
        self.state_publisher = rospy.Publisher(self.state_publisher_topic, State6, queue_size=1)

        self.obstacle_state_publisher_topic = []
        # self.obstacle_state_publisher = {}
        for i in range(self.num_obstacles):
            self.obstacle_state_publisher_topic.append('obstacle/'+self.obstacle_name[i]+'/nav/state_msg')
        
        self.obstacle_state_publisher1 = rospy.Publisher(self.obstacle_state_publisher_topic[0], State6, queue_size=1)
        # self.obstacle_state_publisher2 = rospy.Publisher(self.obstacle_state_publisher_topic[1], State6, queue_size=1)


        # obstacle 
        # self.obstacle_state_pub

        rate_nav = rospy.Rate(self.sampling_frequency)
        counter = 0
        while not rospy.is_shutdown():
           
            # robot state
            rospy.Subscriber("vicon/" + spacecraft_name + "/" + spacecraft_name, TransformStamped, self.get_vicon_data_call_back)
            rospy.Subscriber(spacecraft_name + "/Imu", Imu, self.get_imu_data_call_back)
            
            self.update_velocity_estimate()
            
            state = self.state_vicon
            state[5] = self.state_imu[5]

            self.update_nav_state(state)
            counter +=1
            print('counter',counter)
            print('state',state)
            self.state_publisher.publish(self.state_nav)
            self.state_vicon_old = self.state_vicon

            # obstacle position
            rospy.Subscriber("vicon/" + self.obstacle_name[0] + "/" + self.obstacle_name[0], TransformStamped, self.get_position_data_call_back)
            #print(self.obstacle_state)
            self.obstacle_state_publisher1.publish(self.obstacle_state_nav)
       
            #rospy.Subscriber("vicon/" + self.obstacle_name[1] + "/" + self.obstacle_name[1], TransformStamped, self.get_position_data_call_back)
            #self.obstacle_state_publisher2.publish(self.obstacle_state_nav)
       
            rate_nav.sleep()


    def get_vicon_data_call_back(self,msg):
        self.state_vicon[0] = msg.transform.translation.x
        self.state_vicon[1] = msg.transform.translation.y 

        q_x = msg.transform.rotation.x
        q_y = msg.transform.rotation.y
        q_z = msg.transform.rotation.z

        q_w = msg.transform.rotation.w
        
        t1 = 2.0*(q_w*q_z + q_x*q_y)
        t2 = 1.0 - 2.0*(q_y*q_y + q_z*q_z)
        self.state_vicon[2] = math.atan2(t1, t2)


    def get_imu_data_call_back(self,msg):
        self.state_imu = np.zeros(6)
        # only get angular velocity from imu
        self.state_imu[5] = -msg.angular_velocity.z

    def get_position_data_call_back(self,msg):
        self.obstacle_state = np.zeros(6)
        self.obstacle_state[0] = msg.transform.translation.x
        self.obstacle_state[1] = msg.transform.translation.y
        self.update_obstacle_nav_state(self.obstacle_state)
        

    def update_velocity_estimate(self):
        self.state_vicon[3] = (self.state_vicon[0] - self.state_vicon_old[0])*self.sampling_frequency
        self.state_vicon[4] = (self.state_vicon[1] - self.state_vicon_old[1])*self.sampling_frequency


    def update_nav_state(self,state):
        self.state_nav.state_x     = state[0]
        self.state_nav.state_y     = state[1]
        self.state_nav.state_theta = state[2]
        self.state_nav.state_dx    = state[3]
        self.state_nav.state_dy    = state[4]
        self.state_nav.state_dtheta = state[5]


    def update_obstacle_nav_state(self,state):
        self.obstacle_state_nav.state_x     = state[0]
        self.obstacle_state_nav.state_y     = state[1]
        self.obstacle_state_nav.state_theta = state[2]
        self.obstacle_state_nav.state_dx    = state[3]
        self.obstacle_state_nav.state_dy    = state[4]
        self.obstacle_state_nav.state_dtheta = state[5]
