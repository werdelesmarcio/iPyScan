from datetime import datetime
from scanner.network_utils import connect

def scan_ports(target, initial_port, final_port):
    print(f' [*] Connecting to Target: {target}')
    print(f' [*] Scanning ports between {initial_port} and {final_port}...')
    print(f' [!] Please wait, scanning remote host: \033[1;33m{target}\033[m')
    print(' [*] This may take a while, be patient.\n')

    start_time = datetime.now()

    for port in range(initial_port, final_port + 1):
        if connect(target, port):
            print(f' [+] POSITIVE TO Port {port}:	Status: \033[1;31mOPEN\033[m')

    end_time = datetime.now()
    total_time = end_time - start_time
    
    print('\n' + '-' * 50)
    print(f' [!] Scanning Completed in: {total_time}')
    print('-' * 50)
