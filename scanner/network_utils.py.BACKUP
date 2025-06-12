import socket
import sys

def connect(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.1)
        try:
            s.connect((target, port))
            return True
        except (socket.timeout, socket.error):
            return False

def resolve_target(target):
    try:
        return socket.gethostbyname(target)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting.')
        sys.exit(1)