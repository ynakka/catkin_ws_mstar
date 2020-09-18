#!/usr/bin/env python3

import numpy as np
import roslib
import rospy
import math 
import sys
import csv

from mstar_guidance.msg import Thrusters8 as Thrusters8
from mstar_guidance.msg import State6 as State6 

import trajopt.trajopt as scp 

import rrt_mstar.rrt_ao_mstar as rrt_ao

class guidance_talker:
    def __init__(self,control_param,trajopt_param):

        self.state = np.zeros(6)
        self.thruster = np.zeros(8)

        self.thruster_guid =  Thrusters8()
        self.state_guid = State6()

        self.attitude_control_frequency = control_param['attitude_control_frequency']
        self.position_control_frequency = control_param['position_control_frequency']

        self.max_control_frequency = max(self.position_control_frequency,self.attitude_control_frequency)
        
        ## Setup for planning 

        self.system_param = {'num_states': 6,'num_control':8}
        self.time_param = {'time_init' : 0.0,'time_fin' : 50,'time_steps' : 100}
        self.nominal_trajectory = trajopt_param['nominal_trajectory']
        self.scp_param = trajopt_param['scp_param']
        self.control_cost = trajopt_param['control_cost']
        self.control_limits = trajopt_param['control_limits']
        self.term_state = trajopt_param['terminal_condition']
        # read initial state from sensors
        self.init_state = np.zeros(6)

        
        self.obstacle_name = trajopt_param['obstacle_name']
        self.num_obstacles = len(self.obstacle_name)
        self.obstacle_state_dummy = np.zeros(6)
            
        #intialize the guidance node
        rospy.init_node('guidance_node',anonymous=True, log_level=rospy.DEBUG)
        spacecraft_name = sys.argv[1]
        
        control_guid_publisher_topic = spacecraft_name + '/guid/thruster_msg'
        state_guid_publisher_topic = spacecraft_name +'/guid/state_msg'

		# # an instance for the desired control forces and state in millisec PWM 
        self.control_guid_publisher = rospy.Publisher(control_guid_publisher_topic, Thrusters8, queue_size=1)
        self.state_guid_publisher = rospy.Publisher(state_guid_publisher_topic, State6, queue_size=1)

        # self.obstacle_state_subscriber_topic = []
        # # self.obstacle_state_publisher = {}
        # for i in range(self.num_obstacles):
        #     self.obstacle_state_subscriber_topic.append('obstacle/'+self.obstacle_name[i]+'/nav/state_msg')

        self.obstacle_state = [] #update obstacle state list 
        # rospy.Subscriber(self.obstacle_state_subscriber_topic[0], State6,self.get_obstacle_state)
        # rospy.Subscriber(self.obstacle_state_subscriber_topic[1], State6,self.get_obstacle_state)

        # state_nav_subscriber_topic = spacecraft_name +'/nav/state_msg'
        # rospy.Subscriber(state_nav_subscriber_topic, State6,self.get_initial_state)

        # compute nominal trajectory using RRT 
        self.state_max = np.array([-5,-5,-math.pi,-0.5,-0.5,-10])
        self.state_min = np.array([5,5,math.pi,0.5,0.5,10])
        # state_min = np.array([0,0,-mt.pi,-1,-1,-10])
        # state_max = np.array([1,1,mt.pi,1,1,10])

        x_ao_rrt, u_ao_rrt =  rrt_ao.rrt_ao_mstar(self.init_state,self.term_state,self.max_control_frequency,\
            self.obstacle_state,self.state_min,self.state_max,self.control_limits['u_min'],self.control_limits['u_max'],\
                mass = 10,inertia = 1.62,moment_arm = 0.2)

        # save rrt path file
        np.save('x_ao_rrt.npy',x_ao_rrt)
        np.save('u_ao_rrt.npy',u_ao_rrt)

        # desired_state, desired_control = scp.traj_opt(self.time_param,self.system_param,self.init_state,\
        #                                 self.term_state,self.control_cost,self.control_limits,self.obstacle_state,\
        #                                 self.nominal_trajectory,self.scp_param)


        rate = rospy.Rate(self.max_control_frequency)
        counter = 0
        counter_max = 100 #desired_state.shape[0]  
        # counter_max = end_trajectory # total time steps 
        # plan = False
        while not rospy.is_shutdown():

            # -- plan and save the file --
            # -- update initial state and time horizon for replanning --
            # if plan == True:
            #     # real-time planning section
            #     # set plan to False 
            #     plan = False 

            # read the file and publish the desired state and control 
            # 
            if counter >= counter_max:
                ss = np.zeros(6)
                th = np.zeros(8)
            else:
                ss = np.zeros(6)
                th = np.zeros(8)
                # ss = desired_state[int(counter)]
                # th = desired_control[int(counter)]

            # Update state and Publish the desired state            
            self.update_state(ss)
            self.update_control(th)

            print('counter',counter)            
            print('guidance control',th)
            print('guidance state',ss)

            
            self.state_guid_publisher.publish(self.state_guid)
            self.control_guid_publisher.publish(self.thruster_guid)

            counter = counter + 1 
            # if counter % 10 == 0:
            #     #plan after every 5 sec 
            #     plan = True
            rate.sleep()

    def get_obstacle_state(self,msg):
        self.obstacle_state_dummy = np.zeros(6)
        self.obstacle_state_dummy[0]= msg.state_x
        self.obstacle_state_dummy[1]= msg.state_y
        self.obstacle_state_dummy[2]= msg.state_theta
        self.obstacle_state_dummy[3]= msg.state_dx
        self.obstacle_state_dummy[4]= msg.state_dy
        self.obstacle_state_dummy[5]= msg.state_dtheta
        self.obstacle_state.append([self.obstacle_state_dummy,0.6])

    
    def get_initial_state(self,msg):
        self.init_state = np.zeros(6)
        self.init_state[0]= msg.state_x
        self.init_state[1]= msg.state_y
        self.init_state[2]= msg.state_theta
        self.init_state[3]= msg.state_dx
        self.init_state[4]= msg.state_dy
        self.init_state[5]= msg.state_dtheta

    def update_state(self,s):
        self.state_guid.state_x = s[0]
        self.state_guid.state_y = s[1]
        self.state_guid.state_theta = s[2]
        self.state_guid.state_dx = s[3]
        self.state_guid.state_dy = s[4]
        self.state_guid.state_dtheta = s[5]
        

    def update_control(self,th):
        self.thruster_guid.FXmMZm = th[0]
        self.thruster_guid.FXmMZp = th[1]
        self.thruster_guid.FYmMZm = th[2]
        self.thruster_guid.FYmMZp = th[3]
        self.thruster_guid.FXpMZm = th[4]
        self.thruster_guid.FXpMZp = th[5]
        self.thruster_guid.FYpMZm = th[6]
        self.thruster_guid.FYpMZp = th[7]


