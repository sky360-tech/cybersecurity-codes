# Generated automatically on 2026-09-24T01:48:30.894603
# Module: password_entropy

import math

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
