# Generated automatically on 2026-09-25T02:05:04.809031
# Module: ip_validator

import ipaddress

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
