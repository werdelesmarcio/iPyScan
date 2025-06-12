import sys

def validate_input(argv):
    if len(sys.argv) != 4:
        print('\n [!] ERROR: Missing input arguments.')
        print(' [!] Usage: ./pyTCPScan.py [target] [initial_port] [final_port]\n')
        return False
    try:
        initial_port = int(sys.argv[2])
        final_port = int(sys.argv[3])
        if initial_port < 0 or final_port < 0 or initial_port > 65535 or final_port > 65535:
            print('\n [!] ERROR: Port numbers must be between 0 and 65535.')
            return False
        if initial_port > final_port:
            print('\n [!] ERROR: Initial port cannot be greater than final port.')
            return False
    except ValueError:  # Verifica se as portas são números inteiros
        print('\n [!] ERROR: Port numbers must be integers.')
        return False
    return True  # Retorna True se todos os parâmetros forem válidos