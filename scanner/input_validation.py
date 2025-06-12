def validate_input(argv):  # Validador dos argumentos de entrada
    if len(argv) != 4:
        print("\n[!] ERROR: Missing input arguments.")
        print("\n   Usage: ./pyTCPScan.py [target] [initial_port] [final_port]\n")
        return None

    target = argv[1]

    try:
        initial_port = int(argv[2])
        final_port = int(argv[3])
    except ValueError:  # Checa se foram informados números inteiros para as portas
        print("\n [!] ERROR: Port numbers must be integers.")
        return None
    # Verifica se as portas estão dentro do intervalo válido
    if not (0 <= initial_port <= 65535) or not (0 <= final_port <= 65535):
        print("\n [!] ERROR: Port numbers must be between 0 and 65535.")
        return None
    # Verifica se as portas inicial e final são válidas
    if initial_port > final_port:
        print("\n [!] ERROR: Initial port cannot be greater than final port.")
        return None

    return (
        target,
        initial_port,
        final_port,
    )  # Retorna um tupla com os argumentos validados.
