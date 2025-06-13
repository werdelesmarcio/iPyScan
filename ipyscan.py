#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
iPyScan Version 1.0 (beta)
Desenvolvido por: Werdeles Marcio de C. Soares
E-mail: gh05tb0y@disroot.org
-----------------------------------------------------------------------------
iPyScan é um software de código aberto para escaneamento de portas TCP.
Ele foi desenvolvido para fins educacionais e de segurança, permitindo que
usuários verifiquem quais portas estão abertas em um determinado host
e identifiquem serviços em execução nessas portas. O software é escrito
em Python e utiliza bibliotecas padrão para realizar o escaneamento de forma
eficiente.
"""

# Imports necessários para a execução do software
import sys
import argparse

# Imports do projeto
from utils.banner import banner
from scanner.network_utils import resolve_target, ResolutionError
from scanner.port_scanner import scan_ports


def parse_args():
    """
    Função para analisar os argumentos de linha de comando.
    Retorna um objeto Namespace com os argumentos analisados.
    """
    # Menu de ajuda e opções do software
    # Define os argumentos que o software aceita
    parser = argparse.ArgumentParser(
        prog="iPyScan",
        description=(
            "iPyScan - TCP port scanner with banner grabbing and export.\n"
            "Scans hosts, identifies services and exports in JSON or CSV\n"
        ),
        epilog=(
            "Developed by (gh05tb0y) Werdeles Soares"
            "\nEx.:\n"
            "  ipyscan --target 127.0.0.1 --ports 20-80 --output json\n"
            "  ipyscan --target scanme.nmap.org --ports 1-1000 --threads 200 --output csv\n"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--target",
        required=True,
        help="Hostname or IP address of the target to be scanned.",
    )
    parser.add_argument(
        "--ports",
        required=True,
        help="Port range (e.g. 20-80).",
    )
    parser.add_argument(
        "--threads",
        default=100,
        type=int,
        help="Number of threads (default: 100).",
    )
    parser.add_argument(
        "--output",
        choices=["json", "csv"],
        default="json",
        help="Output format (json or csv, default: json).",
    )
    return parser.parse_args()


def main():
    banner()  # Exibe o banner do software
    args = (
        parse_args()
    )  # Valida os argumentos informados, se auxentes exibe a mensagem de erro.

    try:
        resolved_target = resolve_target(args.target)
    except ResolutionError as e:  # Captura erros de resolução de hostname
        print(e)
        sys.exit(1)

    try:
        port_range = args.ports.split("-")
        initial_port = int(port_range[0])
        final_port = int(port_range[1])
        if not (0 <= initial_port <= 65535 and 0 <= final_port <= 65535):
            raise ValueError("Ports must be between 0 and 65535.")
    except ValueError as e:  # Captura erros de conversão de portas
        print(f"Error processing port range: {e}")
        sys.exit(1)

    scan_ports(
        target=resolved_target,
        initial_port=initial_port,
        final_port=final_port,
        max_threads=args.threads,
        output_format=args.output,
    )


if __name__ == "__main__":
    main()
