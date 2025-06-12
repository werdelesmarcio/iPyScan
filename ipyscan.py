#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
iPyScan Version 1.0 (beta)
Desenvolvido por: Werdeles Marcio de C. Soares
E-mail: gh05tb0y@disroot.org
----------------------------------
iPyScan é um software de código aberto para escaneamento de portas TCP.
Ele foi desenvolvido para fins educacionais e de segurança, permitindo que
usuários verifiquem quais portas estão abertas em um determinado host
e identifiquem serviços em execução nessas portas. O software é escrito
em Python e utiliza bibliotecas padrão para realizar o escaneamento de forma
eficiente.
"""

# Imports necessários para a execução do software
import sys

# from utils.banner import banner
from scanner.input_validation import validate_input
from scanner.network_utils import resolve_target, ResolutionError
from scanner.port_scanner import scan_ports


def main():
    args = validate_input(
        sys.argv
    )  # Valida os argumentos informados, se auxentes exibe a mensagem de erro.
    if not args:
        sys.exit(1)

    target, initial_port, final_port = args  # Desempacota os argumentos validados

    try:
        resolved_target = resolve_target(target)
    except ResolutionError as e:  # Captura erros de resolução de hostname
        print(e)
        sys.exit(1)

    try:
        scan_ports(
            resolved_target, initial_port, final_port
        )  # Função que escaneia o endereço levando em consideração o range de portas informados
    except KeyboardInterrupt:  # Interrupção de execução do sistema
        print("\n You pressed Ctrl+C")
        print(" The application has been stopped prematurely.\n")
        sys.exit(1)  # Mata a execução


if __name__ == "__main__":
    main()
