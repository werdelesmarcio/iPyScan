import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from unittest.mock import patch, MagicMock

from scanner.input_validation import validate_input
from scanner.network_utils import resolve_target, connect, ResolutionError, grab_banner


class TestInputValidation(unittest.TestCase):
    def test_valid_args(self):
        argv = ["ipyscan.py", "127.0.0.1", "20", "80"]
        result = validate_input(argv)
        self.assertEqual(result, ("127.0.0.1", 20, 80))

    def test_missing_args(self):
        argv = ["ipyscan.py", "127.0.0.1"]
        result = validate_input(argv)
        self.assertIsNone(result)

    def test_invalid_ports(self):
        argv = ["ipyscan.py", "127.0.0.1", "abc", "xyz"]
        result = validate_input(argv)
        self.assertIsNone(result)


class TestNetworkUtils(unittest.TestCase):
    def test_resolve_ip_direct(self):
        self.assertEqual(resolve_target("8.8.8.8"), "8.8.8.8")

    def test_resolve_hostname(self):
        self.assertIsInstance(resolve_target("localhost"), str)

    def test_resolve_invalid(self):
        with self.assertRaises(ResolutionError):
            resolve_target("invalid.localhost.unknown")

    def test_connect_false(self):
        self.assertFalse(connect("127.0.0.1", 65534))

    @patch("socket.socket")
    def test_connect_true_mocked(self, mock_socket_class):
        mock_socket = MagicMock()
        mock_socket.connect.return_value = None
        mock_socket_class.return_value.__enter__.return_value = mock_socket
        self.assertTrue(connect("127.0.0.1", 22))

    @patch("socket.socket")
    def test_grab_banner_mock(self, mock_socket_class):
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b"SSH-2.0-OpenSSH_7.9"
        mock_socket.connect.return_value = None
        mock_socket_class.return_value.__enter__.return_value = mock_socket

        banner = grab_banner("127.0.0.1", 22)
        self.assertIn("OpenSSH", banner)


if __name__ == "__main__":
    unittest.main()
