# Generated automatically on 2026-09-23T19:45:03.979531
# Module: hash_verifier

import hashlib

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
