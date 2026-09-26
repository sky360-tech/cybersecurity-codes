# Generated automatically on 2026-09-26T02:10:27.635821
# Module: port_scanner

import socket

def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    '''Checks if a TCP port is open on a target host.'''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

if __name__ == '__main__':
    target = '127.0.0.1'
    for p in [22, 80, 443, 8080]:
        status = 'OPEN' if scan_port(target, p) else 'CLOSED'
        print(f'Port {p}: {status}')
