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
