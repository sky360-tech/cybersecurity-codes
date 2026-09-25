# Generated automatically on 2026-09-25T02:04:59.690394
# Module: subdomain_checker

import urllib.request
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
