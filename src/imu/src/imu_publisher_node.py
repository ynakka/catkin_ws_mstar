#!/usr/bin/env python3

import rospy
from std_msgs.msg import String, Float64, Float32
from sensor_msgs.msg import Imu, MagneticField
import vectornav
import serial
import sys


def talker(imu_port):
    pub = rospy.Publisher(sys.argv[2] + '/Imu', Imu, queue_size=10)
    rospy.init_node('imu', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        imu_values = vectornav.get_imu(imu_port)
        message = Imu()
        message.header.stamp = rospy.get_rostime()
        message.angular_velocity.x = imu_values['omega'][0]
        message.angular_velocity.y = imu_values['omega'][1]
        message.angular_velocity.z = imu_values['omega'][2]
        message.linear_acceleration.x = imu_values['acc'][0]
        message.linear_acceleration.y = imu_values['acc'][1]
        message.linear_acceleration.z = imu_values['acc'][2]

        # rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':

    imu_port = serial.Serial(sys.argv[1], 115200)
    try:
        talker(imu_port)
    except rospy.ROSInterruptException:
        pass