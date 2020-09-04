#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import Imu, MagneticField

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    rospy.loginfo(rospy.get_caller_id() + "I heard {}".format(data))


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("MagField", MagneticField, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()