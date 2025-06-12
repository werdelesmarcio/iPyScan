import contextlib
import socket


class ResolutionError(Exception):
    """Custom exception for resolution errors."""

    pass

    """
    Resolve um Hostname para o IP Se o target já for um IP, retorna o mesmo.
    Se o target for um hostname, tenta resolver para o IP correspondente.
    Se a resolução falhar, levanta uma ResolutionError.
    """


def resolve_target(target):
    with contextlib.suppress(socket.error):
        socket.inet_aton(target)  # Verifica se o target é um IP válido
        return target  # Retorna o IP se já for um IP válido
    try:
        return socket.gethostbyname(target)
    except socket.gaierror as e:
        raise ResolutionError(f"[!] ERROR: Could not resolve '{target}'.") from e


def connect(target, port, timeout=0.1):
    """
    Tenta estabelecer uma conexão TCP com o target na porta especificada.
    Retorna True se a conexão for bem-sucedida, caso contrário, retorna False.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((target, port))
            return True
        except (socket.timeout, socket.error):
            return False


def grab_banner(target, port, timeout=0.1):
    """
    Tenta capturar informações sobre oserviço em execução na porta especificada.
    Retorna o banner como uma string ou None se não for possível obter o banner.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((target, port))

            # Ações ativas para tentar obter o banner
            if port in (80, 8080, 443, 8443):
                s.sendall(b"GET / HTTP/1.0\r\nHost: " + target.encode() + b"\r\n\r\n")
            elif port in (21, 22, 23, 25, 110, 143, 3306, 3389):
                s.sendall(b"HELP\r\n")
            elif port in (53, 67, 68, 123):
                s.sendall(b"\x00\x00\x00\x00")
            elif port in (135, 139, 445):
                s.sendall(b"\x00\x00\x00\x00\x00\x00\x00\x00")
            elif port in (161, 162):
                s.sendall(b"\x30\x0c\x02\x01\x00\x04\x06public\x02\x01\x00")
            elif port in (1433, 1521):
                s.sendall(b"\x00\x00\x00\x00\x00\x00\x00\x00")
            elif port in (3306, 5432):
                s.sendall(b"\x00\x00\x00\x00\x00\x00\x00\x00")
            elif port in (6379, 11211):
                s.sendall(b"*1\r\n$4\r\nPING\r\n")
            else:
                s.sendall(b"\r\n")

            raw_banner = s.recv(1024).decode(errors="ignore").strip()

            lines = raw_banner.splitlines()
            for line in lines:
                if line.strip():
                    cleaned = line.strip()
                    cleaned = cleaned.replace("\r", "").replace("\n", "")
                    return cleaned

    except (socket.timeout, socket.error, ConnectionResetError):
        return None
