#!/usr/bin/python3
# -*- coding: utf-8 -*-

# iPyScan Version 1.0 (Alfa)

# Imports necessários para a execução do software
import sys
from utils.banner import banner
from scanner.input_validation import validate_input
from scanner.network_utils import resolve_target
from scanner.port_scanner import scan_ports
from scanner.udp_scanner import scan_udp_ports  # Novo import


def main():
    banner()  # Exibe o banner do sistema
    validate_input()  # Valida os argumentos informados, se auxentes exibe a mensagem de erro.

    target = sys.argv[1] # Endereço do alvo
    initial_port = int(sys.argv[2]) # Porta inicial do range
    final_port = int(sys.argv[3]) # Porta final do range

    resolved_target = resolve_target(target) # Resolve o IP do endereço da url informada

    try:
        scan_type = input("Choose scan type (TCP/UDP): ").strip().upper()
        
        if scan_type == "TCP":
            scan_ports(resolved_target, initial_port, final_port)
        elif scan_type == "UDP":
            scan_udp_ports(resolved_target, initial_port, final_port)
        else:
            print("Invalid scan type. Choose 'TCP' or 'UDP'.")
            sys.exit(1)

    except KeyboardInterrupt:
        print('\n You pressed Ctrl+C')
        print(' The application has been stopped prematurely.')
        sys.exit(1)


if __name__ == '__main__':
    main()
