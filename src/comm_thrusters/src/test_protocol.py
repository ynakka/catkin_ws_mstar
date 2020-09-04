import unittest
from unittest import mock
import sys
import protocol_handler as p


class TestWaitData(unittest.TestCase):

    def test_get_line(self):
        port = mock.Mock()
        port.read = mock.Mock(side_effect=[bytes([c]) for c in b"command 1 0\n"])
        self.assertEqual(p.get_line(port), 'command 1 0\n')

    def test_get_line_just_enter(self):
        port = mock.Mock()
        port.read = mock.Mock(side_effect=[bytes([c]) for c in b"\n"])
        self.assertEqual(p.get_line(port), '\n')

    # def test_get_line_no_command(self):
    #     port = mock.Mock()
    #     port.read = mock.Mock(side_effect=[bytes([c]) for c in b''])
    #     self.assertEqual(p.get_line(port), '')

    def test_get_command(self):
        port = mock.Mock()
        port.read = mock.Mock(side_effect=[bytes([c]) for c in b"command 1 0\n"])
        self.assertEqual(p.get_command(port), ('command', ['1', '0']))
