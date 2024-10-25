import socket
from datetime import datetime

def connect_udp(target, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(0.1)
        try:
            s.sendto(b'', (target, port))
            s.recvfrom(1024)  # Tenta receber uma resposta
            return True  # A porta está aberta ou respondendo
        except socket.error:
            return False  # Nenhuma resposta significa porta fechada

def scan_udp_ports(target, initial_port, final_port):
    print(f' [*] Scanning UDP ports on Target: {target}')
    print(f' [*] Scanning ports between {initial_port} and {final_port}...\n')

    start_time = datetime.now()

    for port in range(initial_port, final_port + 1):
        if connect_udp(target, port):
            print(f' [+] POSITIVE TO Port {port}:	Status: \033[1;31mOPEN\033[m')

    end_time = datetime.now()
    total_time = end_time - start_time
    print('\n' + '-' * 50)
    print(f' [!] UDP Scanning Completed in: {total_time}')
    print('-' * 50)
