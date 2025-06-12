from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from scanner.network_utils import connect


def scan_ports(target, initial_port, final_port, max_threads=100):
    print(f" [*] Connecting to Target: {target}")
    print(f" [*] Scanning ports between {initial_port} and {final_port}...")
    print(f" [!] Please wait, scanning remote host: \033[1;33m{target}\033[m")
    print(" [*] This may take a while, be patient.\n")

    start_time = datetime.now()
    open_ports = []

    def scan_single_port(port):
        return port if connect(target, port) else None

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {
            executor.submit(scan_single_port, port): port
            for port in range(initial_port, final_port + 1)
        }
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                open_ports.append(result)
                print(f" [+] POSITIVE TO Port {result}:	Status: \033[1;31mOPEN\033[m")

    end_time = datetime.now()
    total_time = end_time - start_time
    print("\n" + "-" * 50)
    print(f" [!] Scanning Completed in: {total_time}")
    print(f' [!] Open ports found: {", ".join(map(str, open_ports))}')
    print("-" * 50)
