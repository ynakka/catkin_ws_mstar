#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Float64, Float32
from sensor_msgs.msg import Imu, MagneticField
import vectornav
import serial
import sys


def talker(imu_port):
    pub = rospy.Publisher('magnetometer', MagneticField, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        # imu_values = vectornav.get_imu(imu_port)

        # message = Imu()
        # message.header.stamp = rospy.get_rostime()
        # message.angular_velocity.x = imu_values['omega'][0]
        # message.angular_velocity.y = imu_values['omega'][1]
        # message.angular_velocity.z = imu_values['omega'][2]
        magnetic_field_values = vectornav.get_magnetic_field(imu_port)
        message = MagneticField()
        message.header.stamp = rospy.get_rostime()

        message.magnetic_field.x = magnetic_field_values['mag'][0]
        message.magnetic_field.y = magnetic_field_values['mag'][1]
        message.magnetic_field.z = magnetic_field_values['mag'][2]

        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__ == '__main__':

    imu_port = serial.Serial(sys.argv[1], 115200)
    try:
        talker(imu_port)
    except rospy.ROSInterruptException:
        pass