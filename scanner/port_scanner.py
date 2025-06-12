from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from scanner.network_utils import connect, grab_banner
from utils.exporter import export_results


def scan_ports(target, initial_port, final_port, max_threads=100):
    print(f" [*] Connecting to Target: {target}")
    print(f" [*] Scanning ports between {initial_port} and {final_port}...")
    print(f" [!] Please wait, scanning remote host: \033[1;33m{target}\033[m")
    print(" [*] This may take a while, be patient.\n")

    start_time = datetime.now()
    open_ports = []

    def scan_single_port(
        port,
    ):  # Função para mostrar a versão dos serviços em execução na porta
        if connect(target, port):
            banner = grab_banner(target, port)
            return (port, banner)
        return None

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {
            executor.submit(scan_single_port, port): port
            for port in range(initial_port, final_port + 1)
        }
        for future in as_completed(futures):
            result = future.result()
            if result:
                port, banner = result
                open_ports.append((port, banner))
                if banner:
                    print(
                        f" [+] POSITIVE TO Port {port}: Status: \033[1;31mOPEN\033[m - Service: {banner}"
                    )
                else:
                    print(
                        f" [+] POSITIVE TO Port {port}: Status: \033[1;31mOPEN\033[m - No service available"
                    )

    end_time = datetime.now()
    total_time = end_time - start_time
    print("\n" + "-" * 50)
    print(f" [!] Scanning Completed in: {total_time}")
    print(f' [!] Open ports found:\n\t{"\n\t".join(map(str, open_ports))}')
    print("-" * 50)

    export_results(open_ports, target, output_format="json")  # ou "csv"
