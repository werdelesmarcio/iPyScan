import sys

def validate_input():
    if len(sys.argv) != 4:
        print('\n [!] ERROR: Missing input arguments.')
        print(' [!] Usage: ./pyTCPScan.py [target] [initial_port] [final_port]\n')
        sys.exit(1)
