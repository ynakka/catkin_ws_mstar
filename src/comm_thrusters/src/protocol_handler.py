#!/usr/bin/env python3

import serial
import sys
import rospy
# from hivemind.msg import Thrusters8
from comm_thrusters.msg import Thrusters8

from std_msgs.msg import Bool, Int8, Float32


def get_line(port):
    buf = b''
    while True:
        c = port.read(1)
        buf = buf + c
        if c == b'\n':
            return buf.decode('ascii')


def get_command(port):
    words = get_line(port).rstrip('\n').split(' ')
    command_name = words[0]
    command_args = words[1:]
    return command_name, command_args


class CommandHandlers:
    def __init__(self, prefix):
        self.prefix = prefix
        self.commands = {
            'error': self.handle_error_msg,
        }

    def handle_error_msg(self, *args):
        rospy.logerr(str(args))



    def handle_command(self, command_name, command_args):
        if command_name in self.commands:
            self.commands[command_name](*command_args)
        else:
            pass
            # rospy.logerr(f'unknown command {command_name} with arguments {command_args}')