# ## read a csv file that has planned trajectory 
#         desired_state = []
#         desired_control = []

#         csv_file = open('/home/nvidia/catkin_ws_stp/src/mstar_guidance/src/trajectories/' + sys.argv[1] + '.csv')
#         sc_trajectory = list(csv.reader(csv_file, delimiter=',', quotechar='|'))
#         end_trajectory = sum(1 for row in sc_trajectory)

#         for i in range(0,end_trajectory):
#             self.state[0] = sc_trajectory[i][0]
#             self.state[1] = sc_trajectory[i][1]
#             self.state[2] = sc_trajectory[i][2]
#             self.state[3] = sc_trajectory[i][3]
#             self.state[4] = sc_trajectory[i][4]
#             self.state[5] = sc_trajectory[i][5]

#             desired_state.append(self.state)

#             self.thruster[0] = sc_trajectory[i][6]
#             self.thruster[1] = sc_trajectory[i][7]
#             self.thruster[2] = sc_trajectory[i][8]
#             self.thruster[3] = sc_trajectory[i][9]
#             self.thruster[4] = sc_trajectory[i][10]
#             self.thruster[5] = sc_trajectory[i][11]
#             self.thruster[4] = sc_trajectory[i][12]
#             self.thruster[5] = sc_trajectory[i][13]

#             desired_control.append(self.thruster)