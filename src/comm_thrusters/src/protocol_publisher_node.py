#!/usr/bin/env python3

import rospy
import serial
import threading
import protocol_handler as p
# from hivemind.msg import Thrusters8
from comm_thrusters.msg import Thrusters8

from std_msgs.msg import Bool, Int8, Float32
import sys
from serial.tools import list_ports


class PortNotFound(Exception):
    pass

def get_serialport(manuf, prod, serial_number=None):
    ports = [p for p in list_ports.comports()
             if p.manufacturer == manuf
                and p.product == prod
                and (serial_number == None or p.serial_number == serial_number)]
    if len(ports) == 0:
        available = [(p.manufacturer, p.product, p.serial_number) for p in list_ports.comports()]
        raise PortNotFound('port not found, available ports are: {}'.format(available))
    return ports[0].device



def serial_comm_publisher(serial_port, prefix):
    cmd_handler = p.CommandHandlers(prefix)

    while not rospy.is_shutdown():
        [command_name, command_args] = p.get_command(serial_port)
        cmd_handler.handle_command(command_name, command_args)


def serial_comm_send(serial_port, command, *args):
    buf = command + ' '
    for arg in args:
        buf += str(arg) + ' '
    buf += '\n'

    serial_port.write(buf.encode('ascii'))
    serial_port.flush()


def handle_thrusters_setpt(msg, serial_port):
    serial_comm_send(serial_port, 'thrusters', msg.FXpMZp, msg.FXpMZm,
                                                msg.FXmMZp, msg.FXmMZm,
                                                msg.FYpMZp, msg.FYpMZm,
                                                msg.FYmMZp, msg.FYmMZm)


def handle_gripper_setpt(msg, serial_port):
    serial_comm_send(serial_port, 'gripper', int(msg.data))



if __name__ == '__main__':
    rospy.init_node('serial_comm', anonymous=True)
    prefix = sys.argv[1]
    # serial_port = serial.Serial(sys.argv[1], 115200)
    serial_port = serial.Serial(get_serialport('Sorina', 'INSboard', '510'), baudrate=115200)
    pub_thd = threading.Thread(target=serial_comm_publisher, args=[serial_port, prefix])
    pub_thd.start()
    rospy.Subscriber(prefix + "/thruster_msg", Thrusters8, handle_thrusters_setpt, callback_args=serial_port)

    while not rospy.is_shutdown():
        rospy.spin()

