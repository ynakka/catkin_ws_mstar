#!/usr/bin/env python3

import numpy as np
import roslib
import rospy
import math 
import sys

from mstar_controller.msg import Thrusters8 as Thrusters8
from mstar_controller.msg import State6 as State6  # Change to navigation msg 


import controller_3dof as cntrl
import low_pass_filter as lpf

class control_talker:
	def __init__(self,system_param,thruster_param,control_param,filter_param,waypoint_error):

		# system parameters
		self.system_param = system_param

		self.gain_position = control_param['gain_position']
		self.gain_attitude = control_param['gain_attitude']

		self.manifold_pressure = thruster_param['manifold_pressure']

		self.attitude_control_frequency = control_param['attitude_control_frequency']
		self.position_control_frequency = control_param['position_control_frequency']

		self.position_error = waypoint_error['position_error']
		self.attitude_error = waypoint_error['attitude_error']

		# self.alpha_attitude = lpf.first_order_iir_param(fs,fc)
		# self.alpha_position = lpf.first_order_iir_param(fs,fc)
		
		# parameter for iir velocity and angular velocity filter
		#  
		self.alpha_position = filter_param['alpha_position']
		self.alpha_attitude = filter_param['alpha_attitude']

		# dummy variables 

		self.min_impulse_bit = 0.01 #20milli sec
		self.max_control_frequency = max(self.position_control_frequency,self.attitude_control_frequency)
		self.max_impulse_bit = 0.3/self.max_control_frequency

		self.state_old_nav = np.zeros(6)
		self.state_nav = np.zeros(6)

		self.state_old_guid = np.zeros(6)
		self.state_guid = np.zeros(6)
		self.control_guid = np.zeros(8)

		self.counter = -1

		# control msg 
		self.thruster = Thrusters8()
		self.thruster_times_ms = np.zeros(8)

		# preliminary variables using methods 

		self.a, self.b, self.thrust_max = cntrl.thuster_model(self.manifold_pressure)
		# following outputs a python method
		self.thruster_force_to_times = cntrl.thruster_model_force_to_times(self.max_control_frequency,self.a,self.b) 
		

		# intialize the control node 
		rospy.init_node('control_node')
		spacecraft_name = sys.argv[1]
		control_publisher_topic = spacecraft_name + '/thruster_msg'
		# publishwe instance for the control forces in millisec PWM 
		self.control_publisher = rospy.Publisher(control_publisher_topic, Thrusters8)

		# topic names 

		self.state_guidance_topic = spacecraft_name +'/guid/state_msg'
		self.control_guidance_topic = spacecraft_name + '/guid/thruster_msg'
		
		self.state_nav_topic = spacecraft_name + '/nav/state_msg'


		rate_control = rospy.Rate(1)

		time_step = 0
		# bool_attitude= False
		while not rospy.is_shutdown():
			#-------------------------------------------------------------------------
			##----subscribe to the guidance algorithm and update desired states-------
			# Note: The guidance control needs to be thruster force 
			#-------------------------------------------------------------------------
			self.state_guidance_subscriber =  rospy.Subscriber(self.state_guidance_topic,State6,self.state_guidance_call_back)
			self.control_guidance_subscriber = rospy.Subscriber(self.control_guidance_topic,Thrusters8,self.control_guidance_call_back)
			

			#-------------------------------------------------------------------------
			##----------subscribe to the navigation algorithm-------------------------------
			##----compute and publish control in the callback function----------------------------
			#-------------------------------------------------------------------------
			self.state_nav_subscriber = rospy.Subscriber(self.state_nav_topic,State6,self.state_nav_call_back)
			
			self.update_thruster_times(self.thruster_times_ms)
			# publish and wait
			self.control_publisher.publish(self.thruster)

			print('thruster_times_ms',self.thruster_times_ms)
			
			# set old state
			self.state_old_nav = self.state_nav
			self.state_old_guid = self.state_guid

			time_step = time_step +1
			# if time_step % 2 == 0:
			# 	self.min_impulse_bit = 0.0 #20milli sec
			# 	bool_attitude = True
			# else:
			# 	self.min_impulse_bit = 0.04 #20milli sec
			# 	bool_attitude = False
			print('time_step', time_step)
			rate_control.sleep()


	def state_nav_call_back(self,msg):
		
		self.state_nav[0] = msg.state_x
		self.state_nav[1] = msg.state_y
		self.state_nav[2] = msg.state_theta
		self.state_nav[3] = msg.state_dx
		self.state_nav[4] = msg.state_dy
		self.state_nav[5] = msg.state_dtheta 

		# compute error 
		self.position_error, self.velocity_error, self.theta_error, self.thetad_error = cntrl.filtered_state_error(self.state_guid,self.state_nav,self.state_old_guid,self.state_old_nav,
																		self.alpha_position,self.alpha_attitude)
		
		# compute control force
		self.control_force = cntrl.controller(self.position_error, self.velocity_error,self.theta_error,self.thetad_error,\
										self.gain_position,self.gain_attitude,self.position_control_frequency,\
										self.attitude_control_frequency)

		# compute thruster force using control allocation tehcnique
		self.thruster_force = cntrl.control_allocation(self.state_nav[2],self.control_force,self.system_param)
		# saturation filter
		self.thruster_force = cntrl.thruster_force_saturation(self.thruster_force,self.thrust_max)
		# Note: saturation filter not required if using QP formulation

		
		# Project the forces to thrustes PWM width in millisec
		self.thruster_times_sec = self.thruster_force_to_times(self.thruster_force)
		self.thruster_times_ms = cntrl.impulse_bit_filter(self.thruster_times_sec,self.max_impulse_bit,self.min_impulse_bit)		

		# if self.counter < 0:
		# 	self.thruster_times_ms = np.zeros(8)
		# 	self.counter = 1


	

	def state_guidance_call_back(self,msg):
		self.state_guid[0] = msg.state_x
		self.state_guid[1] = msg.state_y
		self.state_guid[2] = msg.state_theta
		self.state_guid[3] = msg.state_dx
		self.state_guid[4] = msg.state_dy
		self.state_guid[5] = msg.state_dtheta
	

	def control_guidance_call_back(self,msg):
		self.control_guid[0] = msg.FXmMZm
		self.control_guid[1] = msg.FXmMZp
		self.control_guid[2] = msg.FYmMZm
		self.control_guid[3] = msg.FYmMZp
		self.control_guid[4] = msg.FXpMZm
		self.control_guid[5] = msg.FXpMZp
		self.control_guid[6] = msg.FYpMZm
		self.control_guid[7] = msg.FYpMZp


	def update_thruster_times(self,thruster_times_ms):
		# self.thruster.FXmMZm = 0
		# self.thruster.FXmMZp = 0
		# self.thruster.FYmMZm = 0
		# self.thruster.FYmMZp = 0
		# self.thruster.FXpMZm = 0
		# self.thruster.FXpMZp = 0
		# self.thruster.FYpMZm = 0
		# self.thruster.FYpMZp = 0
		self.thruster.FXmMZm = thruster_times_ms[0]
		self.thruster.FXmMZp = thruster_times_ms[1]
		self.thruster.FYmMZm = thruster_times_ms[2]
		self.thruster.FYmMZp = thruster_times_ms[3]
		self.thruster.FXpMZm = thruster_times_ms[4]
		self.thruster.FXpMZp = thruster_times_ms[5]
		self.thruster.FYpMZm = thruster_times_ms[6]
		self.thruster.FYpMZp = thruster_times_ms[7]


if __name__ == "__main__":
    pass