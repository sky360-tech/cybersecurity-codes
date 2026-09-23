import os
import random
from datetime import datetime

CYBER_TEMPLATES = [
    ("port_scanner", """import socket

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
"""),
    ("hash_verifier", """import hashlib

def calculate_file_hashes(filepath: str) -> dict:
    '''Calculates MD5, SHA1, and SHA256 hashes of a file.'''
    hashes = {'md5': hashlib.md5(), 'sha1': hashlib.sha1(), 'sha256': hashlib.sha256()}
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                for h in hashes.values():
                    h.update(chunk)
        return {k: v.hexdigest() for k, v in hashes.items()}
    except FileNotFoundError:
        return {}

if __name__ == '__main__':
    print(calculate_file_hashes(__file__))
"""),
    ("ip_validator", """import ipaddress

def analyze_ip(ip_str: str) -> dict:
    '''Analyzes an IP address string for classification.'''
    try:
        ip = ipaddress.ip_address(ip_str)
        return {
            'ip': str(ip),
            'version': ip.version,
            'is_private': ip.is_private,
            'is_loopback': ip.is_loopback,
            'is_multicast': ip.is_multicast
        }
    except ValueError:
        return {'error': 'Invalid IP address'}

if __name__ == '__main__':
    print(analyze_ip('192.168.1.1'))
    print(analyze_ip('8.8.8.8'))
"""),
    ("subdomain_checker", """import urllib.request
import urllib.error

def check_subdomain(url: str) -> int:
    '''Sends a HEAD request to check HTTP availability.'''
    req = urllib.request.Request(url, method='HEAD')
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception:
        return 0

if __name__ == '__main__':
    print('HTTP Status:', check_subdomain('https://httpbin.org/get'))
"""),
    ("log_parser", """import re

LOG_PATTERN = r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?)" (\d{3})'

def parse_access_log_line(line: str) -> dict:
    '''Parses standard Nginx/Apache access log entries.'''
    match = re.search(LOG_PATTERN, line)
    if match:
        return {
            'ip': match.group(1),
            'timestamp': match.group(2),
            'request': match.group(3),
            'status': int(match.group(4))
        }
    return {}

if __name__ == '__main__':
    sample = '10.0.0.5 - - [23/Sep/2026:14:00:00 +0000] "GET /admin HTTP/1.1" 403'
    print(parse_access_log_line(sample))
"""),
    ("password_entropy", """import math

def calculate_entropy(password: str) -> float:
    '''Calculates Shannon Entropy for a password string.'''
    if not password:
        return 0.0
    pool_size = 0
    if any(c.islower() for c in password): pool_size += 26
    if any(c.isupper() for c in password): pool_size += 26
    if any(c.isdigit() for c in password): pool_size += 10
    if any(not c.isalnum() for c in password): pool_size += 32
    
    return len(password) * math.log2(pool_size) if pool_size > 0 else 0.0

if __name__ == '__main__':
    print('Entropy:', calculate_entropy('P@ssw0rd2026!'))
""")
]

def generate_daily_code():
    os.makedirs("security_tools", exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    name_prefix, code_body = random.choice(CYBER_TEMPLATES)
    
    filename = f"security_tools/{name_prefix}_{timestamp}.py"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Generated automatically on {datetime.utcnow().isoformat()}\n")
        f.write(f"# Module: {name_prefix}\n\n")
        f.write(code_body)
    
    print(f"Generated module: {filename}")

if __name__ == "__main__":
    generate_daily_code()
