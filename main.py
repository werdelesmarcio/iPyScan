#!/usr/bin/python3
# -*- coding: utf-8 -*-

# PyTCPScan Version 2.1 (Alfa)

# Relação de todos os Imports necessários para a execução do software
import sys
from utils.banner import banner
from scanner.input_validation import validate_input
from scanner.network_utils import resolve_target
from scanner.port_scanner import scan_ports

def main():
    banner()  # Exibe o banner
    validate_input()  # Valida os argumentos

    target = sys.argv[1]
    initial_port = int(sys.argv[2])
    final_port = int(sys.argv[3])

    resolved_target = resolve_target(target)

    try:
        scan_ports(resolved_target, initial_port, final_port)
    except KeyboardInterrupt:
        print('\n You pressed Ctrl+C')
        print(' The application has been stopped prematurely.')
        sys.exit(1)

if __name__ == '__main__':
    main()
