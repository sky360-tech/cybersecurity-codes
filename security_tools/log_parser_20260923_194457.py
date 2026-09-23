# Generated automatically on 2026-09-23T19:44:57.775989
# Module: log_parser

import re

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
